#!/usr/bin/env python3
"""
AuditPIMS - Agente de Evidencia y Auditoría (CLI Demo)
ISO/IEC 27701:2025 | ISO 19011:2018 | Ley 29733 (D.S. 016-2024-JUS)
Grupo 4 - Universidad Nacional de San Agustín (UNSA)
"""

import sys
import argparse
from pathlib import Path

# Colores ANSI para terminal
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

# Banco de evidencias de prueba de "Organización Ejemplo S.A.C."
EVIDENCIAS_PRUEBA = {
    "E1": {
        "codigo": "E1",
        "nombre": "Política de Privacidad (POL-PRI-01 v1.0)",
        "tipo": "Política interna",
        "control": "CL-04 – Política de Privacidad del PIMS",
        "rol": "Responsable",
        "texto": (
            "POLÍTICA DE PRIVACIDAD - Organización Ejemplo S.A.C. Versión 1.0 (Aprobada en marzo 2021).\n"
            "Alcance: Tratamiento de datos de alumnos y docentes de cursos virtuales.\n"
            "Marco Legal: En estricto cumplimiento del Reglamento de la Ley 29733 aprobado mediante D.S. 003-2013-JUS.\n"
            "Revisión: Esta política se revisará cuando la gerencia lo considere conveniente.\n"
            "Atención: Para ejercer sus derechos escribir a contacto@ejemplo.pe. No se cuenta con Oficial de Datos Personales."
        ),
        "falla_esperada": "Aprobada en 2021, nunca revisada; cita reglamento derogado (D.S. 003-2013-JUS); no menciona al ODP.",
        "criterios": {
            "Pertinencia": ("Sí", "Aborda los compromisos generales de privacidad de la organización."),
            "Suficiencia": ("Sí", "Define principios y compromisos básicos de privacidad."),
            "Vigencia": ("No", "Aprobada en 2021 sin revisiones; cita norma derogada (D.S. 003-2013-JUS en vez de D.S. 016-2024-JUS)."),
            "Aprobación": ("Parcial", "Menciona 'Aprobada en marzo 2021' pero carece de firma o cargo responsable."),
            "Trazabilidad": ("Parcial", "Tiene código POL-PRI-01 v1.0, pero sin historial formal de versiones."),
            "Completitud": ("No", "Omite la designación del Oficial de Datos Personales exigida por el nuevo reglamento.")
        },
        "resultado": "No conformidad menor",
        "hallazgo": "Requisito: Mantener la política de privacidad actualizada y alineada a la normativa vigente (CL-04; D.S. 016-2024-JUS). Evidencia: POL-PRI-01 v1.0 data de 2021 y cita el D.S. 003-2013-JUS. Desviación: La política está desactualizada frente al marco normativo vigente desde el 30/03/2025.",
        "base_legal": "Ley 29733 y D.S. N.º 016-2024-JUS (Seguridad y Gobernanza).",
        "recomendacion": "Actualizar la política, adecuarla al D.S. 016-2024-JUS, formalizar la figura del Oficial de Datos Personales y fijar ciclo anual de revisión.",
        "evidencia_adicional": "Nueva versión aprobada por Gerencia General con firma del ODP."
    },
    "E2": {
        "codigo": "E2",
        "nombre": "Registro de Consentimientos de Marketing (REG-CON-01)",
        "tipo": "Registro de base de datos",
        "control": "RT-02 – Demostración del Consentimiento",
        "rol": "Responsable",
        "texto": (
            "REGISTRO CRM MARKETING - Organización Ejemplo S.A.C.\n"
            "Muestra evaluada: 12 titulares registrados en campañas web y telefónicas.\n"
            "Filas 1-2, 4-6, 8, 10, 12: Fecha, canal web (checkbox log) y hash de términos aceptados v2.\n"
            "Filas 3, 7, 9, 11: Registros migrados de base antigua. Campos 'Fecha_Consentimiento', 'Canal_Captación' y 'Versión_Aviso' están en blanco (NULL).\n"
            "Nota de privacidad: Contiene DNI y teléfonos reales en archivo original sin anonimizar."
        ),
        "falla_esperada": "4 de 12 titulares sin constancia de fecha ni canal; contiene datos personales sin anonimizar.",
        "criterios": {
            "Pertinencia": ("Sí", "Demuestra el registro de consentimientos para prospección comercial."),
            "Suficiencia": ("No", "33% de la muestra (4/12) no acredita consentimiento válido ni previo."),
            "Vigencia": ("Sí", "Registros correspondientes al periodo auditado (2025-2026)."),
            "Aprobación": ("No", "Extracción de base de datos sin firma ni certificación de extracción."),
            "Trazabilidad": ("Parcial", "Trazable para 8 titulares; nula trazabilidad para los 4 registros históricos."),
            "Completitud": ("No", "Faltan campos obligatorios: fecha, mecanismo y texto informativo aceptado.")
        },
        "resultado": "No conformidad mayor",
        "hallazgo": "Requisito: El responsable debe demostrar que el titular otorgó consentimiento libre, previo, expreso e informado (RT-02; Ley 29733 art. 13). Evidencia: En REG-CON-01, 4 de 12 titulares carecen de fecha y canal. Desviación: Tratamiento comercial sin prueba de consentimiento legal.",
        "base_legal": "Ley 29733, Arts. 5 (Principio de Consentimiento) y 13.",
        "recomendacion": "Bloquear temporalmente los 4 registros de campañas de marketing hasta obtener ratificación del consentimiento o depurarlos de la base.",
        "evidencia_adicional": "Logs de trazabilidad del CRM o correo de reconfirmación de consentimiento."
    },
    "E3": {
        "codigo": "E3",
        "nombre": "Procedimiento de Derechos ARCO (PRO-ARCO-01 v2.0)",
        "tipo": "Procedimiento operativo",
        "control": "RT-07 – Mecanismos para Ejercicio de Derechos del Titular",
        "rol": "Responsable",
        "texto": (
            "PROCEDIMIENTO DE DERECHOS ARCO - PRO-ARCO-01 v2.0 (Enero 2026).\n"
            "Elaborado por: Asesoría Legal. Aprobado por: Gerente de Operaciones.\n"
            "Flujo: Recepción vía formulario web o correo arco@ejemplo.pe.\n"
            "Plazos: 'Las solicitudes serán respondidas conforme a los plazos previstos en el reglamento vigente'.\n"
            "Registro: Se mantendrá un archivo Excel con correlativo, titular y tipo de derecho solicitado."
        ),
        "falla_esperada": "Documento control (teóricamente conforme, pero en auditoría se observó falta de plazos explícitos y registro vacío).",
        "criterios": {
            "Pertinencia": ("Sí", "Define el procedimiento para atender acceso, rectificación, cancelación y oposición."),
            "Suficiencia": ("Parcial", "Describe el procedimiento pero no adjunta expedientes ni registros de atención real."),
            "Vigencia": ("Sí", "Emitido en enero 2026, plenamente vigente."),
            "Aprobación": ("Sí", "Consta elaboración por Legal y aprobación por Gerencia de Operaciones."),
            "Trazabilidad": ("Sí", "Código formal, versión 2.0 y control de cambios documental."),
            "Completitud": ("Parcial", "Remite genéricamente a 'plazos del reglamento' sin detallar días hábiles específicos.")
        },
        "resultado": "No conformidad menor",
        "hallazgo": "Requisito: Procedimiento documentado con plazos operacionales claros (RT-07; D.S. 016-2024-JUS). Evidencia: PRO-ARCO-01 v2.0 omite fijar plazos numéricos para medir el cumplimiento del servicio. Desviación: Dificulta la medición objetiva del cumplimiento de plazos legales.",
        "base_legal": "Ley 29733 art. 19 y Reglamento D.S. 016-2024-JUS.",
        "recomendacion": "Incorporar en el procedimiento la tabla explícita de plazos de respuesta en días hábiles y formatos de expedientes.",
        "evidencia_adicional": "Expedientes de atención ARCO tramitados en el último semestre."
    },
    "E4": {
        "codigo": "E4",
        "nombre": "Acta de Capacitación en Protección de Datos",
        "tipo": "Registro / Acta",
        "control": "CL-09 – Competencia y Concienciación",
        "rol": "Responsable",
        "texto": (
            "ACTA DE CAPACITACIÓN - Organización Ejemplo S.A.C.\n"
            "Fecha: 15 de febrero de 2026. Tema: 'Protección de Datos y Nuevas Exigencias D.S. 016-2024-JUS'.\n"
            "Instructor: Consultor Externo certificado en PIMS.\n"
            "Asistencia: 24 de 25 colaboradores del área administrativa y académica (96% de asistencia).\n"
            "Evaluación: No se aplicó prueba de conocimientos ni encuesta de efectividad posterior."
        ),
        "falla_esperada": "Asistencia completa registrada, pero carece de evaluación de efectividad.",
        "criterios": {
            "Pertinencia": ("Sí", "Acredita actividades de sensibilización al personal con acceso a PII."),
            "Suficiencia": ("Parcial", "Demuestra asistencia pero no la adquisición real de competencias."),
            "Vigencia": ("Sí", "Ejecutada en febrero 2026."),
            "Aprobación": ("Sí", "Firmada por instructor y responsable de Recursos Humanos."),
            "Trazabilidad": ("Sí", "Lista de asistencia con nombres, DNI y firmas individuales."),
            "Completitud": ("Parcial", "Falta el instrumento de evaluación de eficacia de la formación.")
        },
        "resultado": "Oportunidad de mejora",
        "hallazgo": "Requisito: Evaluar la eficacia de las acciones de formación en privacidad (CL-09; ISO 27701 cláusula 7.2). Evidencia: Acta de capacitación con 96% de asistencia sin medición de aprendizaje. Desviación: Se cumplió con impartir la charla pero no se midió la asimilación del conocimiento.",
        "base_legal": "ISO/IEC 27701:2025 Cláusula 7.2 y Ley 29733.",
        "recomendacion": "Implementar un test corto post-capacitación y un seguimiento semestral de incidentes atribuibles a error humano.",
        "evidencia_adicional": "Resultados de encuestas o evaluaciones de desempeño en privacidad."
    },
    "E5": {
        "codigo": "E5",
        "nombre": "Contrato de Prestación de Servicios Call Center",
        "tipo": "Contrato comercial",
        "control": "RT-15 – Relaciones con Encargados del Tratamiento",
        "rol": "Responsable",
        "texto": (
            "CONTRATO DE SERVICIOS DE TELEVENDEDORES - Organización Ejemplo S.A.C. y TeleCall Perú S.A.\n"
            "Objeto: Gestión de cobranza y prospección de matrículas mediante acceso a base de datos de alumnos.\n"
            "Cláusula 8 (Confidencialidad): 'Las partes guardarán secreto de la información comercial'.\n"
            "Vacíos: No se estipulan instrucciones vinculantes, medidas de seguridad técnicas, régimen de subcontratación, deber de notificación de brechas ni destino final de los datos tras culminar el servicio.\n"
            "Firmas: Las líneas de firma de ambas partes se encuentran en blanco (sin firmar)."
        ),
        "falla_esperada": "Sin cláusulas obligatorias de encargo de tratamiento y firmas en blanco.",
        "criterios": {
            "Pertinencia": ("Sí", "Regula la relación comercial con un tercero que procesa datos personales."),
            "Suficiencia": ("No", "Carece de las cláusulas contractuales obligatorias para encargados."),
            "Vigencia": ("No", "Documento en borrador, sin vigencia legal ejecutoria."),
            "Aprobación": ("No", "Líneas de firma vacías; no existe perfeccionamiento contractual."),
            "Trazabilidad": ("Parcial", "Código de contrato pero sin constancia de suscripción."),
            "Completitud": ("No", "Omite el 100% de exigencias del art. 30 del D.S. 016-2024-JUS.")
        },
        "resultado": "No conformidad mayor",
        "hallazgo": "Requisito: El tratamiento por encargo debe formalizarse por contrato con cláusulas mínimas de seguridad, confidencialidad, subcontratación y destrucción (RT-15; D.S. 016-2024-JUS art. 30). Evidencia: Contrato con TeleCall sin firmar y sin estipulaciones de protección de datos. Desviación: Transmisión de PII a terceros sin amparo contractual vinculante.",
        "base_legal": "Ley 29733 art. 16 y Reglamento D.S. 016-2024-JUS art. 30.",
        "recomendacion": "Suscribir de inmediato una adenda DPA (Data Processing Agreement) con las cláusulas tipo de la ANPD antes de continuar la transferencia de bases de datos.",
        "evidencia_adicional": "Adenda firmada digitalmente y constancia de auditoría al proveedor."
    },
    "E6": {
        "codigo": "E6",
        "nombre": "Procedimiento de Gestión de Incidentes (PRO-INC-01 v0.3)",
        "tipo": "Procedimiento de seguridad",
        "control": "SG-04 – Notificación y Respuesta a Brechas de Privacidad",
        "rol": "Responsable",
        "texto": (
            "PROCEDIMIENTO DE INCIDENTES DE PRIVACIDAD - Versión 0.3 (Borrador de trabajo).\n"
            "Objetivo: Responder ante fugas o accesos no autorizados a datos personales.\n"
            "Sección 4.2: 'En caso de incidente con impacto relevante, el Oficial de Seguridad notificará a la Autoridad Nacional de Protección de Datos Personales en un plazo máximo de 72 horas contadas desde su confirmación'.\n"
            "Anexos: El formulario REG-INC-01 (Registro de Incidentes) no se encuentra adjunto ni implementado."
        ),
        "falla_esperada": "Borrador sin aprobar; estipula 72h frente a las 48h obligatorias de la ley peruana.",
        "criterios": {
            "Pertinencia": ("Sí", "Corresponde directamente a la gestión y respuesta ante incidentes de PII."),
            "Suficiencia": ("No", "Es un borrador sin formato de registro ni simulacros de notificación."),
            "Vigencia": ("No", "Fija 72 horas copiando el RGPD europeo, contraviniendo el plazo de 48 horas de Perú."),
            "Aprobación": ("No", "Versión 0.3 sin firmas de aprobación formal."),
            "Trazabilidad": ("Parcial", "Versión de borrador sin registro en sistema documental oficial."),
            "Completitud": ("No", "Omite el registro de incidentes y fija un plazo ilegal.")
        },
        "resultado": "No conformidad mayor",
        "hallazgo": "Requisito: Notificar a la Autoridad Nacional de Protección de Datos Personales dentro del plazo legal de 48 horas (SG-04; D.S. 016-2024-JUS). Evidencia: PRO-INC-01 v0.3 fija un plazo de 72 horas y está sin aprobar. Desviación: Incumplimiento directo de la normativa legal peruana en materia de brechas de seguridad.",
        "base_legal": "D.S. N.º 016-2024-JUS (Obligación de notificación en 48 horas).",
        "recomendacion": "Corregir el procedimiento fijando el plazo de 48 horas, aprobarlo por Alta Dirección y poner en producción la bitácora de incidentes.",
        "evidencia_adicional": "Procedimiento v1.0 aprobado y constancia de difusión al equipo de TI/CISO."
    },
    "E7": {
        "codigo": "E7",
        "nombre": "Inventario de Tratamientos (INV-TRA-01 v1.1)",
        "tipo": "Registro / RoPA",
        "control": "CL-12 – Registro de Actividades de Tratamiento (RoPA)",
        "rol": "Responsable",
        "texto": (
            "REGISTRO DE BANCOS Y ACTIVIDADES DE TRATAMIENTO - INV-TRA-01 v1.1 (Actualizado dic 2025).\n"
            "Procesos declarados por la organización en su memoria anual: 8 procesos con PII.\n"
            "Procesos inventariados en el registro: 5 procesos (Admisión, Matrícula, Planillas, Marketing, Egresados).\n"
            "Bases legales: 3 procesos citan consentimiento/ejecución contractual; 2 procesos ('Cámaras de Seguridad' y 'Control de Visitas') no consignan base jurídica ni plazo de conservación."
        ),
        "falla_esperada": "Omite 3 procesos institucionales y 2 carecen de base legal explícita.",
        "criterios": {
            "Pertinencia": ("Sí", "Documento central de gobernanza y catálogo de tratamientos PIMS."),
            "Suficiencia": ("Parcial", "Incompleto: cubre 5 de los 8 tratamientos existentes en la entidad."),
            "Vigencia": ("Sí", "Fecha de revisión reciente (diciembre 2025)."),
            "Aprobación": ("Sí", "Aprobado por el Oficial de Datos Personales."),
            "Trazabilidad": ("Sí", "Código de registro, control de versiones y fechas."),
            "Completitud": ("No", "Faltan procesos y columnas esenciales de licitud y retención.")
        },
        "resultado": "No conformidad menor",
        "hallazgo": "Requisito: Identificar y documentar todas las actividades de tratamiento con su respectiva base jurídica (CL-12; ISO 27701 cláusula 6.1.2). Evidencia: INV-TRA-01 v1.1 omite 3 procesos y no indica base legal para videovigilancia. Desviación: Inventario parcial que vulnera el principio de legalidad.",
        "base_legal": "Ley 29733 art. 12 y D.S. 016-2024-JUS.",
        "recomendacion": "Completar los 3 procesos faltantes e incorporar las bases jurídicas (interés legítimo / cumplimiento legal) y plazos de supresión.",
        "evidencia_adicional": "Formularios de recolección de datos de videovigilancia y control de accesos."
    },
    "E8": {
        "codigo": "E8",
        "nombre": "Nota de Entrevista al Jefe de TI",
        "tipo": "Entrevista verbal",
        "control": "SG-02 – Cifrado y Salvaguardas Técnicas de PII",
        "rol": "Responsable",
        "texto": (
            "MINUTA DE REUNIÓN DE AUDITORÍA - 28/09/2026.\n"
            "Auditor: '¿Cómo garantizan la confidencialidad de la base de datos de postulantes?'.\n"
            "Jefe de TI: 'Las bases de datos en PostgreSQL están totalmente cifradas en reposo y en tránsito. Contamos con claves rotativas y respaldos diarios seguros. Todo el sistema está protegido y no hay riesgo de fuga.'\n"
            "Documentos de respaldo adjuntos: Ninguno. No se aportaron capturas de configuración, políticas de cifrado ni certificados SSL/TLS."
        ),
        "falla_esperada": "Mera declaración testimonial sin evidencia documental ni técnica verificable.",
        "criterios": {
            "Pertinencia": ("Parcial", "Trata sobre seguridad de la base de datos, pero sin datos técnicos."),
            "Suficiencia": ("No", "Una declaración verbal aislada no constituye evidencia objetiva según ISO 19011."),
            "Vigencia": ("Sí", "Entrevista realizada durante el periodo de auditoría."),
            "Aprobación": ("No", "No existe acta firmada por el entrevistado ratificando la declaración."),
            "Trazabilidad": ("No", "No existen logs, capturas ni reportes del motor de base de datos."),
            "Completitud": ("No", "Carece de todo elemento técnico probatorio.")
        },
        "resultado": "No verificable",
        "hallazgo": "Requisito: Demostrar la aplicación de medidas técnicas de cifrado de PII (SG-02; ISO 27701 cláusula 8). Evidencia: Nota testimonial del Jefe de TI sin soporte técnico. Desviación: Regla de oro: Sin evidencia no hay conformidad. La declaración verbal es insuficiente para dictaminar cumplimiento.",
        "base_legal": "D.S. N.º 016-2024-JUS (Medidas de seguridad técnicas obligatorias).",
        "recomendacion": "Solicitar la política de cifrado formal, captura de configuración de TDE/pgcrypto en PostgreSQL y certificado TLS del servidor.",
        "evidencia_adicional": "Reporte de auditoría de configuración de base de datos y matriz de roles de acceso."
    }
}

