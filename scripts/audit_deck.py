#!/usr/bin/env python3
"""Audit awal deck PPTX untuk workshop-skills.

Skrip ini menandai slide yang perlu diperiksa ulang sebelum deck diserahkan:
kisi kartu teks, teks layar yang melebihi batas mode, gambar yang dipakai ulang,
dan catatan pembicara yang hanya berisi daftar sumber.

Hasilnya adalah daftar tanda, bukan penilaian akhir. Apakah sebuah visual benar-benar
menjelaskan pesan tetap diputuskan lewat pembacaan render setiap slide.

Pemakaian:
    python3 -I audit_deck.py deck.pptx --mode normal
    python3 -I audit_deck.py deck.pptx --mode detail --json

Kode keluar 0 berarti lolos gerbang, 1 berarti ada pelanggaran yang wajib direvisi.
Hanya memakai pustaka standar Python.
"""

import argparse
import json
import posixpath
import re
import sys
import zipfile
from collections import defaultdict
from xml.etree import ElementTree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"

# Batas kata di luar judul, sumber, dan nomor slide. Normal ditetapkan Wira (K-261024-01).
WORD_LIMIT = {"normal": 45, "detail": 220}
# Proporsi maksimal slide kisi kartu sebelum gerbang gagal.
MAX_CARD_RATIO = 0.10
# Catatan pembicara di bawah jumlah kata ini dianggap belum berisi naskah bicara.
MIN_SCRIPT_WORDS = 25

SOURCE_LINE = re.compile(r"^\s*(sumber|source|ilustrasi|kredit|credit|foto|photo)\b", re.I)
REFERENCE_NOTE = re.compile(r"(https?://|doi\.org|diakses|accessed|\bdoi\b|^sumber|^jalur)", re.I)
REFERENCE_TITLE = re.compile(r"(referensi|rujukan|daftar pustaka|references|bibliograf)", re.I)
CARD_SHAPES = {"rect", "roundRect", "snip1Rect", "round1Rect", "round2SameRect"}


def words(text):
    return re.findall(r"[\w%.,/-]+", text)


def rels_of(zf, part):
    folder, name = posixpath.split(part)
    rel_path = posixpath.join(folder, "_rels", name + ".rels")
    if rel_path not in zf.namelist():
        return {}
    root = ET.fromstring(zf.read(rel_path))
    out = {}
    for rel in root.iter(REL_NS + "Relationship"):
        target = rel.get("Target")
        if rel.get("TargetMode") != "External":
            target = posixpath.normpath(posixpath.join(folder, target))
        out[rel.get("Id")] = (rel.get("Type", "").rsplit("/", 1)[-1], target)
    return out


def slide_parts(zf):
    pres = ET.fromstring(zf.read("ppt/presentation.xml"))
    rels = rels_of(zf, "ppt/presentation.xml")
    size = pres.find("p:sldSz", NS)
    order = [rels[s.get("{%s}id" % NS["r"])][1] for s in pres.find("p:sldIdLst", NS)]
    return order, int(size.get("cx")), int(size.get("cy"))


def box(el):
    xfrm = el.find(".//a:xfrm", NS)
    if xfrm is None or xfrm.find("a:off", NS) is None or xfrm.find("a:ext", NS) is None:
        return None
    off, ext = xfrm.find("a:off", NS), xfrm.find("a:ext", NS)
    return int(off.get("x")), int(off.get("y")), int(ext.get("cx")), int(ext.get("cy"))


def shape_text(sp):
    paras = []
    for para in sp.findall(".//a:p", NS):
        line = "".join(t.text or "" for t in para.findall(".//a:t", NS)).strip()
        if line:
            paras.append(line)
    return paras


def similar(a, b, tol=0.12):
    return abs(a - b) <= tol * max(a, b)


def ph_idx(el):
    ph = el.find(".//p:nvPr/p:ph", NS)
    return None if ph is None else ph.get("idx", "0")


def layout_boxes(zf, rels):
    """Posisi placeholder di layout. Placeholder di slide mewarisinya bila tidak menyimpan posisi sendiri."""
    layout = next((t for kind, t in rels.values() if kind == "slideLayout"), None)
    if not layout or layout not in zf.namelist():
        return {}
    root = ET.fromstring(zf.read(layout))
    out = {}
    for el in list(root.iter("{%s}sp" % NS["p"])) + list(root.iter("{%s}pic" % NS["p"])):
        idx, b = ph_idx(el), box(el)
        if idx is not None and b:
            out[idx] = b
    return out


