#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de PDF Oficial:
GUION MAESTRO DE EXPOSICIÓN (5 INTEGRANTES) — AUDITPIMS 2.0
Universidad Nacional de San Agustín (UNSA) - Auditoría de Sistemas 2026
"""

import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT_PDF = "/Users/piero.o/Downloads/SEMESTRE II - SISTEMAS/AUDITORIA/GUION_EXPOSICION_5_INTEGRANTES_GRUPO4.pdf"

class Guion5PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(left=15, top=15, right=15)
        
        # Cargar fuentes del sistema Mac si existen
        font_dir = '/System/Library/Fonts/Supplemental'
        if os.path.exists(os.path.join(font_dir, 'Arial.ttf')):
            self.add_font('ArialCustom', '', os.path.join(font_dir, 'Arial.ttf'))
            self.add_font('ArialCustom', 'B', os.path.join(font_dir, 'Arial Bold.ttf'))
            self.add_font('ArialCustom', 'I', os.path.join(font_dir, 'Arial Italic.ttf'))
            self.font_family_name = 'ArialCustom'
        else:
            self.font_family_name = 'Helvetica'

    def header(self):
        self.set_font(self.font_family_name, 'B', 7.5)
        self.set_text_color(120, 53, 15) # Ámbar oscuro
        self.cell(0, 4, "UNSA | ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS | AUDITORÍA DE SISTEMAS (2026)", 
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_font(self.font_family_name, 'I', 7)
        self.set_text_color(100, 110, 120)
        self.cell(0, 4, "AuditPIMS 2.0: Agente de Evidencia y Auditoría (Grupo 4) | Guion Oficial 5 Integrantes", 
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_draw_color(220, 180, 130)
        self.set_line_width(0.3)
        self.line(15, self.get_y() + 1, 195, self.get_y() + 1)
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_font(self.font_family_name, 'I', 7.5)
        self.set_text_color(130, 140, 150)
        self.set_draw_color(220, 225, 230)
        self.line(15, self.get_y() - 1, 195, self.get_y() - 1)
        self.cell(0, 6, f"Página {self.page_no()}/{{nb}} - AuditPIMS Grupo 4 (UNSA 2026)", align="C")

    def speaker_header(self, num_str, name_str, role_str, time_str):
        self.set_x(15)
        self.ln(1)
        self.set_fill_color(254, 243, 199) # Ámbar suave
        self.set_draw_color(217, 119, 6) # Borde ámbar fuerte
        self.set_line_width(0.4)
        
        self.set_font(self.font_family_name, 'B', 9.5)
        self.set_text_color(120, 53, 15)
        self.cell(135, 6.5, f" {num_str}. {name_str} — {role_str}", border=1, fill=True)
        
        self.set_font(self.font_family_name, 'B', 8.5)
        self.set_text_color(180, 83, 9)
        self.cell(45, 6.5, f"Tiempo: {time_str} ", border=1, fill=True, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.5)

    def screen_cue(self, text):
        self.set_x(15)
        self.set_font(self.font_family_name, 'B', 7.5)
        self.set_text_color(146, 64, 14) # Ámbar marrón
        self.set_fill_color(255, 251, 235) # Marfil
        self.set_draw_color(245, 158, 11)
        self.multi_cell(0, 4, f"[QUÉ PROYECTAR EN PANTALLA]: {text}", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def speech_text(self, text):
        self.set_x(15)
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(229, 231, 235)
        self.set_font(self.font_family_name, '', 8)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 4, f'"{text}"', border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.5)

    def transition_cue(self, text):
        self.set_x(15)
        self.set_font(self.font_family_name, 'I', 7.5)
        self.set_text_color(3, 105, 161) # Azul enlace
        self.cell(0, 4, f"-> Pase de voz: {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def question_box(self, q_num, question, answer):
        self.set_x(15)
        self.set_font(self.font_family_name, 'B', 8)
        self.set_text_color(120, 53, 15)
        self.set_fill_color(254, 243, 199)
        self.set_draw_color(217, 119, 6)
        self.cell(0, 5, f"[?] Pregunta {q_num}: {question}", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_x(15)
        self.set_font(self.font_family_name, '', 7.8)
        self.set_text_color(40, 45, 55)
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(229, 231, 235)
        self.multi_cell(0, 3.8, f"Respuesta blindada: {answer}", border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)


def generar_pdf():
    pdf = Guion5PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # TÍTULO PRINCIPAL
    pdf.set_font(pdf.font_family_name, 'B', 14)
    pdf.set_text_color(120, 53, 15)
    pdf.cell(0, 7.5, "GUION OFICIAL DE EXPOSICIÓN — 5 INTEGRANTES", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    
    pdf.set_font(pdf.font_family_name, 'B', 10)
    pdf.set_text_color(75, 85, 99)
    pdf.cell(0, 5, "AuditPIMS 2.0: Agente de Evidencia y Auditoría de Sistemas", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    
    pdf.set_font(pdf.font_family_name, '', 7.5)
    pdf.set_text_color(107, 114, 128)
    pdf.cell(0, 4, "Curso: Auditoría de Sistemas (UNSA 2026) | Docente: Edward Vicente Zarate Carlos", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.cell(0, 4, "Grupo 4: Bernahola Vilca, Contreras Huamani, Soncco Mamani, Velasque Arcos, Quispe Madariaga", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(2)

    # REGLA DE ORO DE LA PRESENTACIÓN
    pdf.set_fill_color(254, 242, 242)
    pdf.set_draw_color(239, 68, 68)
    pdf.set_font(pdf.font_family_name, 'B', 7.5)
    pdf.set_text_color(153, 27, 27)
    estrategia = (
        "REGLA DE ORO DE PRESENTACIÓN (Show me the code):\n"
        "• CERO diapositivas de texto aburrido en PowerPoint. Toda la exposición se apoya en el Dashboard Web en vivo "
        "(http://localhost:8000) y el repositorio público en GitHub (https://github.com/Piero-design/AuditPIMS).\n"
        "• Tiempo total estricto: 6:00 minutos (1:10 min por integrante aprox). Mantener sincronización fluida."
    )
    pdf.multi_cell(0, 3.8, estrategia, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    # ---------------------------------------------------------
    # INTEGRANTE 1
    # ---------------------------------------------------------
    pdf.speaker_header("PARTE 1", "INTEGRANTE 1", "Introducción, Problema y Rol en el Salón", "1:10 min")
    pdf.screen_cue("Proyectar la página principal del Dashboard Web (http://localhost:8000) o el README de GitHub.")
    pdf.speech_text(
        "Buenos días profesor, buenos días compañeros. Somos el Grupo 4 y presentamos nuestro proyecto: "
        "AuditPIMS 2.0: Agente de Evidencia y Auditoría de Sistemas.\n\n"
        "En la implementación de un Sistema de Gestión de Privacidad de la Información (PIMS), el mayor dolor de "
        "cabeza no es redactar políticas en un papel, sino demostrar con evidencias objetivas que esos controles "
        "se cumplen en el día a día sin caer en subjetividades humanas.\n\n"
        "Tradicionalmente, la auditoría se hace de forma manual, lenta y fatigante: un auditor tarda días revisando "
        "contratos, y suele cometer errores graves como asumir que si un documento dice 'cumplimos el RGPD en 72 horas' "
        "está bien, desconociendo la ley peruana.\n\n"
        "En el ecosistema multiagente de este curso, nuestro grupo cumple el rol de Agente Juez y Auditor Interno: "
        "nuestro sistema está diseñado para auditar y emitir dictámenes periciales sobre los artefactos que produzcan "
        "los otros 7 grupos del salón."
    )
    pdf.transition_cue("A continuación, mi compañero [Nombre Integrante 2] detallará el marco normativo estricto del agente.")

    # ---------------------------------------------------------
    # INTEGRANTE 2
    # ---------------------------------------------------------
    pdf.speaker_header("PARTE 2", "INTEGRANTE 2", "Marco Normativo Dual (ISO 27701 y D.S. 016-2024-JUS)", "1:10 min")
    pdf.screen_cue("Señalar en el encabezado del Dashboard los badges normativos (ISO 27701:2025 y Ley 29733 - 48h).")
    pdf.speech_text(
        "Gracias. Para garantizar rigor técnico y legal, nuestro agente se fundamenta en dos marcos vigentes:\n\n"
        "1. ISO/IEC 27701:2025 (2.ª edición): Cuya principal revolución técnica es que ahora es un estándar "
        "completamente independiente y certificable por sí mismo, sin requerir previamente ISO 27001. Nuestro agente "
        "tiene estructurados sus 52 controles para Responsables (RT) y Encargados (EN) del tratamiento.\n\n"
        "2. El Marco Legal Peruano: La Ley N.º 29733 y su nuevo Reglamento aprobado mediante el D.S. N.º 016-2024-JUS, "
        "vigente desde marzo de 2025.\n\n"
        "Aquí el agente aplica una regla de negocio crítica: muchas organizaciones copian plantillas europeas del "
        "RGPD que dan 72 horas para notificar fugas de datos. En el Perú, el nuevo reglamento exige de forma perentoria "
        "un plazo máximo de 48 horas ante la ANPDP. Si el agente detecta que un procedimiento fija 72 horas, "
        "dictamina automáticamente una No Conformidad Mayor."
    )
    pdf.transition_cue("Doy el pase a mi compañero [Nombre Integrante 3] para explicar la arquitectura técnica de software.")

    # ---------------------------------------------------------
    # INTEGRANTE 3
    # ---------------------------------------------------------
    pdf.speaker_header("PARTE 3", "INTEGRANTE 3", "Arquitectura, Criptografía SHA-256 y la Skill", "1:10 min")
    pdf.screen_cue("Proyectar el Diagrama de Arquitectura en Capas en GitHub o la carpeta 'auditoria-evidencias-pims'.")
    pdf.speech_text(
        "Gracias. El reto técnico de este Hito fue pasar de un prompt improvisado de ChatGPT a una arquitectura "
        "de software agéntica y reutilizable, sustentada en tres componentes:\n\n"
        "1. Cadena de Custodia Criptográfica (SHA-256): Antes de que un documento pase a la IA, el sistema ejecuta código "
        "Python para calcular el hash criptográfico SHA-256 del archivo físico en memoria. Esto garantiza la integridad y "
        "el no repudio que exige el Control A.3.14 de ISO 27701; si la evidencia es alterada un solo byte, la auditoría lo detecta.\n\n"
        "2. La Skill Modular (auditoria-evidencias-pims): Contiene los 52 controles y evalúa las evidencias aplicando de manera "
        "paramétrica los 6 criterios formales de auditoría de ISO 19011:2018: Pertinencia, Suficiencia, Vigencia, "
        "Aprobación, Trazabilidad y Completitud.\n\n"
        "3. Motor de IA Agnóstico: Nuestro backend en FastAPI puede conectarse a modelos en la nube como Gemini, o conectarse "
        "localmente a las GPUs del laboratorio de la universidad vía Ollama, garantizando soberanía de datos y confidencialidad total."
    )
    pdf.transition_cue("Siguiendo el principio de 'Talk is cheap. Show me the code', mi compañero Piero realizará la demo en vivo.")

    # Salto de página para Integrante 4 y 5
    pdf.add_page()

    # ---------------------------------------------------------
    # INTEGRANTE 4 (PIERO)
    # ---------------------------------------------------------
    pdf.speaker_header("PARTE 4", "INTEGRANTE 4 (Piero Bernahola)", "Demostración en Vivo en el Dashboard", "1:30 min")
    pdf.screen_cue("Tener abierto http://localhost:8000 en el navegador. Realizar la carga y clic en vivo.")
    pdf.speech_text(
        "Gracias. Como pueden ver en pantalla, este es el Dashboard de AuditPIMS 2.0, desarrollado en FastAPI con una "
        "interfaz ejecutiva cálida en tonos blanco y ámbar, diseñada para auditoría formal.\n\n"
        "(Acción: Seleccionar el Contrato Telecall en el menú)\n"
        "Vamos a auditar en vivo el Contrato de Locación de Servicios con Telecall Perú S.A. Observen cómo en la esquina "
        "inferior izquierda el sistema ya calculó su huella digital criptográfica SHA-256 (0748853a...). La evidencia queda sellada.\n\n"
        "(Acción: Clic en el botón naranja 'Evaluar con IA Agéntica')\n"
        "Presionamos 'Evaluar'. En menos de 2 segundos, el agente cotejó el contrato contra la Skill y la legislación peruana:\n"
        "• Dictaminó automáticamente: NO CONFORMIDAD MAYOR.\n"
        "• En la cuadrícula superior evaluó los 6 criterios de ISO 19011: marcó Aprobación = NO, porque el contrato tiene las "
        "líneas de firma en blanco; es un borrador no perfeccionado.\n"
        "• Detectó que no existe un Acuerdo de Tratamiento de Datos (DPA) formal y que la confidencialidad solo protegía tarifas "
        "comerciales, dejando totalmente desprotegidos los datos de los alumnos y postulantes.\n"
        "• Cita textualmente las desviaciones y emite recomendaciones de mitigación inmediatas."
    )
    pdf.transition_cue("Le doy el pase a mi compañero [Nombre Integrante 5] para explicar la gobernanza y la integración multiagente.")

    # ---------------------------------------------------------
    # INTEGRANTE 5
    # ---------------------------------------------------------
    pdf.speaker_header("PARTE 5", "INTEGRANTE 5", "Gobernanza HITL, Protocolo Multiagente y Cierre", "1:10 min")
    pdf.screen_cue("Piero hace clic en 'Validar & Firmar', luego cambia a pestaña 'Matriz SOA' y muestra '/docs'.")
    pdf.speech_text(
        "Gracias. Un principio ético y técnico fundamental de nuestro sistema es la gobernanza Human-in-the-Loop (HITL):\n\n"
        "La Inteligencia Artificial realiza el triaje exhaustivo y propone el hallazgo, pero la validez legal siempre requiere "
        "supervisión humana. Como ven en pantalla, el Auditor Líder presiona el botón 'Validar & Firmar (HITL)', sellando "
        "electrónicamente el dictamen aprobado.\n\n"
        "(Piero cambia a la pestaña 'Matriz SOA')\n"
        "En el Modo M3, todos los hallazgos alimentan automáticamente la Matriz de Aplicabilidad (SOA) con los 52 controles, "
        "calculando la tasa de cumplimiento del PIMS en tiempo real.\n\n"
        "(Piero cambia a la pestaña 'Integración Multiagente' o abre /docs)\n"
        "Por último, para integrarnos con los otros 7 grupos del salón, tenemos expuesto el endpoint POST /api/auditar y la "
        "documentación interactiva Swagger. Cualquier grupo puede enviarnos un documento en formato JSON y nuestro agente "
        "le devolverá el dictamen pericial estructurado en segundos.\n\n"
        "Todo el código fuente y las pruebas están disponibles públicamente en nuestro repositorio de GitHub. "
        "Muchas gracias profesor, quedamos listos para sus preguntas."
    )
    pdf.ln(1)

    # BANCO DE PREGUNTAS TRAMPA
    pdf.set_font(pdf.font_family_name, 'B', 10.5)
    pdf.set_text_color(120, 53, 15)
    pdf.cell(0, 6, "BANCO DE PREGUNTAS TRAMPA DEL DOCENTE (Y CÓMO RESPONDER)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    pdf.question_box(
        "1", 
        "¿Por qué no usar simplemente ChatGPT o NotebookLM en lugar de programar esto?",
        "NotebookLM es una herramienta pasiva de lectura sin herramientas digitales. Nuestro agente es un sistema de software activo: calcula hashes SHA-256 para custodia pericial (A.3.14), aplica reglas deterministas bajo ISO 19011 (sin alucinaciones complacientes), expone una API REST para conectarse con los otros 7 grupos y guarda trazabilidad para auditoría continua en producción."
    )

    pdf.question_box(
        "2",
        "¿Por qué crearon identificadores propios como CL-04, RT-15, SG-04 y no los números exactos de la norma?",
        "Por respeto al copyright internacional de la norma ISO/IEC 27701:2025 y por claridad arquitectónica: agrupamos los controles por roles funcionales de auditoría: CL para Cláusulas del sistema, RT para Responsables del tratamiento, EN para Encargados y SG para Seguridad compartida."
    )

    pdf.question_box(
        "3",
        "¿La Inteligencia Artificial va a reemplazar al auditor humano?",
        "No. Nuestro diseño se rige estrictamente por el principio Human-in-the-Loop (HITL). La IA procesa en segundos los 52 controles y detecta faltantes con precisión, pero la aprobación final, la calificación de severidad y la emisión del dictamen oficial siempre las valida y firma el auditor humano desde el panel."
    )

    pdf.question_box(
        "4",
        "¿Por qué afirman que un procedimiento con 72 horas es una No Conformidad Mayor?",
        "Porque bajo el D.S. N.º 016-2024-JUS (nuevo reglamento de la Ley 29733 vigente desde marzo 2025), el plazo legal imperativo en el Perú para notificar brechas de seguridad a la ANPDP es de 48 horas. Las 72 horas corresponden al RGPD europeo. Copiar normas foráneas en territorio peruano expone a la empresa a multas graves de la autoridad."
    )

    pdf.question_box(
        "5",
        "¿Dónde podemos revisar el código y los endpoints de su agente?",
        "El proyecto está publicado como código abierto en GitHub: https://github.com/Piero-design/AuditPIMS con licencia académica, y los endpoints REST interactivos están documentados bajo estándar OpenAPI Swagger en /docs."
    )

    pdf.output(OUTPUT_PDF)
    print(f"✔ PDF generado exitosamente en: {OUTPUT_PDF}")

if __name__ == "__main__":
    generar_pdf()