def banner():
    print(f"{Color.CYAN}{Color.BOLD}========================================================================{Color.RESET}")
    print(f"{Color.CYAN}{Color.BOLD}       AuditPIMS: Agente de Evidencia y Auditoría (CLI - Hito 1)       {Color.RESET}")
    print(f"{Color.BLUE}  ISO/IEC 27701:2025 | ISO 19011:2018 | Ley 29733 (D.S. 016-2024-JUS)  {Color.RESET}")
    print(f"{Color.BLUE}  Grupo 4 - Universidad Nacional de San Agustín (UNSA) - Arequipa 2026 {Color.RESET}")
    print(f"{Color.CYAN}{Color.BOLD}========================================================================{Color.RESET}\n")

def listar_evidencias():
    banner()
    print(f"{Color.BOLD}Banco de Evidencias de Prueba ('Organización Ejemplo S.A.C.'):{Color.RESET}\n")
    print(f"{'ID':<4} | {'Evidencia':<42} | {'Control':<8} | {'Resultado Clave':<22}")
    print("-" * 82)
    for k, v in EVIDENCIAS_PRUEBA.items():
        res_color = Color.GREEN if v['resultado'] == 'Conforme' else (
            Color.YELLOW if v['resultado'] == 'Oportunidad de mejora' else (
                Color.RED if 'mayor' in v['resultado'] else Color.CYAN
            )
        )
        print(f"{k:<4} | {v['nombre'][:42]:<42} | {v['control'][:8]:<8} | {res_color}{v['resultado']:<22}{Color.RESET}")
    print("-" * 82)
    print(f"\n{Color.YELLOW}Uso:{Color.RESET} python probar_auditor.py --evaluar <ID>   (Ejemplo: python probar_auditor.py --evaluar E6)")
    print(f"     python probar_auditor.py --consolidar     (Genera Matriz e Informe consolidado)")

