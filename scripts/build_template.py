#!/usr/bin/env python3
"""Bangun template PowerPoint workshop-skills.

Template berisi delapan layout 16:9 dengan zona tetap untuk judul, gambar, label,
bar kesimpulan, sumber, dan nomor slide. Palet dan font mengikuti deck acuan:
navy, teal, emas, merah untuk risiko, serta Inter Display dan Inter.

Pemakaian:
    python3 build_template.py                 # menulis templates/workshop-template.pptx dan .potx
    python3 build_template.py --out <folder>

Memerlukan python-pptx (diuji pada 1.0.2). Ubah konstanta PALET, FONT, dan LAYOUT
di bawah, lalu jalankan ulang untuk menghasilkan template baru.
"""

import argparse
import copy
import os
import re
import shutil
import zipfile

from lxml import etree
from pptx import Presentation
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.util import Emu, Inches

PALET = {
    "navy": "061D32",
    "navy2": "082743",
    "teal": "2697AF",
    "cyan": "0BABB8",
    "emas": "F5B84A",
    "merah": "D64545",
    "latar": "F7F9FB",
    "abu": "5B6B7C",
    "putih": "FFFFFF",
}
FONT = {"judul": "Inter Display", "isi": "Inter"}

W, H = Inches(13.333), Inches(7.5)
M = Inches(0.5)
FOOT_Y, FOOT_H = Inches(7.05), Inches(0.3)
BAR_Y, BAR_H = Inches(6.35), Inches(0.6)
TITLE_Y, TITLE_H = Inches(0.3), Inches(0.85)

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
NSDECL = 'xmlns:a="%s" xmlns:p="%s" xmlns:r="%s"' % (NS["a"], NS["p"], NS["r"])


def run_props(size, color, bold=False, font="isi", caps=False):
    face = "+mj-lt" if font == "judul" else "+mn-lt"
    return (
        '<a:defRPr sz="%d" b="%d"%s><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
        '<a:latin typeface="%s"/></a:defRPr>'
        % (size, 1 if bold else 0, ' cap="all"' if caps else "", PALET[color], face)
    )


def placeholder(sid, name, ph_type, idx, box, prompt, size=1800, color="navy", bold=False,
                font="isi", anchor="t", align="l", caps=False):
    x, y, w, h = (int(v) for v in box)
    ph_attr = 'type="%s" ' % ph_type if ph_type else ""
    text = ""
    if ph_type != "pic":
        text = (
            '<p:txBody><a:bodyPr wrap="square" lIns="0" rIns="0" tIns="0" bIns="0" anchor="%s">'
            '<a:normAutofit/></a:bodyPr><a:lstStyle><a:lvl1pPr marL="0" indent="0" algn="%s">'
            '<a:buNone/>%s</a:lvl1pPr></a:lstStyle><a:p><a:r><a:rPr lang="id-ID"/><a:t>%s</a:t></a:r></a:p></p:txBody>'
            % (anchor, align, run_props(size, color, bold, font, caps), prompt)
        )
    else:
        text = ('<p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle><a:lvl1pPr algn="ctr">%s</a:lvl1pPr>'
                '</a:lstStyle><a:p><a:r><a:rPr lang="id-ID"/><a:t>%s</a:t></a:r></a:p></p:txBody>'
                % (run_props(1400, "abu"), prompt))
    return (
        '<p:sp %s><p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
        '<p:nvPr><p:ph %sidx="%d"/></p:nvPr></p:nvSpPr><p:spPr><a:xfrm><a:off x="%d" y="%d"/>'
        '<a:ext cx="%d" cy="%d"/></a:xfrm>%s</p:spPr>%s</p:sp>'
        % (NSDECL, sid, name, ph_attr, idx, x, y, w, h,
           '<a:solidFill><a:srgbClr val="E3E9EF"/></a:solidFill>' if ph_type == "pic" else "", text)
    )


def rect(sid, name, box, color):
    x, y, w, h = (int(v) for v in box)
    return (
        '<p:sp %s><p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr/><p:nvPr userDrawn="1"/></p:nvSpPr>'
        '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
        '<a:ln><a:noFill/></a:ln></p:spPr></p:sp>' % (NSDECL, sid, name, x, y, w, h, PALET[color])
    )


def title(sid, color="navy", box=None):
    return placeholder(sid, "Judul", "title", 0, box or (M, TITLE_Y, W - 2 * M, TITLE_H),
                       "Judul: tindakan, akibat, atau pertanyaan", 3000, color, True, "judul", "b")


def footer(sid, on_dark=False):
    color = "putih" if on_dark else "abu"
    return [
        placeholder(sid, "Sumber", "body", 20, (M, FOOT_Y, Inches(9.5), FOOT_H),
                    "Sumber: Penulis, tahun, hlm. x", 900, color),
        placeholder(sid + 1, "Nomor slide", "sldNum", 21, (W - M - Inches(1), FOOT_Y, Inches(1), FOOT_H),
                    "", 900, color, align="r"),
    ]


