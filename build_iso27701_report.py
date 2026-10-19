#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Documento Oficial en PDF:
ISO/IEC 27701:2025 - Tabla A.1: Controles para Responsables de PII (PII Controllers)
Análisis Completo de Implementación y Auditoría para la Universidad Nacional de San Agustín (UNSA)
1 Página exacta por cada control, diseño ejecutivo de alta fidelidad.
"""

import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT_DIR = "/Users/piero.o/Downloads/SEMESTRE II - SISTEMAS/AUDITORIA"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ISO_27701_Tabla_A1_UNSA_Analisis_Completo.pdf")

class PDFReport(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False) # Manejamos el flujo manualmente para garantizar 1 pág por control
        self.set_margins(left=16, top=20, right=16)
        
        # Cargar fuentes Unicode del sistema
        font_dir = '/System/Library/Fonts/Supplemental'
        self.add_font('ArialUni', '', os.path.join(font_dir, 'Arial.ttf'))
        self.add_font('ArialUni', 'B', os.path.join(font_dir, 'Arial Bold.ttf'))
        self.add_font('ArialUni', 'I', os.path.join(font_dir, 'Arial Italic.ttf'))
        self.add_font('ArialUni', 'BI', os.path.join(font_dir, 'Arial Bold Italic.ttf'))
        
        self.alias_nb_pages()

    def header(self):
        if self.page_no() > 1:
            self.set_y(8)
            self.set_font("ArialUni", "I", 7.5)
            self.set_text_color(110, 110, 110)
            self.cell(110, 5, "ISO/IEC 27701:2025 | Tabla A.1 — Análisis de Implementación y Auditoría UNSA", border=0, align="L")
            self.cell(68, 5, "Auditoría de Sistemas", border=0, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(197, 202, 233)
            self.set_line_width(0.3)
            self.line(16, 14, 194, 14)
            self.set_y(20)

    def footer(self):
        self.set_y(-12)
        self.set_font("ArialUni", "I", 7.5)
        self.set_text_color(120, 120, 120)
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.2)
        self.line(16, 285, 194, 285)
        self.cell(0, 6, f"Página {self.page_no()} de {{nb}}", border=0, align="C")

    # Helpers de diseño
    def chapter_header(self, code, title_en, title_es):
        self.set_font("ArialUni", "B", 13)
        self.set_text_color(26, 35, 126) # Azul marino
        self.cell(0, 6, f"Control {code} — {title_en}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("ArialUni", "BI", 9.5)
        self.set_text_color(57, 73, 171)
        self.cell(0, 4.5, f"« {title_es} »", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def norm_box(self, text):
        x = self.get_x()
        y = self.get_y()
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(26, 35, 126)
        
        # Calcular altura requerida
        self.set_xy(x + 2, y + 1.5)
        self.cell(174, 3.8, "TEXTO NORMATIVO ISO/IEC 27701:2025:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(x + 2)
        self.set_font("ArialUni", "I", 7.8)
        self.set_text_color(30, 30, 60)
        self.multi_cell(174, 3.6, f"\"{text}\"")
        end_y = self.get_y() + 1.5
        box_h = end_y - y
        
        self.set_draw_color(26, 35, 126)
        self.set_line_width(0.4)
        self.rect(x, y, 178, box_h, style="D")
        self.set_y(end_y + 1.5)

    def explain_section(self, text, analogia):
        self.set_fill_color(232, 240, 254)
        self.set_text_color(13, 71, 161)
        self.set_font("ArialUni", "B", 8.2)
        self.cell(178, 4.8, "  1. EXPLICACIÓN GENERAL DEL CONTROL (Concepto Universal)", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(30, 30, 30)
        self.write(3.8, "• ¿Qué significa en lenguaje sencillo?: ")
        self.set_font("ArialUni", "", 7.8)
        self.write(3.8, f"{text}\n")
        
        self.set_font("ArialUni", "BI", 7.8)
        self.set_text_color(1, 87, 155)
        self.write(3.8, "• Analogía de la vida real: ")
        self.set_font("ArialUni", "I", 7.8)
        self.write(3.8, f"{analogia}\n")
        self.ln(1)

    def applicability_section(self, aplica_txt, porque_txt):
        self.set_fill_color(255, 243, 224)
        self.set_text_color(230, 81, 0)
        self.set_font("ArialUni", "B", 8.2)
        self.cell(178, 4.8, "  2. ¿APLICA EN LA UNSA Y CUÁL ES SU ESTADO ACTUAL?", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(30, 30, 30)
        self.write(3.8, f"• Diagnóstico de Aplicabilidad: {aplica_txt}\n")
        self.set_font("ArialUni", "B", 7.8)
        self.write(3.8, "• Sustento técnico-legal: ")
        self.set_font("ArialUni", "", 7.8)
        self.write(3.8, f"{porque_txt}\n")
        self.ln(1)

    def section_univ(self, antecedentes, when, how, who, what, where):
        self.set_fill_color(232, 245, 233)
        self.set_text_color(46, 125, 50)
        self.set_font("ArialUni", "B", 8.2)
        self.cell(178, 4.8, "  3. PERSPECTIVA DE LA UNIVERSIDAD (UNSA) — IMPLEMENTACIÓN", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(46, 125, 50)
        self.write(3.8, "• Marco y Antecedentes Estatales: ")
        self.set_font("ArialUni", "I", 7.8)
        self.set_text_color(40, 40, 40)
        self.write(3.8, f"{antecedentes}\n")
        
        items_5w = [
            ("WHEN (Cuándo)", when),
            ("HOW (Cómo)", how),
            ("WHO (Quién)", who),
            ("WHAT (Qué entregables)", what),
            ("WHERE (Dónde se ubica)", where)
        ]
        for k, v in items_5w:
            self.set_font("ArialUni", "B", 7.8)
            self.set_text_color(46, 125, 50)
            self.write(3.8, f"• {k}: ")
            self.set_font("ArialUni", "", 7.8)
            self.set_text_color(30, 30, 30)
            self.write(3.8, f"{v}\n")
        self.ln(1)

    def section_audit(self, estado, riesgo, obs, recs):
        self.set_fill_color(255, 235, 238)
        self.set_text_color(198, 40, 40)
        self.set_font("ArialUni", "B", 8.2)
        self.cell(178, 4.8, f"  4. PERSPECTIVA DEL AUDITOR (Ing. Rafael) — ESTADO: {estado} | RIESGO: {riesgo}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(198, 40, 40)
        self.write(3.8, "• Observaciones de Auditoría: ")
        self.set_font("ArialUni", "", 7.8)
        self.set_text_color(30, 30, 30)
        self.write(3.8, f"{obs}\n")
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(198, 40, 40)
        self.write(3.8, "• Recomendaciones de Remediación: ")
        self.set_font("ArialUni", "", 7.8)
        self.set_text_color(30, 30, 30)
        self.write(3.8, f"{recs}\n")
        self.ln(1)

    def section_guiones(self, code, speech_univ, speech_audit):
        self.set_fill_color(243, 229, 245)
        self.set_text_color(123, 31, 162)
        self.set_font("ArialUni", "B", 8.2)
        self.cell(178, 4.8, f"  5. GUIONES DE EXPOSICIÓN ORAL — CONTROL {code}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(46, 125, 50)
        self.write(3.7, "• Guión Como Universidad (UNSA): ")
        self.set_font("ArialUni", "I", 7.8)
        self.set_text_color(45, 55, 65)
        self.write(3.7, f"\"{speech_univ}\"\n")
        
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(198, 40, 40)
        self.write(3.7, "• Guión Como Auditor (Ing. Rafael): ")
        self.set_font("ArialUni", "I", 7.8)
        self.set_text_color(45, 55, 65)
        self.write(3.7, f"\"{speech_audit}\"\n")

print("Generando reporte maestro perfectamente paginado...")
pdf = PDFReport()

# ==========================================
# PÁGINA 1: PORTADA
# ==========================================
pdf.add_page()
pdf.ln(20)
pdf.set_font("ArialUni", "B", 24)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 11, "ISO/IEC 27701:2025", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "B", 13)
pdf.set_text_color(57, 73, 171)
pdf.cell(0, 7, "TABLA A.1 — CONTROLES PARA RESPONSABLES DE PII (CONTROLLERS)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 7, "Conditions for Collection and Processing", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(4)
pdf.set_draw_color(26, 35, 126)
pdf.set_line_width(0.8)
pdf.line(45, pdf.get_y(), 165, pdf.get_y())
pdf.ln(8)

pdf.set_font("ArialUni", "B", 12)
pdf.set_text_color(33, 33, 33)
pdf.cell(0, 7, "INFORME INTEGRAL DE IMPLEMENTACIÓN Y AUDITORÍA", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "", 11)
pdf.set_text_color(66, 66, 66)
pdf.cell(0, 6.5, "Caso de Estudio: Universidad Nacional de San Agustín de Arequipa (UNSA)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(8)
pdf.set_fill_color(248, 249, 253)
pdf.set_draw_color(200, 205, 230)
pdf.rect(22, pdf.get_y(), 166, 52, style="FD")
pdf.set_xy(25, pdf.get_y() + 3.5)

pdf.set_font("ArialUni", "B", 9.5)
pdf.set_text_color(26, 35, 126)
pdf.cell(160, 5, "DATOS DE LA ASIGNATURA Y AUDITORÍA:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.set_font("ArialUni", "", 9)
pdf.set_text_color(40, 40, 40)
pdf.cell(160, 4.8, "• Institución Evaluada: Universidad Nacional de San Agustín de Arequipa (UNSA)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Alcance Normativo: Controles A.1.2.2 al A.1.2.9 (Condiciones de Recolección y Tratamiento)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Marco Jurídico Peruano: Ley N° 29733, D.S. 016-2024-JUS, Ley N° 27806, Ley 30220", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Rol del Auditor: Ing. Rafael (MSc. Ciberseguridad & Auditoría TI, Lead Auditor ISO)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Enfoque de Entrega: Doble Perspectiva (Gestión Universidad 5W + Auditoría) y Guiones Orales", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(25)
pdf.set_font("ArialUni", "I", 9.5)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, "Arequipa, Perú — Semestre Académico 2026", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ==========================================
# PÁGINA 2: METODOLOGÍA E ÍNDICE
# ==========================================
pdf.add_page()
pdf.set_font("ArialUni", "B", 14)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 7, "Marco Metodológico y Estructura del Informe", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

pdf.set_font("ArialUni", "", 8.8)
pdf.set_text_color(30, 30, 30)
intro_text = (
    "El presente informe aborda el estándar internacional ISO/IEC 27701:2025 (Sistema de Gestión de "
    "Privacidad de la Información - PIMS), enfocado en la Tabla A.1 ('Condiciones para la recolección "
    "y tratamiento de PII'). La norma internacional exige demostrar que todo tratamiento de información "
    "personal es lícito, fundado en bases legales válidas en el Perú (Ley N° 29733 y D.S. 016-2024-JUS) "
    "y orientado a propósitos legítimos y explícitos.\n\n"
    "Para garantizar un análisis riguroso y de utilidad práctica para el estudiante y el auditor, cada uno "
    "de los 8 controles (A.1.2.2 al A.1.2.9) se aborda en una página dedicada con 5 dimensiones clave:"
)
pdf.multi_cell(178, 4.5, intro_text)
pdf.ln(2)

metodologia = [
    ("1. Explicación General", "Concepto en palabras sencillas y analogía práctica de la vida real para entender el control antes de entrar a la universidad."),
    ("2. Análisis de Aplicabilidad", "Evaluación de si aplica a la UNSA, si ya se cumple formal o parcialmente, y las razones legales de su situación."),
    ("3. Perspectiva Universidad (UNSA)", "Plan de acción institucional con antecedentes, Portal de Transparencia del Estado y el modelo 5W (When, How, Who, What, Where)."),
    ("4. Perspectiva del Auditor", "Liderazgo técnico del Ing. Rafael (MSc. Auditoría, 10 años de experiencia): diagnóstico GAP, checklist de verificación y dictamen formal."),
    ("5. Guiones de Exposición Oral", "Scripts listos para lectura o ponencia en clase con tono conversacional: uno como Universidad y otro como Auditor.")
]

for tit, desc in metodologia:
    pdf.set_font("ArialUni", "B", 8.4)
    pdf.set_text_color(26, 35, 126)
    pdf.write(4.2, f"• {tit}: ")
    pdf.set_font("ArialUni", "", 8.4)
    pdf.set_text_color(40, 40, 40)
    pdf.write(4.2, f"{desc}\n")
    pdf.ln(0.5)

pdf.ln(3)
pdf.set_font("ArialUni", "B", 10)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 5.5, "Matriz de Controles Analizados (Tabla A.1 ISO/IEC 27701:2025):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

controls_summary = [
    ("A.1.2.2", "Identify and document purpose", "Identificar y documentar propósitos específicos", "Pág. 3"),
    ("A.1.2.3", "Identify lawful basis", "Identificar y demostrar la base legal del tratamiento", "Pág. 4"),
    ("A.1.2.4", "Determine when and how consent is obtained", "Determinar proceso formal para obtener consentimiento", "Pág. 5"),
    ("A.1.2.5", "Obtain and record consent", "Obtener y registrar evidencias verificables de consentimiento", "Pág. 6"),
    ("A.1.2.6", "Privacy impact assessment", "Evaluación de impacto en la privacidad (EIPD / PIA)", "Pág. 7"),
    ("A.1.2.7", "Contracts with PII processors", "Contratos y cláusulas con encargados (procesadores cloud/terceros)", "Pág. 8"),
    ("A.1.2.8", "Joint PII controller", "Acuerdos de co-responsabilidad con instituciones asociadas", "Pág. 9"),
    ("A.1.2.9", "Records related to processing PII", "Mantenimiento seguro de registros de privacidad de PII", "Pág. 10")
]

pdf.set_font("ArialUni", "B", 8)
pdf.set_fill_color(230, 235, 248)
pdf.set_text_color(26, 35, 126)
pdf.cell(18, 5.2, "Control", border=1, fill=True)
pdf.cell(74, 5.2, "Título en Inglés (Norma)", border=1, fill=True)
pdf.cell(70, 5.2, "Propósito del Control", border=1, fill=True)
pdf.cell(16, 5.2, "Ubicación", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "", 7.8)
pdf.set_text_color(30, 30, 30)
for c, en, es, pg in controls_summary:
    pdf.cell(18, 4.8, c, border=1)
    pdf.cell(74, 4.8, en, border=1)
    pdf.cell(70, 4.8, es, border=1)
    pdf.cell(16, 4.8, pg, border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# =========================================================================
# DATOS DETALLADOS DE CADA CONTROL (PÁGINAS 3 A 10)
# =========================================================================

controls_data = [
    {
        "code": "A.1.2.2",
        "title_en": "Identify and document purpose",
        "title_es": "Identificar y documentar el propósito del tratamiento",
        "norm_text": "The organization shall identify and document the specific purposes for which the PII will be processed.",
        "explain": "Antes de recopilar cualquier dato personal, la entidad debe saber con exactitud PARA QUÉ lo quiere y ponerlo formalmente por escrito. No se puede recolectar datos 'por si acaso' o para fines vagos como 'mejoras generales'.",
        "analogia": "Si vas a un hospital por una fractura, te piden tu nombre, DNI y radiografía (propósito asistencial). Si te piden tus estados de cuenta bancaria o qué auto conduces, no hay propósito justificado. Cada dato debe tener su porqué anotado.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA ya tiene inscritos bancos de datos ante la ANPD (Estudiantes, Biblioteca, Grados y Títulos, Seguridad, RRHH) y posee una política web. Sin embargo, no tiene un Registro de Actividades de Tratamiento (RAT) detallado proceso por proceso; los fines declarados son genéricos y no cubren todos los sistemas satélites.",
        "antecedentes": "Ley 29733 (Art. 5 Principio de Finalidad), D.S. 016-2024-JUS, Ley de Transparencia N° 27806, Ley Universitaria 30220 y Directivas internas de OTI.",
        "when": "De inmediato y continuo. Mapeo inicial en 90 días; revisiones semestrales alineadas a cada matrícula o lanzamiento de nuevos sistemas.",
        "how": "1. Levantar inventario de procesos universitarios con PII. 2. Diseñar plantilla RAT. 3. Mapear cada dato a su fin. 4. Aprobar vía Resolución Rectoral. 5. Publicar en Portal de Transparencia.",
        "who": "Lidera OTI con Asesoría Jurídica. Apoyan Decanos, Admisión, RRHH y Bienestar. Aprueba el Rector (RR). Supervisa OCI.",
        "what": "1. Documento maestro RAT. 2. Política de Privacidad actualizada. 3. Resolución Rectoral. 4. Fichas de finalidad en formularios.",
        "where": "Portal de Transparencia Estándar, web oficial (unsa.edu.pe), módulo SISUNSA y módulos de mesa de partes física.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "La universidad posee trámites ante la ANPD pero carece de un inventario maestro centralizado de finalidades. En facultades se solicitan datos en formularios web sin ficha informativa.",
        "rec_audit": "Emitir el RAT consolidado mediante Resolución Rectoral, publicar fichas informativas de finalidad en formularios de admisión y matrícula, y capacitar a jefes de departamento.",
        "speech_univ": "Compañeros y profesor: Para implementar el A.1.2.2, la UNSA debe documentar para qué usa cada dato de sus 25,000 miembros. Ya tenemos bancos en el MINJUSDH, pero con fines muy vagos. Proponemos crear el RAT institucional, aprobarlo por Resolución Rectoral y publicar avisos claros en el Portal de Transparencia y en cada matrícula.",
        "speech_audit": "Como auditor líder, califico este control como PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO). La UNSA tiene avances ante la ANPD pero falla en granularidad técnica: admisión y bienestar piden datos sin exhibir la finalidad al titular. Recomiendo aprobar el RAT en 60 días bajo apercibimiento de observación formal."
    },
    {
        "code": "A.1.2.3",
        "title_en": "Identify lawful basis",
        "title_es": "Identificar y demostrar la base legal del tratamiento",
        "norm_text": "The organization shall determine, document and be able to demonstrate compliance with the relevant lawful basis for the processing of PII for the identified purposes.",
        "explain": "No basta tener un motivo (A.1.2.2); debes demostrar QUÉ NORMA LEGAL te faculta jurídicamente para usar esos datos: si actúas por mandato de ley, contrato, función pública o consentimiento del titular.",
        "analogia": "Un policía no puede revisar tu mochila solo porque 'quiere verificar seguridad'; necesita una orden judicial, flagrancia o ley expresa. Si no tiene ese respaldo normativo, su acto es nulo.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO (Formalmente).",
        "porque_txt": "Al ser universidad pública, la UNSA goza de la excepción del Art. 14 inc. 1 de la Ley 29733 (funciones públicas de la Ley 30220). Esa base legal EXISTE en la ley, pero la UNSA no la tiene formalizada ni documentada en una Matriz de Bases Legales ni en sus contratos de matrícula.",
        "antecedentes": "Ley 29733 (Art. 13 y 14), D.S. 016-2024-JUS, Ley Universitaria 30220 (Art. 98-102), TUO Ley 27444 y resoluciones vinculantes de la ANPD.",
        "when": "Fase de diseño del PIMS (primeros 60 días). Actualización obligatoria ante reformas legales del Congreso, MINJUSDH o SUNEDU.",
        "how": "1. Elaborar Matriz de Bases Legales asociando cada proceso del RAT a su artículo normativo. 2. Diferenciar función pública de consentimiento forzoso. 3. Emitir Directiva Legal Rectoral.",
        "who": "Oficina de Asesoría Jurídica de la UNSA como líder sustantivo, en coordinación con OTI y Secretaría General. Valida el Auditor.",
        "what": "1. Matriz Institucional de Bases Legales. 2. Informe Técnico Legal vinculante. 3. Cláusulas de base legal insertadas en reglamentos académicos.",
        "where": "Oficina de Asesoría Jurídica, anexos del Reglamento General de la UNSA, y publicado en el Portal de Transparencia Estándar.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "Existe la creencia errónea en las dependencias de que 'por ser universidad estatal podemos pedir cualquier dato'. No existe un documento formal que mapee los artículos legales habilitantes.",
        "rec_audit": "Aprobar la Matriz de Bases Legales por Consejo Universitario y capacitar a asesoría jurídica y personal de sistemas para fundamentar cada recolección de datos.",
        "speech_univ": "Para el control A.1.2.3, la universidad tiene que respaldar jurídicamente todo lo que hace. En Perú, el Art. 14.1 de la Ley 29733 nos permite tratar datos académicos sin consentimiento por función pública. Pero debemos DOCUMENTARLO: si la UNSA comparte notas de un alumno mayor de edad con sus padres, cometería una infracción si no tiene consentimiento.",
        "speech_audit": "Dictamino este control como NO IMPLEMENTADO (Riesgo ALTO). La UNSA asume tácitamente que la Ley Universitaria lo cubre todo, pero carece de trazabilidad documental. Si la ANPD inspecciona, la universidad no tiene cómo probar qué base jurídica legitima datos de salud o biometría. Se exigen 45 días para la Matriz."
    },
    {
        "code": "A.1.2.4",
        "title_en": "Determine when and how consent is to be obtained",
        "title_es": "Determinar cuándo y cómo se debe obtener el consentimiento",
        "norm_text": "The organization shall determine and document a process by which it can demonstrate if, when and how consent for the processing of PII was obtained from PII principals.",
        "explain": "Para los tratamientos donde la ley te exige autorización, debes tener un PROCEDIMIENTO formal: en qué momento exacto se pide, qué palabras se usan, qué casillas se marcan y cómo se demuestra que aceptaron libremente.",
        "analogia": "Cuando firmas un consentimiento antes de donar sangre o una cirugía, la clínica tiene un protocolo estricto: te explican los riesgos, firmas un documento específico y te dan copia. No dan por sentado tu sí.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "Aplica para tratamientos que exceden las atribuciones de la Ley 30220: fotos en redes sociales de la UNSA, convenios internacionales con terceros, y tratamientos de datos sensibles en el comedor y tópico de bienestar universitario.",
        "antecedentes": "Ley 29733 (Art. 13 - Consentimiento libre, previo, expreso, informado e inequívoco), D.S. 016-2024-JUS (prohibición de casillas premarcadas).",
        "when": "Previo al inicio de cada ciclo académico y de forma permanente en cada formulario donde se recaben autorizaciones.",
        "how": "1. Mapear casos de consentimiento obligatorio. 2. Diseñar flujogramas de captura. 3. Redactar textos claros sin letra chica. 4. Prohibir casillas premarcadas. 5. Definir mecanismos de revocación.",
        "who": "OTI (arquitectura de software) + Asesoría Jurídica (cláusulas) + Dirección de Bienestar y Comunicación Social.",
        "what": "1. Procedimiento Operativo Estándar (POE) de Consentimiento. 2. Plantillas normalizadas de consentimiento informado. 3. Mecanismo de revocatoria.",
        "where": "Sistemas informáticos académicos (SISUNSA, Portal del Postulante), módulos de tópico médico y portal web.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "En eventos académicos y ferias se capturan datos de estudiantes mediante formularios de Google Forms sin texto de consentimiento informado ni opciones de opt-in.",
        "rec_audit": "Estandarizar todas las interfaces web con mecanismos de consentimiento explícito e incorporar procedimiento de revocatoria en el portal institucional.",
        "speech_univ": "El control A.1.2.4 nos exige definir las reglas del juego para pedir consentimiento. Cuando un estudiante se atiende en el tópico médico o la UNSA usa fotos para publicidad, debemos pedir permiso previo, libre e informado, con casillas desmarcadas y formularios claros. Además, el alumno debe poder revocar su autorización fácilmente.",
        "speech_audit": "Constato informalidad respecto a este control: NO IMPLEMENTADO (Riesgo ALTO). Se recopilan datos en diplomados y ferias mediante formularios sin cláusulas de consentimiento. Esto constituye No Conformidad Mayor bajo ISO 27701. Ordeno suspender formularios no homologados hasta estandarizar el flujo conforme al D.S. 016-2024-JUS."
    },
    {
        "code": "A.1.2.5",
        "title_en": "Obtain and record consent",
        "title_es": "Obtener y registrar el consentimiento otorgado",
        "norm_text": "The organization shall obtain and record consent from PII principals according to the documented processes.",
        "explain": "Si el control anterior era 'diseñar el método', este control es EJECUTARLO y GUARDAR LA EVIDENCIA. Debes conservar registros inalterables que prueben quién aceptó, a qué hora, qué versión leyó y qué IP o firma usó.",
        "analogia": "No basta tener un contrato de alquiler redactado; tienes que tenerlo firmado por el inquilino y archivado bajo llave para cuando necesites probarlo ante un juez.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "Aplica para todos los sistemas de la UNSA donde se capture consentimiento. Si un estudiante denuncia ante la ANPD que no autorizó el uso de su imagen o historial médico, la UNSA debe presentar el log digital o el papel firmado.",
        "antecedentes": "Ley 29733 (Principio de Responsabilidad Proactiva / Accountability), D.S. 016-2024-JUS y directivas de seguridad digital de OTI.",
        "when": "En tiempo real al momento de la interacción del usuario y custodia durante al menos 5 años posteriores a la desvinculación.",
        "how": "1. Implementar tabla 'Consent_Logs' (ID usuario, versión, timestamp, IP, hash). 2. Archivar consentimientos médicos escaneados. 3. Registrar bajas por revocatoria.",
        "who": "Administradores de bases de datos y seguridad TI (OTI), personal de ventanilla de archivo, Oficial de Protección de Datos.",
        "what": "1. Base de datos centralizada de trazas y consentimientos digitales. 2. Repositorio de consentimientos físicos foliados. 3. Reporte de auditoría de revocatorias.",
        "where": "Servidores de base de datos institucionales con respaldos encriptados; archivo físico en Secretaría General y Bienestar.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "La universidad no dispone de tablas de auditoría de consentimientos en sus bases de datos. Los consentimientos en papel de bienestar se encuentran dispersos sin indexación.",
        "rec_audit": "Desarrollar un servicio centralizado de registro de consentimientos (API interna) y digitalizar de inmediato los expedientes físicos existentes.",
        "speech_univ": "Para el control A.1.2.5, la universidad tiene que guardar la prueba irrefutable de que el estudiante aceptó. Guardamos en el servidor fecha, hora, dirección IP y el texto exacto aceptado. Si fue en papel en el tópico médico, se archiva y escanea. Así, ante cualquier fiscalización, la UNSA demuestra pleno respeto a los derechos del titular.",
        "speech_audit": "Declaro el estado de NO IMPLEMENTADO con riesgo ALTO. Al auditar una muestra de 10 alumnos al azar, el sistema no arrojó registros de auditoría con marca de tiempo ni trazabilidad de consentimiento. Esto deja a la UNSA en completa indefensión ante denuncias sancionables de la ANPD. Se exige log inmutable en 30 días."
    },
    {
        "code": "A.1.2.6",
        "title_en": "Privacy impact assessment",
        "title_es": "Evaluación de impacto en la privacidad (EIPD / PIA)",
        "norm_text": "The organization shall assess the need for, and implement where appropriate, a privacy impact assessment whenever new processing of PII or changes to existing processing of PII is planned.",
        "explain": "Antes de crear un sistema nuevo o hacer un cambio tecnológico que use datos personales, debes hacer un 'estudio de riesgos de privacidad' para saber si vulneras derechos y cómo evitar filtraciones o abusos.",
        "analogia": "Es como el Estudio de Impacto Ambiental previo a construir una carretera: primero calculas el daño potencial al entorno y diseñas medidas mitigadoras antes de colocar la primera piedra.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "Aplica con carácter de urgencia. La UNSA cuenta con proyectos de cámaras con reconocimiento biométrico, sistemas de asistencia docente y plataformas cloud. Todo proyecto tecnológico universitario con datos sensibles requiere EIPD.",
        "antecedentes": "Guías de la ANPD sobre Evaluación de Impacto en Protección de Datos Personales, Directivas de Seguridad Digital de la PCM e ISO 31000.",
        "when": "Fase de análisis y diseño de cualquier proyecto de software o infraestructura de TI, ANTES de la compra de equipos o pase a producción.",
        "how": "1. Definir umbrales de obligatoriedad (biometría, salud, IA, cámaras). 2. Describir flujos de datos. 3. Evaluar necesidad/proporcionalidad. 4. Analizar riesgos y definir medidas.",
        "who": "Equipo de Desarrollo de Software / OTI junto con Oficial de Datos (DPO) y Asesoría Jurídica. Aprueba Comité de Gobierno Digital.",
        "what": "1. Metodología Institucional de EIPD / PIA. 2. Informes de EIPD firmados por proyecto. 3. Matriz de riesgos de privacidad actualizada.",
        "where": "Oficina de Tecnologías de la Información, Comité de Gobierno Digital y carpeta técnica de cada proyecto de inversión en TI.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "La UNSA adquirió e instaló cámaras de videovigilancia y sistemas de control biométrico sin haber elaborado un análisis previo de impacto a la privacidad de los estudiantes y docentes.",
        "rec_audit": "Aprobar la directiva de EIPD obligatoria y ejecutar evaluaciones de impacto retroactivas para los sistemas de biometría y videovigilancia actualmente activos.",
        "speech_univ": "El control A.1.2.6 es el 'estudio de impacto ambiental' de los datos personales. En la UNSA solemos comprar servidores o cámaras pensando solo en la parte técnica. Con este control, antes de lanzar un nuevo sistema como el reconocimiento facial o inteligencia artificial, debemos evaluar si hay peligro de filtración y mitigar los riesgos.",
        "speech_audit": "Punto crítico calificado como NO IMPLEMENTADO (Riesgo ALTO). Implementar biometría y videovigilancia sin una EIPD previa vulnera las directrices de la ANPD e ISO 27701. Mi dictamen exige formalizar de inmediato la metodología de EIPD e incorporarla como requisito insubsanable en las bases de licitación de TI."
    },
    {
        "code": "A.1.2.7",
        "title_en": "Contracts with PII processors",
        "title_es": "Contratos con encargados del tratamiento de PII (Processors)",
        "norm_text": "The organization shall have a written contract with any PII processor that it uses, and shall ensure that their contracts with PII processors address the implementation of the appropriate controls in Annex A (see Table A.2).",
        "explain": "Si contratas a una empresa externa para procesar datos por ti (Google para correo, hosting, soporte de ERP o seguridad física), debes firmar un contrato que les exija proteger los datos y no usarlos para fines propios.",
        "analogia": "Si le das las llaves de tu casa a una empresa de limpieza, firmas un contrato donde dice que solo limpian de 9 a 12, que no revisan cajones y que responden si rompen algo. No les das acceso sin límites.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA usa Google Workspace, Microsoft 365, plataformas cloud y empresas de vigilancia. Aunque existen contratos OSCE estándar, la mayoría NO incluye los Anexos de Protección de Datos (DPA) exigidos por la ISO 27701.",
        "antecedentes": "Ley 29733 (Art. 16 - Encargo del Tratamiento), D.S. 016-2024-JUS, Ley de Contrataciones del Estado (OSCE) y cláusulas tipo internacionales.",
        "when": "En bases de licitación, contratación y renegociación contractual de cualquier proveedor que acceda a bases de datos.",
        "how": "1. Identificar proveedores encargados. 2. Diseñar Adenda Estándar de Protección de Datos. 3. Incluir penalidades por brechas. 4. Exigir auditorías al proveedor. 5. Homologar DPAs.",
        "who": "Oficina de Abastecimiento y Logística, Asesoría Jurídica y OTI. Aprueba la Dirección General de Administración (DGA).",
        "what": "1. Cláusula tipo obligatoria de protección de datos en TDRs. 2. Adendas de privacidad suscritas con proveedores. 3. Matriz de encargados.",
        "where": "Expedientes de contratación en Logística, SEACE y archivo de Asesoría Jurídica.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO-ALTO",
        "obs_audit": "Los contratos con proveedores locales de mantenimiento de software y servicios de seguridad física no contienen ninguna cláusula de confidencialidad o tratamiento conforme a Ley 29733.",
        "rec_audit": "Elaborar de inmediato un anexo contractual de protección de datos y remitirlo a todos los proveedores tecnológicos y de servicios de la universidad para firma obligatoria.",
        "speech_univ": "Para el control A.1.2.7, nos enfocamos en los proveedores externos de la UNSA: Google, Microsoft, proveedores de ERP y empresas de vigilancia. La norma nos exige contratos escritos donde se estipule que los datos pertenecen a la UNSA, que no pueden revenderlos y que deben aplicar medidas de seguridad estrictas.",
        "speech_audit": "La UNSA tiene contratos aprobados bajo la Ley OSCE pero vacíos en materia de privacidad: PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO-ALTO). Si un proveedor sufre un hackeo, la UNSA es responsable solidaria por negligencia contractual. Exijo incorporar cláusulas DPA en todos los contratos vigentes en 60 días."
    },
    {
        "code": "A.1.2.8",
        "title_en": "Joint PII controller",
        "title_es": "Responsable conjunto de PII (Co-responsabilidad)",
        "norm_text": "The organization shall determine respective roles and responsibilities for the processing of PII (including PII protection and security requirements) with any joint PII controller.",
        "explain": "Cuando dos instituciones deciden JUNTAS qué hacer con una base de datos (por ejemplo, dos universidades en investigación compartida o doble titulación), deben firmar un acuerdo donde se defina quién responde por qué.",
        "analogia": "Si dos socios abren un negocio y usan la misma lista de clientes, deben firmar un pacto donde diga quién cuida el archivo, quién atiende reclamos y cómo se reparten las culpas si hay una filtración. Nadie puede desentenderse.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "La UNSA mantiene convenios de doble titulación con universidades extranjeras, proyectos de investigación con CONCYTEC/ProCiencia, consorcios (UNSA-UNI-San Marcos) e intercambios donde ambas partes deciden fines y medios.",
        "antecedentes": "Convenios marco y específicos de cooperación académica, Ley 29733 (corresponsabilidad solidaria) y convenios con MINEDU y SUNEDU.",
        "when": "En la negociación y firma de cualquier convenio interinstitucional o consorcio de investigación científica.",
        "how": "1. Mapear convenios activos con transferencia o co-gestión de datos. 2. Diseñar Anexo de Co-Responsabilidad. 3. Asignar quién atiende derechos ARCO. 4. Fijar canal de incidentes.",
        "who": "Oficina de Relaciones Internacionales y Cooperación (ORIC), Vicerrectorado de Investigación (VRI), Asesoría Jurídica y DPO.",
        "what": "1. Protocolo de Co-Responsabilidad para Convenios. 2. Cláusulas bilaterales de privacidad en convenios. 3. Matriz de corresponsabilidades.",
        "where": "Oficina de Relaciones Internacionales, convenios en Secretaría General y portal de transparencia de convenios.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "Los convenios interuniversitarios de investigación y movilidad no delimitan quién es responsable ante una pérdida de datos personales ni quién asume la respuesta a solicitudes ARCO de los beneficiarios.",
        "rec_audit": "Crear una adenda modelo de co-responsabilidad y aplicarla a todos los convenios con intercambio de bases de datos de estudiantes o investigadores.",
        "speech_univ": "El control A.1.2.8 aplica cuando la UNSA trabaja en equipo con otras universidades: doble titulación o proyectos médicos con CONCYTEC. Ambas partes son 'responsables conjuntos'. Este control nos exige firmar un anexo donde se defina quién custodia los datos, quién atiende reclamos y qué hacer si ocurre un incidente de seguridad.",
        "speech_audit": "Constato convenios de cooperación activos sin cláusulas de roles de privacidad: NO IMPLEMENTADO (Riesgo MEDIO). Si los datos de nuestros becarios en el extranjero se filtran, se genera un conflicto de responsabilidades. Recomiendo que ningún convenio con bases de datos sea suscrito sin la visa previa del Oficial de Datos."
    },
    {
        "code": "A.1.2.9",
        "title_en": "Records related to processing PII",
        "title_es": "Registros relacionados con el tratamiento de PII (Custodia y Evidencia)",
        "norm_text": "The organization shall determine and securely maintain the necessary records in support of its obligations for the processing of PII.",
        "explain": "Este control es el archivo y biblioteca de la privacidad: debes guardar, organizar y proteger con máxima seguridad todos los documentos generados por los controles anteriores (el RAT, consentimientos, contratos, evaluaciones de impacto y reclamos ARCO).",
        "analogia": "Es como el archivo contable de una empresa: guardas cada factura, boleta, libro mayor y balance bajo llave y en digital. Si viene la SUNAT a auditarte de sorpresa, tienes todas las carpetas listas para exhibir.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA genera resoluciones rectorales, actas y contratos en su sistema de trámite documentario. Sin embargo, no tiene un sistema centralizado de registros de privacidad de PII; la información está fragmentada y no cuenta con políticas de retención y destrucción segura.",
        "antecedentes": "Ley 29733 (Principio de Seguridad y Calidad), D.S. 016-2024-JUS (conservación y trazabilidad) y Ley del Sistema Nacional de Archivos.",
        "when": "De forma continua. Almacenamiento activo durante el ciclo de vida del dato más el periodo legal de retención (mínimo 5 años para fiscalización de la ANPD).",
        "how": "1. Crear Repositorio Seguro de Privacidad. 2. Aplicar controles de acceso por roles (RBAC). 3. Cifrar registros digitales. 4. Redactar Política de Retención y Disposición. 5. Auditorías semestrales.",
        "who": "Oficial de Protección de Datos (DPO) con Archivo Central de la UNSA, OTI (seguridad digital) y OCI.",
        "what": "1. Catálogo Maestro de Registros de PII. 2. Repositorio Digital Cifrado con control de versiones. 3. Política de Retención y Destrucción Segura. 4. Bitácora de incidentes.",
        "where": "Servidores de almacenamiento seguro de OTI con cifrado en reposo; Archivo Central de la UNSA con control de incendios y accesos.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "Los documentos de privacidad están dispersos: resoluciones en Secretaría General, contratos en Logística y formularios en Bienestar. No existe un índice maestro ni medidas de seguridad específicas.",
        "rec_audit": "Implementar un módulo digital centralizado de gestión documental de privacidad PIMS y formalizar la política de retención y expurgo seguro aprobada por Consejo Universitario.",
        "speech_univ": "Llegamos al control A.1.2.9, que es el 'paraguas' de todo el sistema. Si no guardamos registros ordenados y seguros, lo anterior no se puede demostrar. La UNSA debe crear un Repositorio Central de Privacidad donde estén organizados el RAT, las bases legales, las EIPD y los contratos, respaldados y cifrados para cualquier auditoría.",
        "speech_audit": "Cierro mi dictamen con el A.1.2.9: PARCIALMENTE IMPLEMENTADO (Riesgo ALTO). En auditoría ISO, 'lo que no está documentado y accesible, no existe'. La documentación de la UNSA está atomizada sin política de retención ni garantías de confidencialidad. Exijo consolidar el Repositorio de Registros de Privacidad en un plazo de 90 días."
    }
]

# =========================================================================
# GENERACIÓN DE PÁGINAS 3 A 10 (UNA PÁGINA EXACTA POR CONTROL)
# =========================================================================

for c in controls_data:
    pdf.add_page()
    print(f"Generando página para: {c['code']} - {c['title_en']}...")
    
    # 1. Cabecera y Caja Normativa
    pdf.chapter_header(c['code'], c['title_en'], c['title_es'])
    pdf.norm_box(c['norm_text'])
    
    # 2. Explicación general
    pdf.explain_section(c['explain'], c['analogia'])
    
    # 3. Aplicabilidad UNSA
    pdf.applicability_section(c['aplica_txt'], c['porque_txt'])
    
    # 4. Perspectiva Universidad
    pdf.section_univ(c['antecedentes'], c['when'], c['how'], c['who'], c['what'], c['where'])
    
    # 5. Perspectiva Auditor
    pdf.section_audit(c['estado_audit'], c['riesgo_audit'], c['obs_audit'], c['rec_audit'])
    
    # 6. Guiones
    pdf.section_guiones(c['code'], c['speech_univ'], c['speech_audit'])

# ==========================================
# PÁGINA 11: CONCLUSIONES Y DICTAMEN GLOBAL
# ==========================================
pdf.add_page()
pdf.set_font("ArialUni", "B", 14)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 7, "Dictamen Global de Auditoría y Hoja de Ruta de Implementación", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

pdf.set_font("ArialUni", "", 8.8)
pdf.set_text_color(30, 30, 30)
resumen_global = (
    "Tras la evaluación técnica de los 8 controles de la Tabla A.1 de la norma ISO/IEC 27701:2025 aplicada "
    "a la Universidad Nacional de San Agustín (UNSA), el auditor líder Ing. Rafael emite el siguiente dictamen "
    "consolidado. La universidad evidencia cumplimiento normativo sectorial incipiente (inscripción de bancos "
    "ante la ANPD), pero carece de un Sistema de Gestión de Privacidad de la Información (PIMS) estructurado "
    "y documentado conforme al estándar internacional."
)
pdf.multi_cell(178, 4.5, resumen_global)
pdf.ln(2.5)

# Tabla resumen
pdf.set_font("ArialUni", "B", 8)
pdf.set_fill_color(26, 35, 126)
pdf.set_text_color(255, 255, 255)
pdf.cell(18, 5.5, "Control", border=1, fill=True)
pdf.cell(66, 5.5, "Nombre del Control (ISO 27701)", border=1, fill=True)
pdf.cell(50, 5.5, "Estado de Madurez", border=1, fill=True)
pdf.cell(24, 5.5, "Nivel Riesgo", border=1, fill=True)
pdf.cell(20, 5.5, "Prioridad", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

summary_rows = [
    ("A.1.2.2", "Identify and document purpose", "Parcialmente Implementado", "MEDIO", "Alta (P1)"),
    ("A.1.2.3", "Identify lawful basis", "No Implementado", "ALTO", "Alta (P1)"),
    ("A.1.2.4", "Determine when/how consent obtained", "No Implementado", "ALTO", "Media (P2)"),
    ("A.1.2.5", "Obtain and record consent", "No Implementado", "ALTO", "Media (P2)"),
    ("A.1.2.6", "Privacy impact assessment", "No Implementado", "ALTO", "Alta (P1)"),
    ("A.1.2.7", "Contracts with PII processors", "Parcialmente Implementado", "MEDIO-ALTO", "Media (P2)"),
    ("A.1.2.8", "Joint PII controller", "No Implementado", "MEDIO", "Baja (P3)"),
    ("A.1.2.9", "Records related to processing", "Parcialmente Implementado", "ALTO", "Alta (P1)")
]

pdf.set_font("ArialUni", "", 7.8)
for c_code, c_name, c_est, c_risk, c_prio in summary_rows:
    pdf.set_text_color(30, 30, 30)
    pdf.cell(18, 4.8, c_code, border=1)
    pdf.cell(66, 4.8, c_name, border=1)
    
    # Colores
    if "No" in c_est:
        pdf.set_text_color(180, 0, 0)
    else:
        pdf.set_text_color(180, 100, 0)
    pdf.cell(50, 4.8, c_est, border=1)
    
    if "ALTO" in c_risk:
        pdf.set_text_color(180, 0, 0)
    else:
        pdf.set_text_color(100, 100, 0)
    pdf.cell(24, 4.8, c_risk, border=1)
    
    pdf.set_text_color(30, 30, 30)
    pdf.cell(20, 4.8, c_prio, border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(3)

# Hoja de ruta
pdf.set_font("ArialUni", "B", 10)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 5, "Hoja de Ruta Recomendada de Implementación (12 Meses):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

roadmap_points = [
    ("Fase 1 (Meses 1 a 3): Fundación Documental", "Formalización del RAT (A.1.2.2) y Matriz de Bases Legales (A.1.2.3) vía Resolución Rectoral; actualización de avisos en el Portal de Transparencia."),
    ("Fase 2 (Meses 4 a 6): Gobernanza de Terceros y Riesgo", "Incorporación de adendas DPA a contratos con proveedores clave (A.1.2.7), metodología de EIPD para proyectos nuevos (A.1.2.6) y acuerdos de convenios (A.1.2.8)."),
    ("Fase 3 (Meses 7 a 9): Soluciones Tecnológicas y Consentimiento", "Implementación de base de datos de logs de consentimiento (A.1.2.4 y A.1.2.5) y repositorio cifrado de registros (A.1.2.9)."),
    ("Fase 4 (Meses 10 a 12): Auditoría de Certificación y Cultura", "Capacitación masiva a facultades y dependencias administrativas, simulacro de fiscalización ANPD y auditoría interna ISO 19011.")
]

for tit, desc in roadmap_points:
    pdf.set_font("ArialUni", "B", 8.2)
    pdf.set_text_color(46, 125, 50)
    pdf.write(4, f"• {tit}: ")
    pdf.set_font("ArialUni", "", 8)
    pdf.set_text_color(40, 40, 40)
    pdf.write(4, f"{desc}\n")
    pdf.ln(0.5)

pdf.ln(2.5)
pdf.set_fill_color(232, 234, 246)
pdf.set_draw_color(26, 35, 126)
pdf.rect(16, pdf.get_y(), 178, 15, style="FD")
pdf.set_xy(19, pdf.get_y() + 2)
pdf.set_font("ArialUni", "B", 8.5)
pdf.set_text_color(26, 35, 126)
pdf.cell(172, 4.2, "FIRMA Y RESPONSABILIDAD TÉCNICA DEL AUDITOR LÍDER:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(19)
pdf.set_font("ArialUni", "I", 8.2)
pdf.set_text_color(50, 50, 50)
pdf.cell(172, 4.2, "Ing. Rafael — Especialista en Ciberseguridad y Auditoría TI (MSc.) | Lead Auditor ISO/IEC 27001 & 27701", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Guardar PDF
print(f"Guardando PDF en: {OUTPUT_FILE}...")
pdf.output(OUTPUT_FILE)
print(f"¡PDF generado con éxito! Tamaño: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB, Páginas totales: {pdf.page_no()}")