def evaluar_evidencia(id_evidencia):
    banner()
    if id_evidencia not in EVIDENCIAS_PRUEBA:
        print(f"{Color.RED}[ERROR] La evidencia '{id_evidencia}' no existe en el banco de pruebas.{Color.RESET}")
        return

    ev = EVIDENCIAS_PRUEBA[id_evidencia]

    print(f"{Color.BOLD}>>> EJECUTANDO MODO M2: EVALUACIÓN DE EVIDENCIA CONTEXTUAL{Color.RESET}\n")
    print(f"{Color.BLUE}Evidencia:{Color.RESET}       {ev['nombre']}")
    print(f"{Color.BLUE}Tipo:{Color.RESET}            {ev['tipo']}")
    print(f"{Color.BLUE}Control Auditado:{Color.RESET}{ev['control']}")
    print(f"{Color.BLUE}Rol Entidad:{Color.RESET}     {ev['rol']} del Tratamiento\n")

    print(f"{Color.YELLOW}--- FRAGMENTO DE EVIDENCIA PRESENTADA ---{Color.RESET}")
    for line in ev['texto'].split("\n"):
        print(f"  | {line}")
    print(f"{Color.YELLOW}-----------------------------------------{Color.RESET}\n")

    print(f"{Color.BOLD}>>> EVALUACIÓN DE LOS 6 CRITERIOS (ISO 19011):{Color.RESET}")
    print(f"{'Criterio':<14} | {'Cumple':<10} | {'Sustento / Faltante detectado':<50}")
    print("-" * 80)
    for crit, (cumple, sustento) in ev['criterios'].items():
        c_color = Color.GREEN if cumple == "Sí" else (Color.YELLOW if cumple == "Parcial" else Color.RED)
        print(f"{crit:<14} | {c_color}{cumple:<10}{Color.RESET} | {sustento}")
    print("-" * 80)

    res_color = Color.GREEN if ev['resultado'] == 'Conforme' else (
        Color.YELLOW if ev['resultado'] == 'Oportunidad de mejora' else (
            Color.RED if 'mayor' in ev['resultado'] else Color.CYAN
        )
    )
    print(f"\n{Color.BOLD}DICTAMEN / RESULTADO:{Color.RESET} {res_color}{Color.BOLD}{ev['resultado'].upper()}{Color.RESET}")
    print(f"{Color.BOLD}HALLAZGO FORMAL:{Color.RESET}      {ev['hallazgo']}")
    print(f"{Color.BOLD}BASE LEGAL PERÚ:{Color.RESET}      {Color.MAGENTA}{ev['base_legal']}{Color.RESET}")
    print(f"{Color.BOLD}RECOMENDACIÓN:{Color.RESET}        {ev['recomendacion']}")
    print(f"{Color.BOLD}EVIDENCIA SUGERIDA:{Color.RESET}   {ev['evidencia_adicional']}")
    print(f"\n{Color.CYAN}* Nota de Gobernanza: Resultado propuesto por IA según Skill. Requiere validación del auditor humano.{Color.RESET}\n")

