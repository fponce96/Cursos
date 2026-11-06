#!/usr/bin/env python3
"""Genera tres PDFs de INSYCOM desde el Markdown del curso (sin dependencias de oficina)."""
from pathlib import Path
from xml.sax.saxutils import escape
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "INSYCOM-Curso-Instaladores.md"
OUT = ROOT / "pdf"
OUT.mkdir(exist_ok=True)
BLUE = colors.HexColor("#12365C")
CYAN = colors.HexColor("#00A6C8")
GRAY = colors.HexColor("#445466")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="BrandTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=24, leading=29, textColor=BLUE, alignment=TA_CENTER, spaceAfter=15))
styles.add(ParagraphStyle(name="Sub", parent=styles["Normal"], fontSize=12, leading=17, alignment=TA_CENTER, textColor=GRAY, spaceAfter=12))
styles.add(ParagraphStyle(name="SectionI", parent=styles["Heading1"], fontSize=15, leading=20, textColor=BLUE, spaceBefore=16, spaceAfter=9))
styles.add(ParagraphStyle(name="SectionII", parent=styles["Heading2"], fontSize=11, leading=15, textColor=BLUE, spaceBefore=11, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyI", parent=styles["BodyText"], fontSize=9.3, leading=14, spaceAfter=7))
styles.add(ParagraphStyle(name="BulletI", parent=styles["BodyI"], leftIndent=13, firstLineIndent=-9))

def rich(s):
    s = escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s

def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(CYAN)
    canvas.setLineWidth(1.2)
    canvas.line(42, h-43, w-42, h-43)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(BLUE)
    canvas.drawString(43, h-35, "INSYCOM  |  CAPACITACIÓN TÉCNICA")
    canvas.setStrokeColor(colors.HexColor("#D7E0E8"))
    canvas.line(42, 43, w-42, 43)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(43, 30, "Instructor: Facundo Ponce  •  El reclamo no empieza con el cliente")
    canvas.drawRightString(w-43, 30, str(doc.page))
    canvas.restoreState()

def generate(filename, title, lines):
    path = OUT / filename
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=48, rightMargin=48, topMargin=65, bottomMargin=59, title=title, author="Facundo Ponce | INSYCOM")
    story = [Spacer(1, 20), Paragraph("INSYCOM", styles["BrandTitle"]), Paragraph(rich(title), styles["Sub"]), Paragraph("Instructor: <b>Facundo Ponce</b>", styles["Sub"]), Paragraph("<i>El reclamo no empieza con el cliente</i>", styles["Sub"]), Spacer(1, 25)]
    for line in lines:
        s=line.strip()
        if not s: continue
        if s.startswith("### "): story.append(Paragraph(rich(s[4:]), styles["SectionII"]))
        elif s.startswith("## "): story.append(Paragraph(rich(s[3:]), styles["SectionI"]))
        elif s.startswith("- "): story.append(Paragraph("• " + rich(s[2:]), styles["BulletI"]))
        else: story.append(Paragraph(rich(s), styles["BodyI"]))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(path)

text=SOURCE.read_text(encoding="utf-8")
parts=re.split(r"(?m)^## (0[123] — .+)$", text)
if len(parts) != 7:
    raise ValueError("No se detectaron las tres secciones esperadas del curso")
generate("01_Guion_Instructor_INSYCOM.pdf", "Guion docente integral | Instalaciones ISP", (ROOT / "Guion-Docente-Integral-INSYCOM.md").read_text(encoding="utf-8").splitlines())
generate("02_Manual_Tecnico_INSYCOM.pdf", "Manual técnico del participante", parts[4].splitlines())
generate("03_Actividades_FAQ_Checklist_INSYCOM.pdf", "Actividades, checklist y preguntas frecuentes", parts[6].splitlines())