def audit_slide(zf, part, sw, sh):
    root = ET.fromstring(zf.read(part))
    rels = rels_of(zf, part)
    area = sw * sh
    inherited = layout_boxes(zf, rels)

    def shape_box(el):
        return box(el) or inherited.get(ph_idx(el))

    title, body_words, cards, pics = "", 0, [], []
    text_shapes = []
    for sp in root.iter("{%s}sp" % NS["p"]):
        paras = shape_text(sp)
        if not paras:
            continue
        ph = sp.find(".//p:nvPr/p:ph", NS)
        geom = sp.find(".//a:prstGeom", NS)
        text_shapes.append({
            "paras": paras,
            "box": shape_box(sp),
            "is_title": ph is not None and ph.get("type") in ("title", "ctrTitle"),
            "geom": geom.get("prst") if geom is not None else None,
        })

    # Judul: placeholder judul bila ada, bila tidak ada pakai teks paling atas di 20% tinggi slide.
    title_shape = next((s for s in text_shapes if s["is_title"]), None)
    if title_shape is None:
        top = [s for s in text_shapes if s["box"] and s["box"][1] < 0.2 * sh]
        title_shape = min(top, key=lambda s: s["box"][1]) if top else None
    if title_shape is not None:
        title = " ".join(title_shape["paras"])

    for s in text_shapes:
        if s is title_shape:
            continue
        kept = [p for p in s["paras"] if not SOURCE_LINE.match(p) and not p.strip().isdigit()]
        body_words += sum(len(words(p)) for p in kept)
        b = s["box"]
        if b and s["geom"] in CARD_SHAPES and 0.015 * area <= b[2] * b[3] <= 0.3 * area:
            cards.append(b)

    # Kartu tanpa teks yang menjadi latar kotak teks juga umum; hitung kotak teks yang berdempet ukuran.
    groups = []
    for c in cards:
        for g in groups:
            if similar(g[0][2], c[2]) and similar(g[0][3], c[3]):
                g.append(c)
                break
        else:
            groups.append([c])
    card_grid = max((len(g) for g in groups), default=0)

    for pic in root.iter("{%s}pic" % NS["p"]):
        b = shape_box(pic)
        blip = pic.find(".//a:blip", NS)
        rid = blip.get("{%s}embed" % NS["r"]) if blip is not None else None
        target = rels.get(rid, (None, None))[1]
        frac = (b[2] * b[3]) / area if b else 0.0
        pics.append((target, min(frac, 1.0)))

    # Latar gambar yang dipasang lewat bg slide.
    bg = root.find(".//p:bg//a:blip", NS)
    if bg is not None:
        target = rels.get(bg.get("{%s}embed" % NS["r"]), (None, None))[1]
        pics.append((target, 1.0))

    notes_part = next((t for kind, t in rels.values() if kind == "notesSlide"), None)
    script_words = 0
    if notes_part and notes_part in zf.namelist():
        nroot = ET.fromstring(zf.read(notes_part))
        for sp in nroot.iter("{%s}sp" % NS["p"]):
            ph = sp.find(".//p:nvPr/p:ph", NS)
            if ph is not None and ph.get("type") in ("sldImg", "sldNum"):
                continue
            for para in shape_text(sp):
                if not REFERENCE_NOTE.search(para):
                    script_words += len(words(para))

    return {
        "title": title,
        "body_words": body_words,
        "card_grid": card_grid,
        "pics": pics,
        "image_area": round(max((f for _, f in pics), default=0.0), 2),
        "script_words": script_words,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--mode", choices=sorted(WORD_LIMIT), default="normal")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    with zipfile.ZipFile(args.deck) as zf:
        order, sw, sh = slide_parts(zf)
        slides = [audit_slide(zf, part, sw, sh) for part in order]

    limit = WORD_LIMIT[args.mode]
    usage = defaultdict(list)
    for i, s in enumerate(slides, 1):
        for target, frac in s["pics"]:
            if target and frac >= 0.15:
                usage[target].append(i)
    reused = {t: idx for t, idx in usage.items() if len(idx) > 1}

    rows, content = [], 0
    for i, s in enumerate(slides, 1):
        flags = []
        is_ref = bool(REFERENCE_TITLE.search(s["title"]))
        if not is_ref:
            content += 1
            if s["card_grid"] >= 3 and s["image_area"] < 0.35:
                flags.append("KISI_KARTU")
            if s["body_words"] > limit:
                flags.append("TEKS_%d>%d" % (s["body_words"], limit))
            if s["script_words"] < MIN_SCRIPT_WORDS:
                flags.append("TANPA_NASKAH")
            if any(i in idx for idx in reused.values()):
                flags.append("GAMBAR_ULANG")
            if s["image_area"] == 0 and s["card_grid"] < 3:
                flags.append("TANPA_VISUAL?")
        rows.append({"slide": i, **{k: v for k, v in s.items() if k != "pics"}, "referensi": is_ref, "flags": flags})

    grid = sum("KISI_KARTU" in r["flags"] for r in rows)
    over = sum(any(f.startswith("TEKS_") for f in r["flags"]) for r in rows)
    no_script = sum("TANPA_NASKAH" in r["flags"] for r in rows)
    grid_ratio = grid / content if content else 0.0
    failed = grid_ratio > MAX_CARD_RATIO or over > 0 or no_script > 0
    summary = {
        "deck": args.deck, "mode": args.mode, "slides": len(slides), "slide_isi": content,
        "kisi_kartu": grid, "rasio_kisi_kartu": round(grid_ratio, 2), "melebihi_batas_kata": over,
        "tanpa_naskah": no_script, "gambar_dipakai_ulang": reused, "lolos": not failed,
    }

    if args.json:
        print(json.dumps({"ringkasan": summary, "slide": rows}, ensure_ascii=False, indent=2))
    else:
        print(f"{'No':>3}  {'Kata':>4}  {'Gbr':>4}  {'Naskah':>6}  {'Judul':<48}  Tanda")
        for r in rows:
            print(f"{r['slide']:>3}  {r['body_words']:>4}  {r['image_area']:>4}  {r['script_words']:>6}  "
                  f"{r['title'][:48]:<48}  {' '.join(r['flags'])}")
        print()
        for k, v in summary.items():
            print(f"{k}: {v}")
        print("\nTanda adalah petunjuk. Putusan infografis tetap dibuat dari render setiap slide.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