def consolidar():
    banner()
    print(f"{Color.BOLD}>>> EJECUTANDO MODO M3: CONSOLIDACIÓN DE MATRIZ E INFORME (ISO 19011){Color.RESET}\n")
    print(f"Consolidando resultados de 8 evidencias evaluadas para 'Organización Ejemplo S.A.C.'...\n")

    conteo = {"Conforme": 0, "Oportunidad de mejora": 0, "No conformidad menor": 0, "No conformidad mayor": 0, "No verificable": 0}

    print(f"{'ID':<4} | {'Control':<8} | {'Pert':<4} | {'Suf':<4} | {'Vig':<4} | {'Apr':<4} | {'Traz':<4} | {'Comp':<4} | {'Resultado':<22}")
    print("-" * 75)
    for k, v in EVIDENCIAS_PRUEBA.items():
        res = v['resultado']
        conteo[res] += 1
        res_color = Color.GREEN if res == 'Conforme' else (
            Color.YELLOW if res == 'Oportunidad de mejora' else (
                Color.RED if 'mayor' in res else Color.CYAN
            )
        )
        c = v['criterios']
        def symbol(val):
            return "✔" if val == "Sí" else ("◐" if val == "Parcial" else "✖")

        print(f"{k:<4} | {v['control'][:8]:<8} | {symbol(c['Pertinencia'][0]):<4} | {symbol(c['Suficiencia'][0]):<4} | {symbol(c['Vigencia'][0]):<4} | {symbol(c['Aprobación'][0]):<4} | {symbol(c['Trazabilidad'][0]):<4} | {symbol(c['Completitud'][0]):<4} | {res_color}{res:<22}{Color.RESET}")
    print("-" * 75)

    total = len(EVIDENCIAS_PRUEBA)
    validos = total - conteo['No verificable']
    conformidad = ((conteo['Conforme'] + conteo['Oportunidad de mejora']) / validos) * 100 if validos > 0 else 0

    print(f"\n{Color.BOLD}RESUMEN CUANTITATIVO:{Color.RESET}")
    print(f"  • Total evidencias evaluadas:      {total}")
    print(f"  • {Color.GREEN}Conformes:{Color.RESET}                         {conteo['Conforme']}")
    print(f"  • {Color.YELLOW}Oportunidades de mejora:{Color.RESET}           {conteo['Oportunidad de mejora']}")
    print(f"  • {Color.CYAN}No conformidades menores:{Color.RESET}          {conteo['No conformidad menor']}")
    print(f"  • {Color.RED}No conformidades mayores:{Color.RESET}          {conteo['No conformidad mayor']}")
    print(f"  • {Color.MAGENTA}No verificables (sin evidencia):{Color.RESET}   {conteo['No verificable']}")
    print(f"  • {Color.BOLD}Porcentaje de Conformidad PIMS:{Color.RESET}    {conformidad:.1f} %")

    print(f"\n{Color.BOLD}ORDEN DE SEVERIDAD DE HALLAZGOS (PLAN DE ACCIÓN SUGERIDO):{Color.RESET}")
    print(f"  1. {Color.RED}[CRÍTICO - 30 días]{Color.RESET} E6 (Plazo 72h vs 48h) y E5 (Contrato sin DPA ni firmas) y E2 (Consentimientos nulos).")
    print(f"  2. {Color.CYAN}[MEDIO - 60 días]{Color.RESET}   E1 (Política desactualizada), E7 (Omisión de procesos RoPA) y E3 (Plazos ARCO).")
    print(f"  3. {Color.YELLOW}[BAJO - 90 días]{Color.RESET}    E4 (Medir efectividad de capacitaciones).")
    print(f"  4. {Color.MAGENTA}[REQUIERE PRUEBA]{Color.RESET}   E8 (Aportar evidencias técnicas de cifrado de base de datos).\n")

def main():
    parser = argparse.ArgumentParser(description="AuditPIMS CLI Demo - Grupo 4 UNSA")
    parser.add_argument("--listar", action="store_true", help="Lista las evidencias de prueba")
    parser.add_argument("--evaluar", type=str, metavar="ID", help="Evalúa una evidencia (E1 a E8)")
    parser.add_argument("--consolidar", action="store_true", help="Consolida la matriz y el informe final")

    args = parser.parse_args()

    if args.listar:
        listar_evidencias()
    elif args.evaluar:
        evaluar_evidencia(args.evaluar.upper())
    elif args.consolidar:
        consolidar()
    else:
        listar_evidencias()

if __name__ == "__main__":
    main()
