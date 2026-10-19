#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Documento Oficial en PDF:
ISO/IEC 27701:2025 - Tabla A.1: Sección 'Obligations to PII Principals' (Controles A.1.3.2 al A.1.3.11)
Análisis Completo de Implementación y Auditoría para la Universidad Nacional de San Agustín (UNSA)
1 Página exacta por cada control, diseño ejecutivo de alta fidelidad.
"""

import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT_DIR = "/Users/piero.o/Downloads/SEMESTRE II - SISTEMAS/AUDITORIA"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ISO_27701_Seccion_A1.3_Obligaciones_Titulares_UNSA.pdf")

class PDFReport(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False)
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
            self.cell(115, 5, "ISO/IEC 27701:2025 | Sección A.1.3 — Obligaciones hacia Titulares (UNSA)", border=0, align="L")
            self.cell(63, 5, "Auditoría de Sistemas", border=0, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
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
        self.set_font("ArialUni", "B", 12.5)
        self.set_text_color(26, 35, 126) # Azul marino
        self.cell(0, 5.8, f"Control {code} — {title_en}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("ArialUni", "BI", 9.2)
        self.set_text_color(57, 73, 171)
        self.cell(0, 4.2, f"« {title_es} »", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.8)

    def norm_box(self, text):
        x = self.get_x()
        y = self.get_y()
        self.set_font("ArialUni", "B", 7.8)
        self.set_text_color(26, 35, 126)
        
        self.set_xy(x + 2, y + 1.2)
        self.cell(174, 3.6, "TEXTO NORMATIVO ISO/IEC 27701:2025:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(x + 2)
        self.set_font("ArialUni", "I", 7.6)
        self.set_text_color(30, 30, 60)
        self.multi_cell(174, 3.5, f"\"{text}\"")
        end_y = self.get_y() + 1.2
        box_h = end_y - y
        
        self.set_draw_color(26, 35, 126)
        self.set_line_width(0.4)
        self.rect(x, y, 178, box_h, style="D")
        self.set_y(end_y + 1.2)

    def explain_section(self, text, analogia):
        self.set_fill_color(232, 240, 254)
        self.set_text_color(13, 71, 161)
        self.set_font("ArialUni", "B", 8)
        self.cell(178, 4.5, "  1. EXPLICACIÓN GENERAL DEL CONTROL (Concepto Universal)", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(30, 30, 30)
        self.write(3.7, "• ¿Qué significa en lenguaje sencillo?: ")
        self.set_font("ArialUni", "", 7.6)
        self.write(3.7, f"{text}\n")
        
        self.set_font("ArialUni", "BI", 7.6)
        self.set_text_color(1, 87, 155)
        self.write(3.7, "• Analogía de la vida real: ")
        self.set_font("ArialUni", "I", 7.6)
        self.write(3.7, f"{analogia}\n")
        self.ln(1)

    def applicability_section(self, aplica_txt, porque_txt):
        self.set_fill_color(255, 243, 224)
        self.set_text_color(230, 81, 0)
        self.set_font("ArialUni", "B", 8)
        self.cell(178, 4.5, "  2. ¿APLICA EN LA UNSA Y CUÁL ES SU ESTADO ACTUAL?", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(30, 30, 30)
        self.write(3.7, f"• Diagnóstico de Aplicabilidad: {aplica_txt}\n")
        self.set_font("ArialUni", "B", 7.6)
        self.write(3.7, "• Sustento técnico-legal: ")
        self.set_font("ArialUni", "", 7.6)
        self.write(3.7, f"{porque_txt}\n")
        self.ln(1)

    def section_univ(self, antecedentes, when, how, who, what, where):
        self.set_fill_color(232, 245, 233)
        self.set_text_color(46, 125, 50)
        self.set_font("ArialUni", "B", 8)
        self.cell(178, 4.5, "  3. PERSPECTIVA DE LA UNIVERSIDAD (UNSA) — IMPLEMENTACIÓN", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(46, 125, 50)
        self.write(3.7, "• Marco y Antecedentes Estatales: ")
        self.set_font("ArialUni", "I", 7.6)
        self.set_text_color(40, 40, 40)
        self.write(3.7, f"{antecedentes}\n")
        
        items_5w = [
            ("WHEN (Cuándo)", when),
            ("HOW (Cómo)", how),
            ("WHO (Quién)", who),
            ("WHAT (Qué entregables)", what),
            ("WHERE (Dónde se ubica)", where)
        ]
        for k, v in items_5w:
            self.set_font("ArialUni", "B", 7.6)
            self.set_text_color(46, 125, 50)
            self.write(3.7, f"• {k}: ")
            self.set_font("ArialUni", "", 7.6)
            self.set_text_color(30, 30, 30)
            self.write(3.7, f"{v}\n")
        self.ln(1)

    def section_audit(self, estado, riesgo, obs, recs):
        self.set_fill_color(255, 235, 238)
        self.set_text_color(198, 40, 40)
        self.set_font("ArialUni", "B", 8)
        self.cell(178, 4.5, f"  4. PERSPECTIVA DEL AUDITOR (Ing. Rafael) — ESTADO: {estado} | RIESGO: {riesgo}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(198, 40, 40)
        self.write(3.7, "• Observaciones de Auditoría: ")
        self.set_font("ArialUni", "", 7.6)
        self.set_text_color(30, 30, 30)
        self.write(3.7, f"{obs}\n")
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(198, 40, 40)
        self.write(3.7, "• Recomendaciones de Remediación: ")
        self.set_font("ArialUni", "", 7.6)
        self.set_text_color(30, 30, 30)
        self.write(3.7, f"{recs}\n")
        self.ln(1)

    def section_guiones(self, code, speech_univ, speech_audit):
        self.set_fill_color(243, 229, 245)
        self.set_text_color(123, 31, 162)
        self.set_font("ArialUni", "B", 8)
        self.cell(178, 4.5, f"  5. GUIONES DE EXPOSICIÓN ORAL — CONTROL {code}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(46, 125, 50)
        self.write(3.6, "• Guión Como Universidad (UNSA): ")
        self.set_font("ArialUni", "I", 7.6)
        self.set_text_color(45, 55, 65)
        self.write(3.6, f"\"{speech_univ}\"\n")
        
        self.set_font("ArialUni", "B", 7.6)
        self.set_text_color(198, 40, 40)
        self.write(3.6, "• Guión Como Auditor (Ing. Rafael): ")
        self.set_font("ArialUni", "I", 7.6)
        self.set_text_color(45, 55, 65)
        self.write(3.6, f"\"{speech_audit}\"\n")

print("Generando reporte maestro para Sección A.1.3...")
pdf = PDFReport()

# ==========================================
# PÁGINA 1: PORTADA
# ==========================================
pdf.add_page()
pdf.ln(20)
pdf.set_font("ArialUni", "B", 24)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 11, "ISO/IEC 27701:2025", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "B", 12.5)
pdf.set_text_color(57, 73, 171)
pdf.cell(0, 7, "TABLA A.1 — CONTROLES PARA RESPONSABLES DE PII (PII CONTROLLERS)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 7, "Sección: Obligations to PII Principals (Obligaciones hacia los Titulares)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

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
pdf.cell(160, 4.8, "• Alcance Normativo: Controles A.1.3.2 al A.1.3.11 (Derechos ARCO, Información y DSAR)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Marco Jurídico Peruano: Ley N° 29733, D.S. 016-2024-JUS, Ley N° 27444, Ley 30220", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Rol del Auditor: Ing. Rafael (MSc. Ciberseguridad & Auditoría TI, Lead Auditor ISO)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(25)
pdf.cell(160, 4.8, "• Articulación Académica: Soporte Normativo y de Auditoría para el Proyecto TIF-DSAR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(25)
pdf.set_font("ArialUni", "I", 9.5)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, "Arequipa, Perú — Semestre Académico 2026", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ==========================================
# PÁGINA 2: METODOLOGÍA E ÍNDICE
# ==========================================
pdf.add_page()
pdf.set_font("ArialUni", "B", 13.5)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 6.5, "Marco Normativo y Estructura de la Sección A.1.3", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

pdf.set_font("ArialUni", "", 8.6)
pdf.set_text_color(30, 30, 30)
intro_text = (
    "La sección A.1.3 de la norma ISO/IEC 27701:2025 ('Obligations to PII Principals') materializa el principio "
    "de soberanía y control del titular sobre sus datos personales. En la jurisdicción peruana, esta sección "
    "corresponde directamente al ejercicio y garantía de los Derechos ARCO (Acceso, Rectificación, Cancelación y "
    "Oposición) contemplados en la Ley N° 29733 y reforzados por el Decreto Supremo N° 016-2024-JUS.\n\n"
    "Este informe aborda los 10 controles de la sección mediante un enfoque riguroso de 1 página por control, "
    "articulando la visión institucional de la UNSA (5W), el criterio técnico del auditor líder y el soporte al "
    "proyecto académico TIF-DSAR (Agente Inteligente de Atención de Solicitudes):"
)
pdf.multi_cell(178, 4.3, intro_text)
pdf.ln(2)

controls_summary = [
    ("A.1.3.2", "Determining/fulfilling obligations to principals", "Obligaciones legales hacia titulares", "Pág. 3"),
    ("A.1.3.3", "Determining information for PII principals", "Definir información y timing de entrega", "Pág. 4"),
    ("A.1.3.4", "Providing information to PII principals", "Entrega clara y accesible de información", "Pág. 5"),
    ("A.1.3.5", "Providing mechanism to modify/withdraw consent", "Mecanismo para revocar consentimiento", "Pág. 6"),
    ("A.1.3.6", "Providing mechanism to object to processing", "Mecanismo de Derecho de Oposición", "Pág. 7"),
    ("A.1.3.7", "Access, correction or erasure", "Derechos ARCO (Acceso, Rectificación, Supresión)", "Pág. 8"),
    ("A.1.3.8", "Obligations to inform third parties", "Notificar cambios a terceros cesionarios", "Pág. 9"),
    ("A.1.3.9", "Providing copy of PII processed", "Entrega de copia de datos (Portabilidad)", "Pág. 10"),
    ("A.1.3.10", "Handling requests", "Gestión formal de solicitudes DSAR (Procedimiento)", "Pág. 11"),
    ("A.1.3.11", "Automated decision making", "Decisiones automatizadas y transparencia IA", "Pág. 12")
]

pdf.set_font("ArialUni", "B", 7.8)
pdf.set_fill_color(230, 235, 248)
pdf.set_text_color(26, 35, 126)
pdf.cell(16, 5, "Control", border=1, fill=True)
pdf.cell(75, 5, "Título Normativo (ISO 27701:2025)", border=1, fill=True)
pdf.cell(73, 5, "Alcance Técnico y Legal", border=1, fill=True)
pdf.cell(14, 5, "Ubicación", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "", 7.6)
pdf.set_text_color(30, 30, 30)
for c, en, es, pg in controls_summary:
    pdf.cell(16, 4.6, c, border=1)
    pdf.cell(75, 4.6, en, border=1)
    pdf.cell(73, 4.6, es, border=1)
    pdf.cell(14, 4.6, pg, border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# =========================================================================
# DATOS DETALLADOS DE CADA CONTROL (PÁGINAS 3 A 12)
# =========================================================================

controls_data = [
    {
        "code": "A.1.3.2",
        "title_en": "Determining and fulfilling obligations to PII principals",
        "title_es": "Determinar y cumplir obligaciones hacia los titulares de PII",
        "norm_text": "The organization shall determine and document its legal, regulatory and business obligations to PII principals related to the processing of their PII and provide the means to meet these obligations.",
        "explain": "La entidad debe tener una lista oficial y completa de TODOS los derechos de los titulares (alumnos, docentes, egresados) y debe asegurar el presupuesto, sistemas y personal para cumplirlos efectivamente.",
        "analogia": "Una aerolínea está obligada por ley a reembolsar pasajes cancelados y atender reclamos; no puede decir 'no sabía', debe fijar esas políticas en sus manuales y tener módulos de atención en el aeropuerto con personal capacitado.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA está obligada por la Ley 29733 y D.S. 016-2024-JUS. En su web menciona derechos ARCO pero no tiene una Directiva aprobada por Resolución Rectoral ni una ventanilla especializada con plazos regulados.",
        "antecedentes": "Ley 29733 (Título III), D.S. 016-2024-JUS, Ley 27444 (debido procedimiento administrativo) y Ley Universitaria 30220.",
        "when": "Primeros 60 días del despliegue del PIMS. Revisión anual obligatoria o ante cambios normativos del MINJUSDH.",
        "how": "1. Identificar obligaciones de la Ley 29733. 2. Redactar el Reglamento Institucional de Derechos del Titular. 3. Aprobarlo vía Resolución Rectoral. 4. Habilitar mesa de partes física y módulo SISUNSA.",
        "who": "Asesoría Jurídica y Secretaría General (redacción), OTI (canales virtuales) y Rectorado (aprobación formal).",
        "what": "1. Reglamento Institucional de Derechos de los Titulares. 2. Resolución Rectoral. 3. Catálogo de obligaciones frente a la comunidad.",
        "where": "Portal de Transparencia Estándar, web institucional, mesa de partes general y Secretaría General.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "La universidad reconoce derechos en su web pero no provee los medios reales (means): si un alumno acude a Mesa de Partes a pedir supresión de datos, el personal no sabe qué trámite seguir.",
        "rec_audit": "Aprobar el Reglamento de Derechos de Titulares por Consejo Universitario y designar formalmente al Oficial de Protección de Datos (DPO).",
        "speech_univ": "Para el control A.1.3.2, la UNSA no solo debe saber que la Ley 29733 existe, sino poner los medios reales para cumplirla. Hoy los derechos se mencionan en la web pero no hay ventanilla especializada. Proponemos aprobar un Reglamento de Derechos por Resolución Rectoral y habilitar módulos en SISUNSA y mesas de partes.",
        "speech_audit": "Como auditor líder, califico este punto como PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO). La norma pide determinar obligaciones y proveer los medios (means). La UNSA cumple la teoría legal pero falla en la práctica: no hay personal asignado ni formularios específicos. Exijo institucionalizar la oficina en 60 días."
    },
    {
        "code": "A.1.3.3",
        "title_en": "Determining information for PII principals",
        "title_es": "Determinar la información a proporcionar a los titulares",
        "norm_text": "The organization shall determine and document the information to be provided to PII principals regarding the processing of their PII and the timing of such a provision.",
        "explain": "Se debe definir de antemano QUÉ DATOS EXACTOS se informarán al usuario (identidad, fin, transferencias, retención) y EN QUÉ MOMENTO se entregarán (de forma previa o simultánea a la recolección).",
        "analogia": "Cuando compras un medicamento, la ley exige un prospecto obligatorio en la caja con dosis, contraindicaciones y vencimiento. El laboratorio definió con exactitud qué informar antes de imprimir la caja.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "Aplica a todos los puntos de recolección de la UNSA. Aunque tiene una política web, no ha determinado el paquete informativo obligatorio para cada punto ni el timing; en admisión no se informa sobre la conservación de notas.",
        "antecedentes": "Ley 29733 (Art. 18 - Deber de Información), D.S. 016-2024-JUS y directivas de la ANPD sobre avisos informativos.",
        "when": "En la fase de diseño de formularios (plazo 45 días). Entrega de información previa o simultánea a la recolección de datos.",
        "how": "Diseñar Estructura Informativa Multinivel: Nivel 1 (aviso corto con finalidad y QR en el formulario) + Nivel 2 (política detallada en la web).",
        "who": "OTI (interfaces), Asesoría Jurídica (redacción legal) y Dirección de Comunicación e Imagen Institucional.",
        "what": "1. Estándar Informativo para Recolección de Datos. 2. Plantillas de Avisos Multinivel. 3. Matriz de Momento Informativo (Timing).",
        "where": "Fichas de inscripción de admisión, formularios SISUNSA, carteles de videovigilancia y boletas de pago.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "En becas de comedor y bolsas de trabajo se piden datos socioeconómicos íntimos sin informar previamente el tiempo de conservación ni si serán compartidos con SISFOH/MIDIS.",
        "rec_audit": "Homologar todos los formularios físicos y digitales de recolección con la estructura informativa de la Ley 29733 (Art. 18).",
        "speech_univ": "El control A.1.3.3 exige definir qué le informamos al estudiante y en qué momento. La Ley 29733 exige informar el responsable, los fines y las transferencias. Implementaremos avisos multinivel: un aviso corto con código QR en los formularios de matrícula y admisión, y la política completa en la web.",
        "speech_audit": "Califico como PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO). El control exige regular el timing: informar al momento exacto de la recolección. En la UNSA las políticas están en el pie de página de la web, pero el postulante o alumno no las ve al matricularse. Se exige la matriz informativa en 45 días."
    },
    {
        "code": "A.1.3.4",
        "title_en": "Providing information to PII principals",
        "title_es": "Proporcionar información a los titulares de PII",
        "norm_text": "The organization shall provide PII principals with clear and easily accessible information identifying the PII controller and describing the processing of their PII.",
        "explain": "Exige la ENTREGA REAL Y ACCESIBLE de la información: debe estar en lenguaje claro (sin jerga legal abusiva), visible a simple vista y accesible sin costo ni barreras físicas o digitales.",
        "analogia": "Es como los letreros verdes de salida de emergencia en un cine: deben ser visibles a simple vista y entendibles por cualquiera, no guardados en un archivador cerrado de la gerencia.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA tiene política web, pero está en lenguaje legal complejo, no es accesible para discapacidades visuales y en los campus no existen carteles informativos de zona videovigilada conforme a la directiva de la ANPD.",
        "antecedentes": "Directiva de Seguridad de la ANPD para Videovigilancia, D.S. 016-2024-JUS y estándares W3C de accesibilidad web.",
        "when": "Ejecución en 30 días calendario y actualización continua ante cambios de autoridades o sistemas informáticos.",
        "how": "1. Rediseñar la sección web de privacidad con lenguaje ciudadano. 2. Instalar carteles físicos de videovigilancia en los 3 campus. 3. Poner banners en SISUNSA.",
        "who": "Oficina de Comunicación e Imagen (redacción accesible), OTI (web) y Servicios Generales (cartelería física).",
        "what": "1. Portal Web Accesible de Privacidad. 2. Cartelería física de videovigilancia homologada. 3. Guía rápida ilustrada de derechos.",
        "where": "Página principal (`unsa.edu.pe`), puertas y pabellones de Ingenierías, Sociales y Biomédicas, y aulas virtuales.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO-ALTO",
        "obs_audit": "Hay más de 100 cámaras de seguridad activas en los campus sin ningún cartel de advertencia de videovigilancia que identifique al responsable del banco de datos.",
        "rec_audit": "Instalar con carácter de urgencia la cartelería física homologada de videovigilancia y rediseñar la política web en lenguaje accesible.",
        "speech_univ": "El control A.1.3.4 exige que la información sea fácil de encontrar y entender. Rediseñaremos la web de privacidad para que cualquier alumno la comprenda sin ser abogado. Además, colocaremos carteles visibles en los ingresos de los campus avisando sobre las cámaras de videovigilancia y quién custodia las grabaciones.",
        "speech_audit": "Levanto una observación formal calificada como PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO-ALTO). Omitir carteles de videovigilancia en los campus es una infracción pasible de sanción por la ANPD. Los estudiantes no tienen forma de saber quién custodia las grabaciones. Ordeno subsanar carteles en 30 días."
    },
    {
        "code": "A.1.3.5",
        "title_en": "Providing mechanism to modify or withdraw consent",
        "title_es": "Proporcionar mecanismo para modificar o revocar el consentimiento",
        "norm_text": "The organization shall provide a mechanism for PII principals to modify or withdraw their consent.",
        "explain": "Dar consentimiento no es irreversible; el titular tiene derecho a cambiar de opinión. La entidad debe ofrecer un mecanismo tan fácil para RETIRAR el permiso como lo fue para otorgarlo.",
        "analogia": "Si te suscribes a un boletín o servicio web con un solo clic, debe haber un botón visible que diga 'Cancelar suscripción'. Sería abusivo e ilegal que para salirte te exijan enviar una carta notarial.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "Aplica para tratamientos basados en consentimiento (fotos institucionales, becas voluntarias, correos de eventos externos). La UNSA no dispone de ningún botón ni trámite en SISUNSA para desmarcar autorizaciones.",
        "antecedentes": "Ley 29733 (Art. 13.5), D.S. 016-2024-JUS (regla de equivalencia de medios para revocatoria gratuita y accesible).",
        "when": "Desarrollo en 60 días calendario y vigencia permanente dentro de la plataforma virtual del estudiante.",
        "how": "1. Habilitar en SISUNSA la pestaña 'Mis Permisos de Privacidad'. 2. Configurar casillas toggles para autorizaciones opcionales. 3. Actualizar bases de datos al desactivar.",
        "who": "OTI (desarrollo informático) y Asesoría Jurídica (reglas de negocio sobre tratamientos revocables vs. obligatorios de ley).",
        "what": "1. Módulo Web de Gestión de Consentimientos en SISUNSA. 2. Formulario de Revocatoria para mesa de partes. 3. Procedimiento de baja técnica.",
        "where": "Configuración de perfil en SISUNSA y Mesa de Partes física de la universidad.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "No existe ningún mecanismo en los sistemas institucionales para retirar el consentimiento. Los egresados no tienen opción de opt-out en correos masivos de posgrado.",
        "rec_audit": "Implementar el módulo de preferencias de privacidad en SISUNSA y agregar enlace de desuscripción automática al pie de los correos institucionales.",
        "speech_univ": "El control A.1.3.5 garantiza que el estudiante sea dueño de su decisión. Si autorizó el uso de su foto o recibir correos de ferias de empleo, puede cambiar de opinión. Agregaremos una pestaña en SISUNSA llamada 'Mis Permisos' para que con un clic desactive las autorizaciones voluntarias, tal como exige la ley peruana.",
        "speech_audit": "Declaro NO IMPLEMENTADO con riesgo ALTO. La revocabilidad es un pilar de la Ley 29733 y la ISO 27701. Retener datos contra la voluntad del titular sin una obligación legal imperativa constituye infracción grave. Se exige el despliegue del módulo de revocatoria en 60 días."
    },
    {
        "code": "A.1.3.6",
        "title_en": "Providing mechanism to object to PII processing",
        "title_es": "Mecanismo para oponerse al tratamiento (Derecho de Oposición)",
        "norm_text": "The organization shall provide a mechanism for PII principals to object to the processing of their PII.",
        "explain": "Aunque la entidad tenga base legal para procesar datos, si el titular tiene un motivo fundado y legítimo de afectación personal (seguridad, acoso), puede exigir que dejen de usar sus datos para ese fin específico.",
        "analogia": "Si una empresa publica el directorio con teléfonos y direcciones de todos sus trabajadores, pero una empleada tiene una orden de restricción contra una expareja violenta, tiene derecho a oponerse para proteger su integridad.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "El Derecho de Oposición es fundamental (Art. 22 Ley 29733). Aplica si un estudiante solicita que no se publique su nombre en murales o listas de mérito por razones de seguridad. La UNSA no tiene protocolo formal para esto.",
        "antecedentes": "Ley 29733 (Art. 22 - Derecho de Oposición), D.S. 016-2024-JUS (plazo perentorio de respuesta: 10 días hábiles).",
        "when": "Aprobación en 60 días calendario; respuesta obligatoria en un máximo de 10 días hábiles desde la presentación.",
        "how": "1. Diseñar el Procedimiento de Oposición. 2. Crear formulario físico y digital. 3. Ponderar legalmente el motivo del titular frente al deber institucional. 4. Bloquear el tratamiento en 10 días.",
        "who": "Asesoría Jurídica (evaluación de motivos fundados), Secretaría General (recepción) y OTI (bloqueo en base de datos).",
        "what": "1. Directiva Institucional de Oposición. 2. Formulario Normalizado de Oposición de PII. 3. Matriz de criterios de ponderación legal.",
        "where": "Mesa de partes física, mesa de partes virtual de la UNSA y módulo de trámites del estudiante.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "Se identificó la publicación de listas de notas con nombres y DNI completos en murales físicos de facultades, sin permitir a los estudiantes oponerse por privacidad o seguridad.",
        "rec_audit": "Prohibir la exhibición pública de DNI en listas de calificaciones y aprobar el procedimiento formal de oposición con plazo de 10 días.",
        "speech_univ": "El control A.1.3.6 corresponde a la letra 'O' de los derechos ARCO: el Derecho de Oposición. Si un alumno tiene motivos justificados, como sufrir acoso o amenazas, puede oponerse a que su nombre se publique en murales. Crearemos el formulario oficial con un plazo legal de 10 días hábiles para resolver y bloquear los datos.",
        "speech_audit": "Califico como NO IMPLEMENTADO (Riesgo ALTO). Denegar injustificadamente el derecho de oposición es sancionado con multas graves por la ANPD. En la UNSA los estudiantes no tienen una vía formal para oponerse a la difusión pública de sus datos. Exijo emitir la directiva y formulario en 60 días."
    },
    {
        "code": "A.1.3.7",
        "title_en": "Access, correction or erasure",
        "title_es": "Acceso, rectificación o supresión (Derechos ARCO)",
        "norm_text": "The organization shall implement policies, procedures or mechanisms to meet its obligations to PII principals to access, correct or erase their PII.",
        "explain": "Es el núcleo de los Derechos ARCO: Acceso (saber qué datos tienen de ti), Rectificación (corregir errores o desactualizaciones) y Cancelación/Supresión (borrar datos cuando no haya base legal o ya no sean necesarios).",
        "analogia": "Si en tu reporte crediticio o en tu DNI tu apellido está mal escrito o figura una deuda ya pagada, tienes derecho a que corrijan el error y borren el registro deudor. La entidad no puede negarse.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA tramita rectificaciones de nombres o notas mediante trámites administrativos tradicionales (FUT), pero son burocráticos y exceden los plazos legales (10 y 20 días). No existe protocolo de supresión de datos.",
        "antecedentes": "Ley 29733 (Art. 19, 20 y 21), D.S. 016-2024-JUS (gratuidad absoluta de los derechos ARCO, plazos: 20 días acceso, 10 rectificación/cancelación).",
        "when": "Aprobación en 60 días calendario. Cumplimiento estricto de plazos: 20 días para acceso y 10 para rectificación y supresión.",
        "how": "1. Integrar trámite gratuito ARCO en el TUPA. 2. Habilitar módulo en SISUNSA con seguimiento. 3. Crear procedimiento técnico de borrado seguro y anonimización en OTI.",
        "who": "Oficial de Protección de Datos (DPO), Secretaría General, OTI (ejecución técnica en bases de datos) y Asesoría Jurídica.",
        "what": "1. Procedimiento Operativo de Atención ARCO. 2. Formulario Único Gratuito ARCO. 3. Protocolo de Supresión y Anonimización Segura.",
        "where": "Mesa de partes física de facultades, Mesa de Partes Virtual y módulo SISUNSA.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "Los trámites de rectificación de datos en Secretaría General demoran hasta 60 días, superando holgadamente los 10 días de ley. No existe proceso de supresión para postulantes no admitidos.",
        "rec_audit": "Rediseñar el flujo administrativo para cumplir estrictamente con los plazos de 10 y 20 días hábiles y eliminar tasas arancelarias en trámites de privacidad.",
        "speech_univ": "El control A.1.3.7 representa el corazón de los Derechos ARCO: Acceso, Rectificación y Supresión. La ley peruana exige que sea 100% gratuito y rápido: 20 días para acceso y 10 para rectificar o borrar. Implementaremos el trámite digital en SISUNSA para que el alumno no tenga que hacer colas con papeles.",
        "speech_audit": "Califico como PARCIALMENTE IMPLEMENTADO con riesgo ALTO. La debilidad crítica de la UNSA es la demora: los trámites burocráticos sobrepasan los plazos de ley, lo que expone a la universidad a multas de hasta 50 UIT por la ANPD. Exijo un sistema automatizado con alertas de vencimiento."
    },
    {
        "code": "A.1.3.8",
        "title_en": "PII controllers' obligations to inform third parties",
        "title_es": "Obligación de informar a terceros cesionarios",
        "norm_text": "The organization shall inform third parties with whom PII has been shared of any modification, withdrawal or objections pertaining to the shared PII, and implement appropriate policies, procedures or mechanisms to do so.",
        "explain": "Si compartiste datos con un tercero (SUNEDU, bancos, ministerios) y luego el titular rectifica o cancela su información, estás obligado a AVISARLE a ese tercero para que también actualice o borre los datos en sus sistemas.",
        "analogia": "Es el efecto dominó: si cambias legalmente de nombre en el RENIEC, no basta con actualizar su oficina; RENIEC avisa a SUNAT, Migraciones y bancos para que en todos lados figures con tu nombre correcto.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "La UNSA comparte datos masivos con SUNEDU, MINEDU, bancos recaudadores y PRONABEC. Si un alumno corrige judicialmente su nombre o género en la UNSA, no existe procedimiento para notificar a esos terceros.",
        "antecedentes": "Ley 29733 (Art. 16 y 20), D.S. 016-2024-JUS (obligación de comunicar rectificaciones a cesionarios en plazo breve).",
        "when": "Diseño en 90 días calendario y ejecución en un máximo de 10 días hábiles tras aprobarse una rectificación o cancelación.",
        "how": "1. Mantener registro de transferencias. 2. Diseñar Protocolo de Comunicación a Terceros. 3. Enviar oficios electrónicos o sincronización API hacia entidades externas.",
        "who": "Dirección de Asuntos Académicos (DUFA), Secretaría General, OTI y Asesoría Jurídica.",
        "what": "1. Protocolo de Notificación a Terceros Receptores de Datos. 2. Registro de Transferencias y Notificaciones. 3. Modelo de Oficio de Comunicación ARCO.",
        "where": "Secretaría General de la UNSA y módulos de interoperabilidad técnica de OTI.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "Cuando un alumno rectifica apellidos por filiación, la UNSA actualiza su base interna pero no notifica a los bancos del padrón de matrícula, provocando rechazos de pago y desactualización externa.",
        "rec_audit": "Elaborar el protocolo de notificación a terceros y crear una bitácora de interoperabilidad de transferencias.",
        "speech_univ": "El control A.1.3.8 evita que los datos errados queden flotando en otras entidades. Si la UNSA envió datos a SUNEDU o a bancos de cobranza, y el alumno corrige su nombre en la universidad, debemos notificar formalmente a esas instituciones externas. Implementaremos un protocolo de oficio digital automático.",
        "speech_audit": "Determino este control como NO IMPLEMENTADO (Riesgo MEDIO). La cadena de exactitud de los datos se rompe si la UNSA no notifica a los terceros con quienes comparte información. Si un alumno corrige sus datos y no se avisa a SUNEDU, se producen perjuicios directos. Se exige el protocolo en 60 días."
    },
    {
        "code": "A.1.3.9",
        "title_en": "Providing copy of PII processed",
        "title_es": "Proporcionar copia de la PII tratada (Portabilidad / Acceso)",
        "norm_text": "The organization shall be able to provide a copy of the PII that is processed, when requested by the PII principal.",
        "explain": "Si un usuario te dice 'quiero una copia de toda la información que tienes sobre mí', debes poder extraer y entregarle un reporte completo de sus datos en un formato legible, estructurado y seguro.",
        "analogia": "Es como pedir tu Historia Clínica completa en un hospital o el consolidado de movimientos bancarios: la institución está legalmente obligada a darte una copia íntegra de tu expediente.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO.",
        "porque_txt": "La UNSA entrega certificados de notas y constancias de matrícula, pero cobra tasas (TUPA). No existe mecanismo para entregar gratuitamente una copia consolidada de datos médicos, biométricos o de biblioteca.",
        "antecedentes": "Ley 29733 (Art. 19 - Derecho de Acceso y Gratuidad), D.S. 016-2024-JUS (entrega en formato accesible y legible).",
        "when": "Desarrollo en 60 días calendario; entrega de la copia en un máximo de 20 días hábiles tras la solicitud formal.",
        "how": "1. Crear en SISUNSA el botón 'Descargar mi Expediente de Datos Personales'. 2. Generar PDF/ZIP cifrado con datos académicos, médicos y registros. 3. Para solicitudes presenciales, entregar reporte impreso sin costo.",
        "who": "OTI (scripts de extracción y compilación de datos) y Secretaría General (entrega presencial).",
        "what": "1. Módulo digital de auto-descarga de expediente de PII en SISUNSA. 2. Formato del Reporte Maestro de Datos Personales. 3. Protocolo de entrega segura.",
        "where": "Menú del estudiante en SISUNSA y Mesa de Partes General de la UNSA.",
        "estado_audit": "Parcialmente Implementado",
        "riesgo_audit": "MEDIO",
        "obs_audit": "La universidad condiciona la entrega de información personal al cobro de aranceles (ej. certificados), vulnerando la gratuidad del Derecho de Acceso de la Ley 29733. No hay forma de exportar registros biométricos.",
        "rec_audit": "Implementar la descarga gratuita del expediente de datos personales en SISUNSA y definir el protocolo para registros especiales de biometría e imágenes.",
        "speech_univ": "El control A.1.3.9 exige que la universidad pueda entregarle al alumno una copia completa de toda su información. Hoy entregamos certificados pero cobrando tasas y solo de notas. Implementaremos una opción en SISUNSA para descargar gratis su Expediente de Privacidad en PDF con todos sus datos consolidados y cifrados.",
        "speech_audit": "Evalúo este control como PARCIALMENTE IMPLEMENTADO (Riesgo MEDIO). Cobrar por copias de datos personales vulnera la gratuidad establecida por la ANPD. Además, la OTI debe poder exportar datos en formatos estructurados estándar. Recomiendo habilitar la función de exportación gratuita en 60 días."
    },
    {
        "code": "A.1.3.10",
        "title_en": "Handling requests",
        "title_es": "Gestión y resolución de solicitudes de titulares (DSAR)",
        "norm_text": "The organization shall define and document policies and procedures for handling and responding to legitimate requests from PII principals.",
        "explain": "Es el PROCEDIMIENTO OPERATIVO COMPLETO para atender solicitudes de derechos (DSAR): cómo se valida la identidad del titular, cómo se registra, quién investiga internamente, quién responde y cómo se cumplen los plazos.",
        "analogia": "Es como el Libro de Reclamaciones formal: no basta con tener el libro; la empresa tiene un manual estricto que dice que cada reclamo se numera, se deriva, se investiga y se responde por escrito en el plazo de ley.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO (Formalmente).",
        "porque_txt": "Las solicitudes de datos en la UNSA entran por Mesa de Partes genérica bajo la Ley 27444 (plazo de 30 días), violando los plazos más cortos de la Ley 29733 (10 y 20 días). Este es el foco directo del proyecto TIF-DSAR.",
        "antecedentes": "Ley 29733 (Título III), D.S. 016-2024-JUS (plazos de 10 y 20 días hábiles) y Ley 27444 (principios de celeridad y eficacia).",
        "when": "Primeros 60 días calendario para el procedimiento administrativo y tecnológico.",
        "how": "1. Aprobar la Directiva de Procedimiento DSAR. 2. Implementar flujo digital con numeración de expediente de privacidad. 3. Incorporar el Agente de IA (TIF-DSAR) para preclasificar y redactar respuestas.",
        "who": "Oficial de Protección de Datos (DPO), Secretaría General, Asesoría Jurídica y OTI.",
        "what": "1. Manual de Procedimientos DSAR de la UNSA. 2. Libro Digital de Registro de Solicitudes ARCO. 3. Modelos de resolución de respuesta formal.",
        "where": "Sistema de Trámite Documentario (STD) de la UNSA y Mesa de Partes Virtual.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "ALTO",
        "obs_audit": "La universidad carece de un procedimiento especial para solicitudes de datos personales. Las peticiones se mezclan con trámites generales, perdiendo trazabilidad y venciendo los plazos legales.",
        "rec_audit": "Separar el flujo de solicitudes de privacidad en el Sistema de Trámite Documentario y desplegar un sistema de seguimiento automatizado con semáforos de plazos.",
        "speech_univ": "El control A.1.3.10 es el procedimiento operativo que hace realidad los derechos de los alumnos. Si un pedido entra por Mesa de Partes común, se pierde entre miles de papeles. Con este control creamos un flujo especializado: valida identidad, clasifica el pedido y activa un reloj de 10 o 20 días. Aquí se integra nuestro proyecto TIF con el agente de IA.",
        "speech_audit": "Determino este control como NO IMPLEMENTADO (Riesgo ALTO). No contar con un procedimiento documentado para gestionar solicitudes DSAR expone a la universidad a multas coercitivas de la ANPD ante el primer reclamo no atendido. Dictamino implementar de inmediato el protocolo DSAR y su libro de control en 45 días."
    },
    {
        "code": "A.1.3.11",
        "title_en": "Automated decision making",
        "title_es": "Decisiones automatizadas y perfilamiento de titulares",
        "norm_text": "The organization shall identify obligations, including legal obligations, to the PII principals resulting from decisions made by the organization which are related to the PII principal based solely on automated processing of PII, and be able to demonstrate how it addresses these obligations.",
        "explain": "Si un algoritmo o sistema de Inteligencia Artificial toma una decisión que afecta la vida de una persona SIN intervención humana (rechazar una beca, asignar turnos o calificar), se debe explicar la lógica y garantizar el derecho a revisión humana.",
        "analogia": "Si postulas a un crédito bancario y una IA te rechaza en 2 segundos basándose en tu edad o código postal, tienes derecho a saber por qué fuiste rechazado y exigir que un analista humano revise tu caso manualmente.",
        "aplica_txt": "APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO.",
        "porque_txt": "La UNSA utiliza algoritmos para turnos de matrícula, selección de cupos de comedor universitario y calificación óptica de exámenes de admisión. No tiene un protocolo que reconozca el derecho a revisión humana de estas decisiones.",
        "antecedentes": "ISO/IEC 27701:2025, Directivas de Inteligencia Artificial de la PCM y principios de debido procedimiento de la Ley 27444.",
        "when": "Plazo de 60 días calendario para la auditoría de algoritmos y formalización del derecho de revisión humana.",
        "how": "1. Inventariar sistemas de decisión automatizada. 2. Documentar la lógica de los algoritmos en fichas comprensibles. 3. Habilitar en SISUNSA el botón 'Solicitar revisión humana'. 4. Crear comités de apelación.",
        "who": "OTI (documentación técnica de algoritmos), Asesoría Jurídica y Direcciones Académicas correspondientes.",
        "what": "1. Catálogo Institucional de Sistemas de Decisión Automatizada. 2. Protocolo de Garantía de Intervención Humana. 3. Fichas de Explicabilidad de Algoritmos.",
        "where": "Reglamentos académicos de matrícula y becas, y en el sistema informático SISUNSA.",
        "estado_audit": "No Implementado",
        "riesgo_audit": "MEDIO-ALTO",
        "obs_audit": "Existen procesos donde el sistema informático rechaza beneficios estudiantiles de forma automatizada sin que los alumnos conozcan la fórmula exacta ni tengan derecho a una reconsideración manual.",
        "rec_audit": "Elaborar fichas de transparencia algorítmica y reglamentar formalmente el derecho a la revisión humana de decisiones automáticas.",
        "speech_univ": "Finalizamos con el control A.1.3.11: Decisiones automatizadas. En la UNSA usamos sistemas automáticos para ordenar matrículas o asignar cupos de comedor. Este control exige que ningún estudiante quede desamparado ante una decisión de una computadora: la universidad debe explicar la fórmula y garantizar que un ser humano pueda revisar su caso.",
        "speech_audit": "Dictamino este control como NO IMPLEMENTADO con riesgo MEDIO-ALTO. Con el avance de la inteligencia artificial, este control de la ISO 27701:2025 cobra una vigencia vital. La universidad no puede escudarse en 'así lo calculó el sistema' sin brindar explicabilidad ni derecho a revisión humana. Se exige transparentar la lógica en 60 días."
    }
]

# =========================================================================
# GENERACIÓN DE PÁGINAS 3 A 12 (UNA PÁGINA EXACTA POR CONTROL)
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
# PÁGINA 13: CONCLUSIONES Y DICTAMEN GLOBAL
# ==========================================
pdf.add_page()
pdf.set_font("ArialUni", "B", 13.5)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 6.5, "Dictamen Global de Auditoría — Sección A.1.3 y Articulación TIF-DSAR", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

pdf.set_font("ArialUni", "", 8.5)
pdf.set_text_color(30, 30, 30)
resumen_global = (
    "Tras la evaluación de los 10 controles de la Sección A.1.3 de la norma ISO/IEC 27701:2025 ('Obligaciones hacia los "
    "Titulares de PII') en la Universidad Nacional de San Agustín (UNSA), el auditor líder Ing. Rafael determina que "
    "la institución presenta una vulnerabilidad crítica en la atención de Derechos ARCO y gestión de solicitudes DSAR. "
    "No existen flujos especializados con alertas de tiempo ni protocolos para decisiones automatizadas."
)
pdf.multi_cell(178, 4.2, resumen_global)
pdf.ln(2)

# Tabla resumen
pdf.set_font("ArialUni", "B", 7.8)
pdf.set_fill_color(26, 35, 126)
pdf.set_text_color(255, 255, 255)
pdf.cell(16, 5, "Control", border=1, fill=True)
pdf.cell(66, 5, "Nombre del Control (ISO 27701)", border=1, fill=True)
pdf.cell(48, 5, "Estado de Madurez", border=1, fill=True)
pdf.cell(24, 5, "Nivel Riesgo", border=1, fill=True)
pdf.cell(24, 5, "Prioridad", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

summary_rows = [
    ("A.1.3.2", "Determining/fulfilling obligations", "Parcialmente Implementado", "MEDIO", "Alta (P1)"),
    ("A.1.3.3", "Determining info for principals", "Parcialmente Implementado", "MEDIO", "Media (P2)"),
    ("A.1.3.4", "Providing info to principals", "Parcialmente Implementado", "MEDIO-ALTO", "Alta (P1)"),
    ("A.1.3.5", "Modify or withdraw consent", "No Implementado", "ALTO", "Alta (P1)"),
    ("A.1.3.6", "Mechanism to object (Oposición)", "No Implementado", "ALTO", "Alta (P1)"),
    ("A.1.3.7", "Access, correction or erasure (ARCO)", "Parcialmente Implementado", "ALTO", "Urgente (P1)"),
    ("A.1.3.8", "Inform third parties of changes", "No Implementado", "MEDIO", "Media (P2)"),
    ("A.1.3.9", "Providing copy of PII (Portabilidad)", "Parcialmente Implementado", "MEDIO", "Media (P2)"),
    ("A.1.3.10", "Handling requests (DSAR)", "No Implementado", "ALTO", "Urgente (P1)"),
    ("A.1.3.11", "Automated decision making", "No Implementado", "MEDIO-ALTO", "Media (P2)")
]

pdf.set_font("ArialUni", "", 7.5)
for c_code, c_name, c_est, c_risk, c_prio in summary_rows:
    pdf.set_text_color(30, 30, 30)
    pdf.cell(16, 4.4, c_code, border=1)
    pdf.cell(66, 4.4, c_name, border=1)
    
    if "No" in c_est:
        pdf.set_text_color(180, 0, 0)
    else:
        pdf.set_text_color(180, 100, 0)
    pdf.cell(48, 4.4, c_est, border=1)
    
    if "ALTO" in c_risk:
        pdf.set_text_color(180, 0, 0)
    else:
        pdf.set_text_color(100, 100, 0)
    pdf.cell(24, 4.4, c_risk, border=1)
    
    pdf.set_text_color(30, 30, 30)
    pdf.cell(24, 4.4, c_prio, border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(3)

# Conexión TIF
pdf.set_font("ArialUni", "B", 9.5)
pdf.set_text_color(26, 35, 126)
pdf.cell(0, 5, "Articulación Estratégica con el Proyecto TIF-DSAR (Agente de IA):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("ArialUni", "", 8)
pdf.set_text_color(40, 40, 40)
tif_text = (
    "Los controles evaluados justifican plenamente el Trabajo de Investigación Formativa (TIF-DSAR): "
    "El desarrollo de un Agente de Inteligencia Artificial especializado en atención de solicitudes automatiza de forma directa "
    "los controles A.1.3.6 (Oposición), A.1.3.7 (Acceso/Rectificación/Cancelación) y A.1.3.10 (Gestión de Solicitudes). "
    "El agente valida identidad, clasifica pedidos, controla plazos perentorios de 10 y 20 días hábiles y genera borradores "
    "técnicos de respuesta, mitigando el riesgo de sanciones administrativas ante la ANPD."
)
pdf.multi_cell(178, 4, tif_text)
pdf.ln(2)

pdf.set_fill_color(232, 234, 246)
pdf.set_draw_color(26, 35, 126)
pdf.rect(16, pdf.get_y(), 178, 14, style="FD")
pdf.set_xy(19, pdf.get_y() + 1.8)
pdf.set_font("ArialUni", "B", 8.2)
pdf.set_text_color(26, 35, 126)
pdf.cell(172, 4, "FIRMA Y RESPONSABILIDAD TÉCNICA DEL AUDITOR LÍDER:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(19)
pdf.set_font("ArialUni", "I", 7.8)
pdf.set_text_color(50, 50, 50)
pdf.cell(172, 4, "Ing. Rafael — Especialista en Ciberseguridad y Auditoría TI (MSc.) | Lead Auditor ISO/IEC 27001 & 27701", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Guardar PDF
print(f"Guardando PDF en: {OUTPUT_FILE}...")
pdf.output(OUTPUT_FILE)
print(f"¡PDF generado con éxito! Tamaño: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB, Páginas totales: {pdf.page_no()}")