def bar(sid):
    return [
        rect(sid, "Bar kesimpulan", (0, BAR_Y, W, BAR_H), "navy"),
        rect(sid + 1, "Aksen emas", (0, BAR_Y, Inches(0.12), BAR_H), "emas"),
        placeholder(sid + 2, "Kesimpulan", "body", 22, (M, BAR_Y, W - 2 * M, BAR_H),
                    "Satu kalimat kesimpulan", 1600, "putih", True, anchor="ctr"),
    ]


def body_area_y():
    return TITLE_Y + TITLE_H + Inches(0.2)


def layouts():
    top = body_area_y()
    area_h = BAR_Y - top - Inches(0.2)
    out = {}

    left_w = Inches(5.6)
    out["Cover"] = [
        rect(2, "Panel navy", (0, 0, left_w, H), "navy"),
        rect(3, "Aksen emas", (Inches(0.35), Inches(1.4), Inches(0.08), Inches(4.4)), "emas"),
        placeholder(4, "Gambar cover", "pic", 10, (left_w, 0, W - left_w, H), "Gambar: adegan dari dunia kerja audiens"),
        placeholder(5, "Judul", "ctrTitle", 0, (Inches(0.7), Inches(1.4), Inches(4.6), Inches(2.4)),
                    "Judul sesi", 4000, "putih", True, "judul", "b"),
        placeholder(6, "Subjudul", "subTitle", 1, (Inches(0.7), Inches(4.0), Inches(4.6), Inches(1.2)),
                    "Satu kalimat janji sesi", 1800, "putih"),
        placeholder(7, "Pembicara", "body", 23, (Inches(0.7), Inches(5.5), Inches(4.6), Inches(0.4)),
                    "Nama pembicara | penyelenggara", 1400, "emas", True),
    ]

    out["Pembuka bagian"] = [
        # Bentuk di layout selalu tergambar di bawah isi slide, jadi gambar berhenti tepat di atas pita navy.
        placeholder(2, "Gambar latar", "pic", 10, (0, 0, W, Inches(4.6)), "Gambar suasana bagian"),
        rect(3, "Pita navy", (0, Inches(4.6), W, Inches(2.9)), "navy"),
        placeholder(4, "Label bagian", "body", 24, (M, Inches(4.9), Inches(6), Inches(0.4)),
                    "Bagian 2", 1400, "emas", True, caps=True),
        title(5, "putih", (M, Inches(5.35), W - 2 * M, Inches(1.2))),
    ] + footer(6, on_dark=True)

    out["Visual penuh"] = [
        title(2),
        placeholder(3, "Gambar utama", "pic", 10, (0, top, W, area_h),
                    "Gambar penjelas tanpa teks. Label ditulis native di atasnya."),
    ] + bar(4) + footer(7)

    half = (W - 2 * M - Inches(0.3)) / 2
    out["Sebelum dan sesudah"] = [
        title(2),
        placeholder(3, "Label kiri", "body", 12, (M, top, half, Inches(0.4)), "Sebelum", 1600, "teal", True, caps=True),
        placeholder(4, "Label kanan", "body", 13, (M + half + Inches(0.3), top, half, Inches(0.4)),
                    "Sesudah", 1600, "emas", True, caps=True),
        placeholder(5, "Gambar kiri", "pic", 10, (M, top + Inches(0.5), half, area_h - Inches(0.5)), "Adegan sebelum"),
        placeholder(6, "Gambar kanan", "pic", 11, (M + half + Inches(0.3), top + Inches(0.5), half, area_h - Inches(0.5)),
                    "Adegan sesudah, objek sama"),
    ] + bar(7) + footer(10)

    n, gap = 4, Inches(0.2)
    pw = (W - 2 * M - gap * (n - 1)) / n
    panels = [title(2)]
    for i in range(n):
        x = M + i * (pw + gap)
        panels.append(placeholder(3 + 3 * i, "Jam %d" % (i + 1), "body", 30 + i, (x, top, pw, Inches(0.4)),
                                  "10.1%d" % (5 + i), 1600, "teal", True))
        panels.append(placeholder(4 + 3 * i, "Panel %d" % (i + 1), "pic", 10 + i,
                                  (x, top + Inches(0.45), pw, Inches(2.9)), "Adegan langkah %d" % (i + 1)))
        panels.append(placeholder(5 + 3 * i, "Keterangan %d" % (i + 1), "body", 40 + i,
                                  (x, top + Inches(3.45), pw, area_h - Inches(3.45)), "Siapa melakukan apa", 1300, "navy"))
    out["Skenario berjam"] = panels + bar(20) + footer(23)

    out["Detail"] = [
        title(2),
        placeholder(3, "Subjudul", "body", 1, (M, TITLE_Y + TITLE_H, W - 2 * M, Inches(0.4)),
                    "Subjudul yang menjelaskan konteks", 1500, "teal"),
        placeholder(4, "Isi berlapis", "body", 2, (M, top + Inches(0.3), Inches(6.6), area_h - Inches(0.3)),
                    "Contoh, angka, langkah. Mode Detail boleh padat asalkan tertata.", 1300, "navy"),
        placeholder(5, "Gambar", "pic", 10, (M + Inches(6.9), top + Inches(0.3), W - 2 * M - Inches(6.9), area_h - Inches(0.3)),
                    "Visual penjelas"),
    ] + bar(6) + footer(9)

    out["Tugas latihan"] = [
        title(2),
        placeholder(3, "Langkah", "body", 1, (M, top, Inches(5.6), area_h),
                    "Langkah yang bisa diamati, satu per baris", 1600, "navy"),
        placeholder(4, "Label contoh", "body", 12, (M + Inches(5.9), top, Inches(6), Inches(0.4)),
                    "Contoh hasil jadi", 1400, "emas", True, caps=True),
        placeholder(5, "Contoh hasil", "pic", 10, (M + Inches(5.9), top + Inches(0.45), W - 2 * M - Inches(5.9), area_h - Inches(0.45)),
                    "Gambar contoh hasil jadi"),
    ] + bar(6) + footer(9)

    out["Referensi"] = [
        title(2),
        placeholder(3, "Daftar referensi", "body", 1, (M, top, W - 2 * M, FOOT_Y - top - Inches(0.2)),
                    "Penulis. (Tahun). Judul. Venue. https://doi.org/...", 1200, "navy"),
    ] + footer(4)
    return out


