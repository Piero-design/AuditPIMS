#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del PDF Oficial:
GUION MAESTRO DE EXPOSICIÓN – HITO 1 (GRUPO 4)
AuditPIMS: Agente de Evidencia y Auditoría
Universidad Nacional de San Agustín (UNSA) - Auditoría de Sistemas 2026
"""

import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT_PDF = "/Users/piero.o/Downloads/SEMESTRE II - SISTEMAS/AUDITORIA/GUION_EXPOSICION_HITO1_GRUPO4.pdf"

class GuionPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(left=16, top=16, right=16)
        
        # Cargar fuentes del sistema Mac
        font_dir = '/System/Library/Fonts/Supplemental'
        if os.path.exists(os.path.join(font_dir, 'Arial.ttf')):
            self.add_font('ArialCustom', '', os.path.join(font_dir, 'Arial.ttf'))
            self.add_font('ArialCustom', 'B', os.path.join(font_dir, 'Arial Bold.ttf'))
            self.add_font('ArialCustom', 'I', os.path.join(font_dir, 'Arial Italic.ttf'))
            self.font_family_name = 'ArialCustom'
        else:
            self.font_family_name = 'Helvetica'

    def header(self):
        self.set_font(self.font_family_name, 'B', 8)
        self.set_text_color(100, 110, 120)
        self.cell(0, 5, "UNSA | ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS | AUDITORÍA DE SISTEMAS (2026)", 
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_font(self.font_family_name, 'I', 7.5)
        self.cell(0, 4, "TIF - Hito 1: AuditPIMS - Agente de Evidencia y Auditoría (Grupo 4)", 
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.set_draw_color(200, 210, 220)
        self.set_line_width(0.3)
        self.line(16, self.get_y() + 1, 194, self.get_y() + 1)
        self.ln(4)

    def footer(self):
        self.set_y(-12)
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(130, 140, 150)
        self.set_draw_color(220, 225, 230)
        self.line(16, self.get_y() - 1, 194, self.get_y() - 1)
        self.cell(0, 6, f"Página {self.page_no()}/{{nb}} - AuditPIMS Grupo 4 (UNSA 2026)", align="C")

    def chapter_title(self, num_str, title_str):
        self.set_font(self.font_family_name, 'B', 12)
        self.set_text_color(15, 34, 64) # Navy azul
        self.set_fill_color(240, 244, 250)
        self.cell(0, 8, f"  {num_str}. {title_str}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(2)

    def section_subtitle(self, text):
        self.set_font(self.font_family_name, 'B', 10)
        self.set_text_color(30, 70, 130)
        self.cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def speech_box(self, label, text):
        self.set_fill_color(248, 250, 252)
        self.set_draw_color(210, 220, 235)
        self.set_font(self.font_family_name, 'B', 8.5)
        self.set_text_color(15, 75, 140)
        self.cell(0, 5, f"[DISCURSO] {label}:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font(self.font_family_name, '', 8.5)
        self.set_text_color(40, 45, 55)
        
        # Rectángulo contenedor
        self.multi_cell(0, 4.2, f'"{text}"', border=1, fill=True)
        self.ln(2)

    def instruction_box(self, text):
        self.set_font(self.font_family_name, 'B', 8)
        self.set_text_color(140, 70, 10)
        self.set_fill_color(255, 250, 240)
        self.multi_cell(0, 4.5, f"[PANTALLA] {text}", border=1, fill=True)
        self.ln(2)

    def code_box(self, code_text):
        self.set_font("Courier", "B", 8)
        self.set_text_color(20, 80, 20)
        self.set_fill_color(240, 250, 240)
        self.set_draw_color(180, 220, 180)
        self.multi_cell(0, 4.2, code_text, border=1, fill=True)
        self.ln(2)

def compilar_pdf():
    pdf = GuionPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Título Principal
    pdf.set_font(pdf.font_family_name, 'B', 16)
    pdf.set_text_color(15, 34, 64)
    pdf.cell(0, 9, "GUION MAESTRO DE EXPOSICIÓN – HITO 1", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    
    pdf.set_font(pdf.font_family_name, 'B', 11)
    pdf.set_text_color(70, 85, 105)
    pdf.cell(0, 6, "AuditPIMS: Agente de Evidencia y Auditoría", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    
    pdf.set_font(pdf.font_family_name, '', 8.5)
    pdf.set_text_color(100, 110, 120)
    pdf.cell(0, 5, "Docente: Edward Vicente Zarate Carlos | Grupo 4: Bernahola, Contreras, Soncco, Velasque, Quispe", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(3)

    # Bloque de Estrategia
    pdf.set_fill_color(245, 247, 250)
    pdf.set_draw_color(200, 210, 225)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(15, 34, 64)
    estrategia = (
        "ESTRATEGIA 'SHOW ME THE CODE' (Linus Torvalds): Cero diapositivas aburridas. "
        "Se proyecta el Informe Técnico en PDF y la terminal de VS Code ejecutando la IA en vivo. "
        "Todo el equipo domina este guion para alternar o apoyarse con total naturalidad."
    )
    pdf.multi_cell(0, 4.5, estrategia, border=1, fill=True)
    pdf.ln(4)

    # 1. PARTE 1
    pdf.chapter_title("1", "INTRODUCCIÓN, PROBLEMA Y MARCO NORMATIVO (0:00 - 1:30 min)")
    pdf.instruction_box("QUÉ PROYECTAR EN PANTALLA: Abrir el PDF del Informe Técnico en las páginas 2 y 3.")
    pdf.speech_box(
        "QUÉ DECIR EN LA EXPOSICIÓN",
        "Buenos días profesor. Somos el Grupo 4 y nuestro proyecto es AuditPIMS: Agente de Evidencia y Auditoría.\n\n"
        "En un Sistema de Gestión de Privacidad de la Información (PIMS), el mayor cuello de botella no es redactar políticas, sino demostrar con evidencias objetivas que los controles se cumplen en el día a día.\n\n"
        "Para este Hito 1, nos fundamentamos en dos marcos normativos estrictamente vigentes:\n"
        "1. La nueva norma ISO/IEC 27701:2025 (2.ª edición, octubre 2025): que ahora es un estándar independiente y certificable por sí mismo sin exigir antes ISO 27001.\n"
        "2. El marco legal peruano obligatorio: la Ley N.º 29733 y su nuevo Reglamento aprobado mediante el D.S. N.º 016-2024-JUS (vigente desde marzo de 2025), que introduce exigencias como la notificación de brechas en 48 horas y el Oficial de Datos Personales."
    )

    # 2. PARTE 2
    pdf.chapter_title("2", "DE PROMPT A SKILL MODULAR (1:30 - 3:00 min)")
    pdf.instruction_box("QUÉ PROYECTAR: Mostrar la estructura de carpetas en VS Code: auditoria-evidencias-pims (SKILL.md, references y assets).")
    pdf.speech_box(
        "QUÉ DECIR EN LA EXPOSICIÓN",
        "El primer reto técnico del Hito 1 fue transformar la tarea: pasar de un prompt improvisado a una skill estructurada y reutilizable.\n\n"
        "Si un auditor usa un prompt suelto en ChatGPT como 'Revisa esta política y dime si cumple ISO 27701', el modelo comete fallas graves: responde con generalidades, no cita fragmentos probatorios, no distingue si la empresa es Responsable o Encargada, y cada vez usa criterios distintos. No es auditable.\n\n"
        "Para solucionarlo, construimos la skill 'auditoria-evidencias-pims', compuesta por:\n"
        "• SKILL.md: Define el trigger semántico y 3 Modos: M1 (Planificar checklist), M2 (Evaluar con 6 criterios de ISO 19011) y M3 (Consolidar matriz e informe).\n"
        "• Carpeta references/: Base de conocimiento modular con 52 controles (CL, RT, EN, SG), criterios de evaluación y el resumen de la Ley 29733.\n"
        "• Carpeta assets/: Plantillas formales de matriz de evidencias e informe de hallazgos."
    )

    pdf.add_page()

    # 3. PARTE 3
    pdf.chapter_title("3", "DEMOSTRACION EN VIVO - 'SHOW ME THE CODE' (3:00 - 5:30 min)")
    pdf.instruction_box("QUE PROYECTAR: Compartir la Terminal integrada de VS Code ejecutando el script con IA real.")

    pdf.section_subtitle("> Caso 1: Deteccion de Falla Legal Critica (Evidencia E6)")
    pdf.code_box("python3 auditor_con_ia.py --evaluar E6")
    pdf.speech_box(
        "QUE EXPLICAR MIENTRAS LA IA RESPONDE",
        "Aqui auditamos el Procedimiento de Incidentes (E6). Fijense como la IA evalua los 6 criterios de ISO 19011 citando el texto y detecta la falla legal mas critica:\n"
        "El procedimiento de la empresa fijaba 72 horas para reportar brechas a la autoridad (copiando el RGPD europeo). La skill detecta inmediatamente que bajo el D.S. 016-2024-JUS de Peru el plazo legal estricto es de 48 horas. Dictamina automaticamente No Conformidad Mayor, cita el requisito, la evidencia y la desviacion, y genera las recomendaciones correctivas."
    )

    pdf.section_subtitle("> Caso 2: Regla de Oro - 'Sin Evidencia no hay Conformidad' (Evidencia E8)")
    pdf.code_box("python3 auditor_con_ia.py --evaluar E8")
    pdf.speech_box(
        "QUE EXPLICAR MIENTRAS LA IA RESPONDE",
        "Probamos el control de cifrado en base de datos. Solo se presento una entrevista testimonial donde el Jefe de TI afirma: 'Las bases de datos en PostgreSQL estan totalmente cifradas'.\n"
        "Un chatbot comun diria 'Conforme'. Nuestra skill aplica la regla de oro: una declaracion verbal aislada carece de evidencia objetiva. Dictamina 'No Verificable' y exige configuraciones tecnicas y reportes reales."
    )

    pdf.section_subtitle("> Caso 3: Consolidacion Automatica de Matriz (Modo M3)")
    pdf.code_box("python3 probar_auditor.py --consolidar")
    pdf.speech_box(
        "QUE EXPLICAR",
        "En el Modo M3, la skill consolida las 8 evidencias evaluadas, genera la matriz con simbologia ISO (cumple, parcial, no cumple), calcula el porcentaje de conformidad y genera el plan de accion ordenado por severidad (30, 60 y 90 dias)."
    )

    # 4. PARTE 4
    pdf.chapter_title("4", "CONCLUSIONES Y SALTO AL HITO 2 (5:30 - 6:30 min)")
    pdf.speech_box(
        "QUE DECIR EN EL CIERRE",
        "En las pruebas alcanzamos un 87.5% de coincidencia con la clave de auditoria. La unica discrepancia en la evidencia E3 demostro que la skill fue incluso mas estricta que la clave, detectando vacios en plazos numericos.\n\n"
        "¿Que representa el Hito 1? Un Skill y un Asistente funcional que asiste al auditor humano.\n"
        "¿Que haremos en el Hito 2 (Proyecto Agentico)? Darle autonomia completa. Conectaremos herramientas MCP (Model Context Protocol) para que el agente inspeccione carpetas y bases de datos automaticamente, calcule hashes SHA-256 de integridad documental y audite de forma continua el PIMS.\n\n"
        "Muchas gracias, quedamos atentos a sus preguntas."
    )

    pdf.add_page()

    # 5. PREGUNTAS TRAMPA
    pdf.chapter_title("5", "BANCO DE PREGUNTAS TRAMPA DEL DOCENTE Y RESPUESTAS BLINDADAS")
    
    preguntas = [
        ("¿Por que crearon codigos propios como CL-04, RT-02, SG-04 y no los de la norma ISO oficial?",
         "Por dos motivos: primero, el texto integro de ISO/IEC 27701:2025 esta protegido por derechos de autor de ISO, por lo que creamos resumenes propios. Segundo, organizamos funcionalmente los roles: CL para Clausulas del sistema, RT para Responsables, EN para Encargados y SG para Seguridad compartida. Indicamos expresamente que son referenciales."),
        
        ("¿Por que una Skill y no un simple prompt largo en ChatGPT?",
         "Una Skill es arquitectura de software: tiene un archivo de metadatos (SKILL.md) con activacion semantica automatica, separacion modular de conocimiento en references/ (evita saturar la memoria de contexto), plantillas inmutables y reglas estrictas de no invencion."),
        
        ("¿Por que en la evidencia E3 el asistente dio 'No conformidad menor' si su clave decia 'Conforme'?",
         "Demostro el rigor del sistema. El documento de prueba PRO-ARCO-01 decia que responderia 'conforme a los plazos del reglamento', pero no ponia los dias habiles en numeros. Nuestro asistente aplico con rigor los criterios de Suficiencia y Completitud: sin plazos cuantificables no se puede auditar el servicio. La discrepancia fue un aporte de rigor valido."),
        
        ("¿Que le falta a este Hito 1 para ser verdaderamente un Agente (Hito 2)?",
         "Le falta autonomia de ejecucion y herramientas externas (MCP). En el Hito 1 requiere que un humano le entregue el documento. En el Hito 2 tendra un bucle continuo: inspeccionara carpetas o bases de datos por si solo, calculara hashes SHA-256 de integridad para cumplir con el control A.3.14 y emitira alertas continuas."),
        
        ("¿Como evitan que la IA alucine o invente cumplimientos?",
         "Con las 7 Reglas Obligatorias: (1) Sin evidencia no hay conformidad, (2) Citar siempre textualmente la evidencia, (3) No inventar datos inexistentes, y (4) La decision final siempre recae en el auditor humano.")
    ]

    for p, r in preguntas:
        pdf.set_font(pdf.font_family_name, 'B', 8.5)
        pdf.set_text_color(160, 30, 30)
        pdf.cell(0, 5, f"[?] {p}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font(pdf.font_family_name, '', 8)
        pdf.set_text_color(35, 40, 50)
        pdf.set_fill_color(250, 252, 255)
        pdf.multi_cell(0, 4, f"[RESPUESTA]: {r}", border=1, fill=True)
        pdf.ln(2)

    # 6. TABLA RESUMEN DE EVIDENCIAS
    pdf.chapter_title("6", "TABLA RESUMEN DEL BANCO DE EVIDENCIAS (E1 a E8)")
    pdf.set_font(pdf.font_family_name, 'B', 7.5)
    pdf.set_fill_color(230, 235, 245)
    pdf.set_text_color(15, 34, 64)
    
    # Cabecera tabla
    pdf.cell(10, 6, "ID", border=1, align="C", fill=True)
    pdf.cell(50, 6, "Evidencia", border=1, align="L", fill=True)
    pdf.cell(16, 6, "Control", border=1, align="C", fill=True)
    pdf.cell(62, 6, "Falla Sembrada", border=1, align="L", fill=True)
    pdf.cell(40, 6, "Dictamen", border=1, align="C", fill=True)
    pdf.ln()

    datos = [
        ("E1", "Política de Privacidad v1.0", "CL-04", "Aprobada en 2021; cita D.S. 003 derogado; sin ODP", "No conformidad menor"),
        ("E2", "Registro Consentimientos CRM", "RT-02", "4 de 12 sin fecha ni canal; datos sin anonimizar", "No conformidad mayor"),
        ("E3", "Procedimiento Derechos ARCO", "RT-07", "Sin plazos numéricos explícitos ni registros", "NC menor (Rigor IA)"),
        ("E4", "Acta de Capacitación PIMS", "CL-09", "Asistencia 96% pero sin evaluar efectividad", "Oportunidad de mejora"),
        ("E5", "Contrato Proveedor Call Center", "RT-15", "Sin cláusulas DPA ni de seguridad; firmas vacías", "No conformidad mayor"),
        ("E6", "Procedimiento de Incidentes", "SG-04", "Borrador; fija 72h frente a 48h del D.S. 016", "No conformidad mayor"),
        ("E7", "Inventario Tratamientos RoPA", "CL-12", "Lista 5 de 8 procesos; 2 sin base legal", "No conformidad menor"),
        ("E8", "Entrevista al Jefe de TI", "SG-02", "Declaración verbal sin soporte técnico alguno", "No verificable")
    ]

    pdf.set_font(pdf.font_family_name, '', 7)
    pdf.set_text_color(30, 35, 45)
    for row in datos:
        pdf.cell(10, 5, row[0], border=1, align="C")
        pdf.cell(50, 5, row[1][:32], border=1, align="L")
        pdf.cell(16, 5, row[2], border=1, align="C")
        pdf.cell(62, 5, row[3][:42], border=1, align="L")
        pdf.cell(40, 5, row[4], border=1, align="C")
        pdf.ln()

    pdf.output(OUTPUT_PDF)
    print(f"PDF generado con éxito en: {OUTPUT_PDF}")

if __name__ == "__main__":
    compilar_pdf()