def set_theme(prs):
    master = prs.slide_masters[0]
    theme = master.part.part_related_by(RT.THEME)
    xml = theme.blob.decode("utf-8")
    slots = {"dk1": "navy", "lt1": "putih", "dk2": "navy2", "lt2": "latar", "accent1": "teal",
             "accent2": "emas", "accent3": "cyan", "accent4": "merah", "accent5": "navy2",
             "accent6": "abu", "hlink": "teal", "folHlink": "cyan"}
    for slot, key in slots.items():
        xml = re.sub(r"<a:%s>.*?</a:%s>" % (slot, slot),
                     '<a:%s><a:srgbClr val="%s"/></a:%s>' % (slot, PALET[key], slot), xml, flags=re.S)
    xml = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*', r"\g<1>" + FONT["judul"], xml)
    xml = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*', r"\g<1>" + FONT["isi"], xml)
    xml = re.sub(r'<a:clrScheme name="[^"]*"', '<a:clrScheme name="workshop-skills"', xml)
    theme._blob = xml.encode("utf-8")


def set_master_background(prs):
    csld = prs.slide_masters[0]._element.find("p:cSld", NS)
    old = csld.find("p:bg", NS)
    if old is not None:
        csld.remove(old)
    bg = etree.fromstring('<p:bg %s><p:bgPr><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
                          '<a:effectLst/></p:bgPr></p:bg>' % (NSDECL, PALET["latar"]))
    csld.insert(0, bg)


def rebuild_layouts(prs):
    master = prs.slide_masters[0]
    specs = layouts()
    existing = list(master.slide_layouts)
    for layout in existing[len(specs):]:
        master.slide_layouts.remove(layout)
    for layout, (name, shapes) in zip(master.slide_layouts, specs.items()):
        csld = layout._element.find("p:cSld", NS)
        csld.set("name", name)
        tree = csld.find("p:spTree", NS)
        for child in list(tree):
            if child.tag.endswith("}sp") or child.tag.endswith("}pic") or child.tag.endswith("}grpSp"):
                tree.remove(child)
        for xml in shapes:
            tree.append(etree.fromstring(xml))


def to_potx(src, dst):
    tmp = dst + ".tmp"
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(b"presentationml.presentation.main+xml", b"presentationml.template.main+xml")
            zout.writestr(item, data)
    shutil.move(tmp, dst)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(here, "..", "templates"))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(W), Emu(H)
    set_theme(prs)
    set_master_background(prs)
    rebuild_layouts(prs)

    pptx_path = os.path.join(args.out, "workshop-template.pptx")
    prs.save(pptx_path)
    to_potx(pptx_path, os.path.join(args.out, "workshop-template.potx"))
    print("Ditulis:", pptx_path, "dan workshop-template.potx")
    for layout in prs.slide_masters[0].slide_layouts:
        print(" -", layout.name, [p.placeholder_format.idx for p in layout.placeholders])


if __name__ == "__main__":
    main()
