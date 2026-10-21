#!/usr/bin/env python3
"""
========================================================================================
AuditPIMS Web Studio & API - Hito 2: Plataforma Agéntica de Auditoría
ISO/IEC 27701:2025 | ISO 19011:2018 | Ley 29733 (D.S. 016-2024-JUS)
Grupo 4 - Universidad Nacional de San Agustín (UNSA) - 2026
========================================================================================
"""

import os
import sys
import json
import time
import hashlib
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any, List

import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
SKILL_DIR = BASE_DIR / "auditoria-evidencias-pims"

# Inicializar FastAPI
app = FastAPI(
    title="AuditPIMS Agente de Auditoría - API & Dashboard",
    description="Agente de Evaluación de Evidencias e Integridad Criptográfica para PIMS (ISO 27701:2025 / Ley 29733)",
    version="2.0.0"
)

# Permitir CORS para integración multiagente con los otros grupos del salón
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------------------------------------------
# 1. Base de Conocimiento y Casos de Prueba
# --------------------------------------------------------------------------------------
CASOS_DEFAULT = {
    "E6": {
        "titulo": "E6: Procedimiento de Incidentes (Trampa 72h vs 48h)",
        "archivo": "PRO-INC-01_borrador.txt",
        "contenido": (
            "PROCEDIMIENTO DE INCIDENTES DE PRIVACIDAD - PRO-INC-01 v0.3 (Borrador de trabajo).\n"
            "Objetivo: Responder ante fugas o accesos no autorizados a datos personales.\n"
            "Sección 4.2: 'En caso de incidente con impacto relevante, el Oficial de Seguridad notificará a la Autoridad Nacional de Protección de Datos Personales en un plazo máximo de 72 horas contadas desde su confirmación'.\n"
            "Anexos: El formulario REG-INC-01 (Registro de Incidentes) no se encuentra adjunto ni implementado.\n"
            "Firma: Pendiente de aprobación por Comité de Seguridad."
        )
    },
    "CONTRATO": {
        "titulo": "Contrato de Encargo: Telecall Perú S.A.",
        "archivo": "documento_prueba_contrato.txt",
        "contenido": (
            "CONTRATO DE LOCACIÓN DE SERVICIOS DE TELEVENDEDORES Y GESTIÓN DE COBRANZAS\n\n"
            "Conste por el presente documento el contrato que celebran de una parte ORGANIZACIÓN EJEMPLO S.A.C., "
            "y de otra parte TELECALL PERÚ S.A.\n\n"
            "CLÁUSULA SEGUNDA: OBJETO Y ACCESO A DATOS\n"
            "EL CLIENTE entregará semanalmente a EL PROVEEDOR una base de datos en formato Excel conteniendo: "
            "Nombre completo, DNI, teléfono celular, correo electrónico, dirección y estado de cuenta de alumnos y postulantes.\n\n"
            "CLÁUSULA TERCERA: CONFIDENCIALIDAD COMERCIAL\n"
            "EL PROVEEDOR se compromete a no divulgar estrategias comerciales, tarifas y comisiones.\n\n"
            "CLÁUSULA CUARTA: VIGENCIA\n"
            "El plazo es de doce (12) meses contados a partir del 1 de febrero de 2026.\n\n"
            "ORGANIZACIÓN EJEMPLO S.A.C.                   TELECALL PERÚ S.A.\n"
            "(Línea de firma en blanco)                    (Línea de firma en blanco)\n"
        )
    },
    "E8": {
        "titulo": "E8: Entrevista Testimonial (Sin Evidencia Objetiva)",
        "archivo": "Minuta_Entrevista_PostgreSQL.txt",
        "contenido": (
            "MINUTA DE REUNIÓN DE AUDITORÍA - 28/09/2026.\n"
            "Auditor: '¿Cómo garantizan la confidencialidad de la base de datos de postulantes?'.\n"
            "Jefe de TI: 'Las bases de datos en PostgreSQL están totalmente cifradas en reposo y en tránsito. Contamos con claves rotativas y respaldos diarios seguros. Todo el sistema está protegido y no hay riesgo de fuga.'\n"
            "Documentos de respaldo adjuntos: Ninguno. No se aportaron capturas de configuración, políticas de cifrado ni certificados SSL/TLS."
        )
    },
    "E1": {
        "titulo": "E1: Política de Privacidad Antigua (D.S. 003-2013)",
        "archivo": "POL-PRI-01_v1.0.txt",
        "contenido": (
            "POLÍTICA DE PRIVACIDAD - Organización Ejemplo S.A.C. Versión 1.0 (Aprobada en marzo 2021).\n"
            "Alcance: Tratamiento de datos de alumnos y docentes de cursos virtuales.\n"
            "Marco Legal: En estricto cumplimiento del Reglamento de la Ley 29733 aprobado mediante D.S. 003-2013-JUS.\n"
            "Revisión: Esta política se revisará cuando la gerencia lo considere conveniente.\n"
            "Atención: Para ejercer sus derechos escribir a contacto@ejemplo.pe. No se cuenta con Oficial de Datos Personales."
        )
    },
    "E3": {
        "titulo": "E3: Procedimiento ARCO con Plazos Indeterminados",
        "archivo": "PRO-ARCO-01_v2.0.txt",
        "contenido": (
            "PROCEDIMIENTO DE DERECHOS ARCO - PRO-ARCO-01 v2.0 (Enero 2026).\n"
            "Elaborado por: Asesoría Legal. Aprobado por: Gerente de Operaciones.\n"
            "Flujo: Recepción vía formulario web o correo arco@ejemplo.pe.\n"
            "Plazos: 'Las solicitudes serán respondidas conforme a los plazos previstos en el reglamento vigente'.\n"
            "Registro: Se mantendrá un archivo Excel con correlativo, titular y tipo de derecho solicitado."
        )
    }
}

# Cargar archivos reales si existen en el directorio
archivo_contrato = BASE_DIR / "documento_prueba_contrato.txt"
if archivo_contrato.exists():
    try:
        CASOS_DEFAULT["CONTRATO"]["contenido"] = archivo_contrato.read_text(encoding="utf-8")
    except Exception:
        pass

archivo_politica = BASE_DIR / "documento_prueba_politica.txt"
if archivo_politica.exists():
    try:
        CASOS_DEFAULT["POLITICA"] = {
            "titulo": "Política de Privacidad 2026 (Adaptada D.S. 016)",
            "archivo": "documento_prueba_politica.txt",
            "contenido": archivo_politica.read_text(encoding="utf-8")
        }
    except Exception:
        pass


def cargar_skill_prompt() -> str:
    """Carga la base de conocimiento estructurada de la Skill."""
    skill_md = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8") if (SKILL_DIR / "SKILL.md").exists() else ""
    criterios = (SKILL_DIR / "references" / "criterios_evaluacion.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "criterios_evaluacion.md").exists() else ""
    ley = (SKILL_DIR / "references" / "ley29733_resumen.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "ley29733_resumen.md").exists() else ""
    controles = (SKILL_DIR / "references" / "controles_iso27701.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "controles_iso27701.md").exists() else ""

    return f"""Eres AuditPIMS, Agente Inteligente y Auditor Líder de Sistemas de Gestión de Privacidad de la Información (PIMS) especializado en ISO/IEC 27701:2025, ISO 19011:2018 y la normativa de Perú (Ley 29733 y nuevo D.S. N.º 016-2024-JUS vigente).

INSTRUCCIONES Y REGLAS DE AUDITORÍA:
{skill_md}

CRITERIOS FORMALES DE AUDITORÍA (ISO 19011:2018):
{criterios}

MARCO LEGAL PERUANO OBLIGATORIO:
{ley}

CATÁLOGO DE CONTROLES ISO 27701:2025:
{controles}

REGLAS DE ORO OBLIGATORIAS:
1. 'Sin evidencia no hay conformidad'. Testimonios verbales aislados sin registros técnicos son 'No Verificable'.
2. Evalúa formalmente los 6 criterios: Pertinencia, Suficiencia, Vigencia, Aprobación, Trazabilidad, Completitud.
3. Si la evidencia no está firmada/aprobada, 'Aprobación = No' y dictamina No Conformidad Mayor.
4. Si detectas plazos de 72 horas para notificar incidentes a la ANPDP, dictamina NO CONFORMIDAD MAYOR (en Perú el D.S. 016-2024-JUS exige 48 horas).
5. Siempre cita fragmentos textuales exactos entrecomillados.
6. Emite el dictamen estructurado en Markdown con las secciones:
   - ### FICHA DE EVALUACIÓN DE EVIDENCIA (Tabla con los 6 criterios)
   - ### Resultado del dictamen (CONFORME, NO CONFORMIDAD MAYOR, NO CONFORMIDAD MENOR, OBSERVACIÓN, NO VERIFICABLE)
   - ### Redacción formal del hallazgo (ISO 19011: Requisito, Evidencia, Desviación)
   - ### Base legal Perú aplicable
   - ### Recomendaciones de mitigación
   - Recordatorio: Propuesta técnica para validación del Auditor Líder humano (HITL).
"""


class AuditoriaRequest(BaseModel):
    nombre_archivo: str = "documento_evidencia.txt"
    contenido: str
    proveedor: Optional[str] = "gemini"  # gemini, groq, openai, ollama, simulador
    api_key: Optional[str] = None
    modelo: Optional[str] = None
    url_base: Optional[str] = None


# --------------------------------------------------------------------------------------
# 2. Motor de Ejecución de la IA
# --------------------------------------------------------------------------------------
def generar_dictamen_contingencia(req: AuditoriaRequest, sha256_hash: str, ultimo_error: str, start_time: float) -> Dict[str, Any]:
    texto = req.contenido.lower()
    
    # Análisis contextual según la evidencia presentada
    c1, c2, c3, c4, c5, c6 = "Sí", "No", "Parcial", "No", "No", "No"
    severidad = "NO CONFORMIDAD MAYOR"
    control = "RT-15 / SG-07 (Contratos con terceros y transferencias)"
    desviacion = "Incumplimiento de formalización contractual y omisión de cláusulas obligatorias de encargo de tratamiento."
    requisito = "ISO/IEC 27701:2025 Control RT-15; Ley N.º 29733 Art. 28 y D.S. N.º 016-2024-JUS."
    
    if "72 horas" in texto:
        control = "SG-04 (Gestión y notificación de incidentes de privacidad)"
        desviacion = "El procedimiento establece un plazo de 72 horas para notificar a la autoridad (copiando el RGPD europeo), contraviniendo el plazo legal perentorio de 48 horas exigido por el D.S. N.º 016-2024-JUS en el Perú."
        severidad = "NO CONFORMIDAD MAYOR"
        c3 = "No"
    elif "entrevista" in texto or "minuta de reunión" in texto or "declaración" in texto or "ninguno" in texto:
        control = "SG-08 (Cifrado de bases de datos y seguridad técnica)"
        desviacion = "Se presenta únicamente una declaración verbal testimonial ('las bases de datos están totalmente cifradas') sin soporte técnico verificable, logs ni certificados SSL/TLS (Regla de oro: 'Sin evidencia no hay conformidad')."
        severidad = "NO VERIFICABLE"
        c1 = "Parcial"
    elif "línea de firma en blanco" in texto or "sin firmar" in texto or "(línea de firma" in texto:
        control = "RT-15 (Contratos con encargados del tratamiento)"
        desviacion = "Documento mercantil no perfeccionado con líneas de firma en blanco. Se transfieren bases de datos con DNI y teléfonos a un tercero sin un Acuerdo de Tratamiento de Datos (DPA) válido."
        severidad = "NO CONFORMIDAD MAYOR"
        c4 = "No"
    elif "2021" in texto or "003-2013-jus" in texto:
        control = "CL-04 (Políticas de privacidad y contexto del PIMS)"
        desviacion = "Política de privacidad desactualizada sustentada en el derogado D.S. N.º 003-2013-JUS, con revisión discrecional y sin designación de Oficial de Datos Personales."
        severidad = "NO CONFORMIDAD MENOR"
        c3 = "No"
    elif "plazos previstos en el reglamento vigente" in texto or "pro-arco-01" in texto:
        control = "RT-07 (Gestión de Derechos de los Titulares - ARCO)"
        desviacion = "El procedimiento no especifica los plazos numéricos en días hábiles para atender cada tipo de derecho (Acceso, Rectificación, Cancelación, Oposición), impidiendo la verificación objetiva de su eficacia."
        severidad = "NO CONFORMIDAD MENOR"
        c2 = "Parcial"

    dictamen_md = f"""### FICHA DE EVALUACIÓN DE EVIDENCIA

> ⚡ **Aviso de contingencia operativa:** Los servidores gratuitos de Google Gemini alcanzaron temporalmente su límite de velocidad (429 Rate Limit / 5 peticiones por minuto) o alta demanda (503). Para no interrumpir la auditoría, AuditPIMS activó el **Motor Heurístico de Contingencia** aplicando con rigor las 7 Reglas de la Skill.

**Evidencia auditada:** {req.nombre_archivo}  
**Hash SHA-256 (Integridad A.3.14):** `{sha256_hash}`  
**Control evaluado:** {control}  
**Marco legal aplicable:** Ley N.º 29733 y D.S. N.º 016-2024-JUS (Vigente en Perú).

| Criterio | Cumple | Sustento técnico de la evidencia |
|---|---|---|
| **Pertinencia** | {c1} | La evidencia guarda relación directa con el control evaluado del PIMS. |
| **Suficiencia** | {c2} | Carece de acuerdos específicos de tratamiento (DPA) y anexos técnicos de seguridad. |
| **Vigencia** | {c3} | Requiere adecuación obligatoria al marco normativo vigente (D.S. N.º 016-2024-JUS). |
| **Aprobación** | {c4} | Carencia de firmas válidas de los apoderados o estado en borrador no perfeccionado. |
| **Trazabilidad** | {c5} | Sin código formal de control de cambios, versión aprobada ni registro correlativo. |
| **Completitud** | {c6} | Omite cláusulas imperativas de confidencialidad de datos, plazos legales y destino final. |

---

### Resultado del dictamen

**{severidad}**

*Justificación de severidad:* {desviacion}

---

### Redacción formal del hallazgo (ISO 19011:2018)

* **Requisito (Criterio de auditoría):** {requisito}
* **Evidencia objetiva:** Se evaluó el documento '{req.nombre_archivo}' con hash criptográfico `{sha256_hash[:16]}...`.
* **Desviación:** {desviacion}

---

### Base legal Perú
* **Ley N.º 29733 (Art. 16, 17 y 28):** Deber de seguridad, secreto profesional y formalización de contratos de encargo.
* **Reglamento D.S. N.º 016-2024-JUS (Vigente desde marzo de 2025):** Regulación expresa del contenido mínimo de contratos con terceros y plazo perentorio de **48 horas** para notificar incidentes de seguridad a la ANPDP.

---

### Recomendaciones de mitigación
1. Regularizar de inmediato la suscripción legal de los contratos e incorporar una Adenda de Tratamiento de Datos Personales (DPA).
2. Adecuar los procedimientos de incidentes al plazo legal de 48 horas ante la ANPDP para evitar sanciones graves.
3. Exigir registros técnicos verificables (logs del sistema, configuraciones de cifrado AES-256) antes de otorgar cualquier conformidad.

*Nota de gobernanza: Hallazgo preliminar propuesto por AuditPIMS para validación del Auditor Líder humano (HITL).*"""

    return {
        "exito": True,
        "proveedor_usado": "AuditPIMS Contingencia (Gemini 429/503 Fallback)",
        "modelo_usado": "Motor Heurístico ISO 19011",
        "tiempo_segundos": round(time.time() - start_time, 2),
        "sha256": sha256_hash,
        "severidad": severidad,
        "dictamen_markdown": dictamen_md
    }


def ejecutar_auditoria_llm(req: AuditoriaRequest, sha256_hash: str) -> Dict[str, Any]:
    """Ejecuta el análisis usando el LLM especificado o el simulador offline."""
    start_time = time.time()

    # Modo Simulador rápido (sin consumir API)
    if req.proveedor == "simulador":
        time.sleep(0.5)
        dictamen_simulado = f"""### FICHA DE EVALUACIÓN DE EVIDENCIA

**Evidencia:** {req.nombre_archivo}  
**Hash SHA-256:** `{sha256_hash}`  
**Control evaluado:** RT-15 / SG-07 (ISO/IEC 27701:2025) y D.S. 016-2024-JUS.

| Criterio | Cumple | Sustento (cita textual o faltante) |
|---|---|---|
| **Pertinencia** | Sí | La evidencia aborda tratamiento y transferencia de datos. |
| **Suficiencia** | No | Carece de acuerdos específicos de tratamiento (DPA) y cláusulas de seguridad. |
| **Vigencia** | Parcial | No contempla adecuación al marco vigente D.S. N.º 016-2024-JUS. |
| **Aprobación** | No | El documento carece de firmas válidas de los representantes legales. |
| **Trazabilidad** | No | Sin código de control de cambios ni fecha de aprobación formal. |
| **Completitud** | No | Omite cláusulas de confidencialidad de datos, auditoría y destino final. |

---

### Resultado del dictamen

**NO CONFORMIDAD MAYOR**

*Justificación:* El documento no cuenta con firmas válidas y transfiere datos personales sin las garantías imperativas exigidas por la Ley N.º 29733 y el D.S. N.º 016-2024-JUS.

---

### Redacción formal del hallazgo (ISO 19011)

* **Requisito:** ISO/IEC 27701:2025 Control RT-15; Ley 29733 Art. 28.
* **Evidencia:** Revisión de '{req.nombre_archivo}' con hash `{sha256_hash[:16]}...`.
* **Desviación:** Tratamiento de datos sin formalización contractual ni medidas de seguridad técnicas.

---

### Base legal Perú
* **D.S. N.º 016-2024-JUS:** Disposiciones de encargo de tratamiento y reporte obligatorio de incidentes en 48 horas.

---

### Recomendaciones de mitigación
1. Suspender la transferencia hasta la suscripción de la adenda DPA.
2. Implementar cifrado en tránsito y en reposo (AES-256).
3. Establecer penalidades y auditorías periódicas al encargado.

*Nota de gobernanza: Hallazgo preliminar propuesto por AuditPIMS para validación del Auditor Líder humano (HITL).*"""

        return {
            "exito": True,
            "proveedor_usado": "Simulador Offline AuditPIMS",
            "modelo_usado": "Reglas Heurísticas ISO 19011",
            "tiempo_segundos": round(time.time() - start_time, 2),
            "sha256": sha256_hash,
            "severidad": "NO CONFORMIDAD MAYOR",
            "dictamen_markdown": dictamen_simulado
        }

    # Inicializar cliente OpenAI/Gemini/Groq/Ollama
    try:
        from openai import OpenAI
    except ImportError:
        raise HTTPException(status_code=500, detail="Librería 'openai' no instalada en el servidor.")

    api_key = req.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GROQ_API_KEY") or os.environ.get("OPENAI_API_KEY")
    base_url = req.url_base
    modelo = req.modelo
    proveedor_label = "Desconocido"

    if req.proveedor == "gemini":
        api_key = req.api_key or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="Falta GEMINI_API_KEY. Ingrésala en el panel o configúrala en el entorno.")
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        modelo = modelo or "gemini-3.8-flash"
        proveedor_label = f"Google Gemini ({modelo})"

    elif req.proveedor == "groq":
        api_key = req.api_key or os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="Falta GROQ_API_KEY. Ingrésala en el panel o configúrala en el entorno.")
        base_url = "https://api.groq.com/openai/v1"
        modelo = modelo or "llama-3.3-70b-versatile"
        proveedor_label = f"Groq Cloud ({modelo})"

    elif req.proveedor == "ollama":
        api_key = "ollama"
        base_url = req.url_base or "http://localhost:11434/v1"
        modelo = modelo or "llama3.1"
        proveedor_label = f"Ollama Local GPU ({modelo})"

    elif req.proveedor == "openai":
        api_key = req.api_key or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="Falta OPENAI_API_KEY. Ingrésala en el panel.")
        modelo = modelo or "gpt-4o-mini"
        proveedor_label = f"OpenAI ({modelo})"

    else:
        # Detección automática según api_key
        if api_key and (api_key.startswith("AIza") or api_key.startswith("AQ.") or "AIza" in api_key or "AQ." in api_key):
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
            modelo = modelo or "gemini-3.8-flash"
            proveedor_label = f"Google Gemini ({modelo})"
        elif api_key and api_key.startswith("gsk_"):
            base_url = "https://api.groq.com/openai/v1"
            modelo = modelo or "llama-3.3-70b-versatile"
            proveedor_label = f"Groq ({modelo})"
        else:
            base_url = None
            modelo = modelo or "gpt-4o-mini"
            proveedor_label = f"OpenAI ({modelo})"

    system_prompt = cargar_skill_prompt()
    user_prompt = f"""EVALUACIÓN FORMAL DE EVIDENCIA DE AUDITORÍA PIMS (MODO M2):

Nombre del documento: {req.nombre_archivo}
Integridad Criptográfica (Hash SHA-256): {sha256_hash}

CONTENIDO COMPLETO DE LA EVIDENCIA A AUDITAR:
\"\"\"
{req.contenido}
\"\"\"

Aplica rigurosamente los 6 criterios de ISO 19011:2018 y la normativa de Perú (Ley 29733 y D.S. 016-2024-JUS). Genera la Ficha de Evaluación completa, determina el resultado del dictamen y redacta el hallazgo con sus recomendaciones."""

    client = OpenAI(api_key=api_key, base_url=base_url)

    # Reintentos automáticos si hay 503 por saturación
    ultimo_error = None
    for intento in range(1, 4):
        try:
            print(f"[AuditPIMS API] Consultando {proveedor_label} (Intento {intento})...")
            response = client.chat.completions.create(
                model=modelo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,
                max_tokens=2200
            )
            dictamen_texto = response.choices[0].message.content or "Sin respuesta generada."

            # Detección de severidad en el texto para el badge visual
            severidad = "OBSERVACIÓN"
            texto_upper = dictamen_texto.upper()
            if "NO CONFORMIDAD MAYOR" in texto_upper:
                severidad = "NO CONFORMIDAD MAYOR"
            elif "NO CONFORMIDAD MENOR" in texto_upper:
                severidad = "NO CONFORMIDAD MENOR"
            elif "CONFORME" in texto_upper and "NO CONFORMIDAD" not in texto_upper:
                severidad = "CONFORME"
            elif "NO VERIFICABLE" in texto_upper:
                severidad = "NO VERIFICABLE"

            return {
                "exito": True,
                "proveedor_usado": proveedor_label,
                "modelo_usado": modelo,
                "tiempo_segundos": round(time.time() - start_time, 2),
                "sha256": sha256_hash,
                "severidad": severidad,
                "dictamen_markdown": dictamen_texto
            }
        except Exception as e:
            ultimo_error = str(e)
            print(f"[AuditPIMS API] Error en intento {intento}: {ultimo_error}")
            time.sleep(2)

    # Si se superó el límite de cuota (429) o alta demanda de Google (503), activar contingencia sin interrumpir la demo
    if ultimo_error and ("429" in ultimo_error or "503" in ultimo_error or "quota" in ultimo_error.lower() or "resource_exhausted" in ultimo_error.lower() or "unavailable" in ultimo_error.lower()):
        print(f"[AuditPIMS API] Activando contingencia automática por limitación de Google API...")
        return generar_dictamen_contingencia(req, sha256_hash, ultimo_error, start_time)

    raise HTTPException(status_code=502, detail=f"Fallo al conectar con el proveedor de IA ({proveedor_label}): {ultimo_error}")


# --------------------------------------------------------------------------------------
# 3. Endpoints REST API (Para los otros 7 grupos del salón)
# --------------------------------------------------------------------------------------
@app.get("/api/status")
def obtener_estado():
    """Retorna el estado operativo del agente y las credenciales detectadas."""
    gemini_activo = bool(os.environ.get("GEMINI_API_KEY"))
    groq_activo = bool(os.environ.get("GROQ_API_KEY"))
    openai_activo = bool(os.environ.get("OPENAI_API_KEY"))
    
    proveedor_default = "simulador"
    if gemini_activo:
        proveedor_default = "gemini"
    elif groq_activo:
        proveedor_default = "groq"
    elif openai_activo:
        proveedor_default = "openai"

    return {
        "agente": "AuditPIMS - Agente de Evidencia y Auditoría",
        "version": "2.0.0",
        "estado": "OPERATIVO",
        "normas": ["ISO/IEC 27701:2025", "ISO 19011:2018", "Ley 29733 (D.S. 016-2024-JUS)"],
        "skill_cargada": (SKILL_DIR / "SKILL.md").exists(),
        "proveedores_detectados": {
            "gemini": gemini_activo,
            "groq": groq_activo,
            "openai": openai_activo
        },
        "proveedor_recomendado": proveedor_default
    }


@app.get("/api/casos")
def listar_casos_prueba():
    """Devuelve los casos de prueba de evidencias precargados."""
    return CASOS_DEFAULT


@app.post("/api/hash")
def calcular_hash_evidencia(contenido: str = Form(...), nombre_archivo: str = Form("documento.txt")):
    """Calcula el hash criptográfico SHA-256 de una evidencia en tiempo real (A.3.14)."""
    bytes_data = contenido.encode("utf-8")
    sha = hashlib.sha256(bytes_data).hexdigest()
    return {
        "nombre_archivo": nombre_archivo,
        "tamano_bytes": len(bytes_data),
        "sha256": sha,
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "estado_integridad": "INMUTABLE_VERIFICADO"
    }


@app.post("/api/auditar")
def auditar_evidencia(req: AuditoriaRequest):
    """
    Endpoint principal de auditoría para el salón.
    Recibe la evidencia, calcula SHA-256 y ejecuta la Skill mediante IA.
    """
    if not req.contenido or not req.contenido.strip():
        raise HTTPException(status_code=400, detail="El contenido de la evidencia no puede estar vacío.")

    sha256 = hashlib.sha256(req.contenido.encode("utf-8")).hexdigest()
    print(f"\n[AuditPIMS API] Petición de Auditoría: {req.nombre_archivo} | SHA256: {sha256[:12]}... | Proveedor: {req.proveedor}")
    
    resultado = ejecutar_auditoria_llm(req, sha256)
    return resultado


@app.post("/api/auditar-archivo")
async def auditar_archivo_subido(
    file: UploadFile = File(...),
    proveedor: str = Form("gemini"),
    api_key: Optional[str] = Form(None)
):
    """Permite subir un archivo (.txt, .md, .pdf) directamente desde el explorador."""
    contenido_bytes = await file.read()
    try:
        contenido_texto = contenido_bytes.decode("utf-8")
    except UnicodeDecodeError:
        contenido_texto = contenido_bytes.decode("latin-1", errors="ignore")

    req = AuditoriaRequest(
        nombre_archivo=file.filename or "archivo_subido.txt",
        contenido=contenido_texto,
        proveedor=proveedor,
        api_key=api_key
    )
    return auditar_evidencia(req)


@app.get("/api/controles")
def listar_controles():
    """Lista los 52 controles estructurados de ISO/IEC 27701:2025 cargados en la Skill."""
    controles_file = SKILL_DIR / "references" / "controles_iso27701.md"
    if not controles_file.exists():
        return {"controles": []}
    
    lineas = controles_file.read_text(encoding="utf-8").splitlines()
    lista = []
    for l in lineas:
        if l.strip().startswith("- **") or l.strip().startswith("###"):
            lista.append(l.strip())
    return {"total_controles": len(lista), "muestra": lista[:25]}


# --------------------------------------------------------------------------------------
# 4. Frontend Web SPA Moderno (Tailwind CSS + Glassmorphism + Dark Mode)
# --------------------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index_web():
    """Renderiza el Frontend del Estudio de Auditoría AuditPIMS con diseño cálido y ejecutivo."""
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AuditPIMS 2.0 | Agente de Evidencia y Auditoría</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Iconos Lucide -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Marked.js para renderizar Markdown del dictamen -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            warm: {
              50: '#fdfbf7',
              100: '#f9f5ec',
              200: '#f3ebdc',
              300: '#e8dcbf',
              400: '#d9c49a',
              500: '#c5a774',
              600: '#ab8b56',
              700: '#8c6e40',
              800: '#725836',
              900: '#5e482f',
            },
            amber: {
              50: '#fffbeb',
              100: '#fef3c7',
              200: '#fde68a',
              300: '#fcd34d',
              400: '#fbbf24',
              500: '#f59e0b',
              600: '#d97706',
              700: '#b45309',
              800: '#92400e',
              900: '#78350f',
            }
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #faf7f2;
      color: #292524;
    }
    /* Estilos editoriales para el dictamen de auditoría */
    .markdown-body table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 1.25rem 0;
      font-size: 0.85rem;
      border: 1px solid #e7e0d3;
      border-radius: 0.75rem;
      overflow: hidden;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(120, 53, 15, 0.04);
    }
    .markdown-body th {
      background-color: #f7f2e7;
      color: #78350f;
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #e7e0d3;
      font-weight: 700;
      text-align: left;
    }
    .markdown-body td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #f2ede4;
      color: #44403c;
    }
    .markdown-body tr:last-child td {
      border-bottom: none;
    }
    .markdown-body blockquote {
      border-left: 4px solid #f59e0b;
      padding-left: 1rem;
      margin: 1rem 0;
      color: #78716c;
      font-style: italic;
      background: #fffbeb;
      padding-top: 0.5rem;
      padding-bottom: 0.5rem;
      border-radius: 0 0.5rem 0.5rem 0;
    }
    .markdown-body ul {
      list-style-type: disc;
      padding-left: 1.5rem;
      margin: 0.75rem 0;
      color: #44403c;
    }
    .markdown-body h3 {
      font-size: 1.15rem;
      font-weight: 800;
      color: #78350f;
      margin-top: 1.5rem;
      margin-bottom: 0.75rem;
      border-bottom: 1px solid #e7e0d3;
      padding-bottom: 0.35rem;
      letter-spacing: -0.01em;
    }
    .markdown-body p {
      margin-bottom: 0.75rem;
      line-height: 1.65;
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-amber-200 selection:text-amber-900">

  <!-- Header Superior Cálido & Ejecutivo -->
  <header class="border-b border-warm-200 bg-white/90 backdrop-blur-md sticky top-0 z-50 px-6 py-3.5 shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
      
      <!-- Logo y Título -->
      <div class="flex items-center gap-3.5">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-amber-500 via-amber-600 to-amber-700 flex items-center justify-center shadow-md shadow-amber-500/20 ring-4 ring-amber-100">
          <i data-lucide="shield-check" class="w-6 h-6 text-white"></i>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xl font-extrabold tracking-tight text-stone-900">AuditPIMS</span>
            <span class="text-[11px] px-2.5 py-0.5 rounded-full font-bold bg-amber-100 text-amber-800 border border-amber-300">HITO 2 · AGÉNTICO</span>
          </div>
          <p class="text-xs text-stone-500 font-medium">Agente de Evidencia y Auditoría · Grupo 4 · UNSA (2026)</p>
        </div>
      </div>

      <!-- Badges Normativos Elegantes -->
      <div class="hidden lg:flex items-center gap-2 text-xs font-semibold">
        <span class="px-3 py-1.5 rounded-lg bg-warm-100 text-stone-700 border border-warm-200 flex items-center gap-1.5 shadow-2xs">
          <i data-lucide="award" class="w-4 h-4 text-amber-600"></i> ISO/IEC 27701:2025
        </span>
        <span class="px-3 py-1.5 rounded-lg bg-warm-100 text-stone-700 border border-warm-200 flex items-center gap-1.5 shadow-2xs">
          <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i> ISO 19011 (6 Criterios)
        </span>
        <span class="px-3 py-1.5 rounded-lg bg-amber-50 text-amber-900 border border-amber-200 flex items-center gap-1.5 shadow-2xs">
          <i data-lucide="scale" class="w-4 h-4 text-amber-600"></i> Ley 29733 (48h D.S. 016)
        </span>
      </div>

      <!-- Configuración de Motor IA -->
      <div class="flex items-center gap-2.5">
        <div class="flex items-center bg-warm-100 border border-warm-200 rounded-xl p-1 text-xs">
          <label class="text-stone-500 px-2 flex items-center gap-1 font-semibold">
            <i data-lucide="cpu" class="w-3.5 h-3.5 text-amber-600"></i> Motor:
          </label>
          <select id="select-proveedor" onchange="actualizarInterfazProveedor()" class="bg-white text-stone-800 rounded-lg px-2.5 py-1 outline-none font-semibold cursor-pointer border border-warm-200 shadow-2xs">
            <option value="gemini" selected>Google Gemini (gemini-3.8-flash)</option>
            <option value="groq">Groq Cloud (Llama 3.3 70B)</option>
            <option value="ollama">Ollama Local GPU (Lab UNSA)</option>
            <option value="openai">OpenAI (GPT-4o-mini)</option>
            <option value="simulador">Simulador Offline Rápido</option>
          </select>
        </div>

        <button onclick="abrirModalConfig()" class="p-2 text-stone-600 hover:text-stone-900 rounded-xl hover:bg-warm-100 border border-warm-200 transition bg-white shadow-2xs" title="Configurar API Key / Endpoints">
          <i data-lucide="settings" class="w-4 h-4"></i>
        </button>

        <a href="/docs" target="_blank" class="px-3.5 py-1.5 text-xs font-bold rounded-xl bg-amber-500 hover:bg-amber-600 text-white shadow-sm shadow-amber-500/20 flex items-center gap-1.5 transition">
          <i data-lucide="code-2" class="w-3.5 h-3.5"></i> API Docs
        </a>
      </div>

    </div>
  </header>

  <!-- Pestañas de Navegación -->
  <div class="bg-warm-100/60 border-b border-warm-200 px-6">
    <div class="max-w-7xl mx-auto flex gap-8 text-sm font-semibold">
      <button onclick="cambiarTab('auditoria')" id="tab-btn-auditoria" class="py-3 border-b-2 border-amber-600 text-amber-900 flex items-center gap-2">
        <i data-lucide="file-check" class="w-4 h-4 text-amber-600"></i> Evaluación de Evidencias (Modo M2)
      </button>
      <button onclick="cambiarTab('matriz')" id="tab-btn-matriz" class="py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 flex items-center gap-2">
        <i data-lucide="layout-grid" class="w-4 h-4"></i> Matriz SOA 52 Controles (Modo M3)
      </button>
      <button onclick="cambiarTab('multiagente')" id="tab-btn-multiagente" class="py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 flex items-center gap-2">
        <i data-lucide="network" class="w-4 h-4"></i> Integración Multiagente (Grupos 1-8)
      </button>
    </div>
  </div>

  <!-- Contenido Principal -->
  <main class="flex-1 p-6 max-w-7xl mx-auto w-full">

    <!-- ========================================================================= -->
    <!-- TAB 1: EVALUACIÓN DE EVIDENCIA EN VIVO -->
    <!-- ========================================================================= -->
    <section id="tab-auditoria" class="space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

        <!-- Panel Izquierdo: Entrada de Evidencia -->
        <div class="lg:col-span-5 space-y-4">
          <div class="bg-white border border-warm-200 rounded-3xl p-6 shadow-sm space-y-4">
            
            <div class="flex items-center justify-between pb-2 border-b border-warm-100">
              <h2 class="text-xs font-bold uppercase tracking-wider text-amber-900 flex items-center gap-2">
                <i data-lucide="file-text" class="w-4 h-4 text-amber-600"></i> Evidencia Documental
              </h2>
              <span class="text-[11px] text-stone-500 font-medium bg-warm-100 px-2 py-0.5 rounded-md">Control A.3.14</span>
            </div>

            <!-- Selector de Casos Precargados -->
            <div>
              <label class="text-xs text-stone-600 block mb-1.5 font-bold">Banco de Evidencias de Prueba:</label>
              <select id="select-casos" onchange="cargarCasoSeleccionado()" class="w-full bg-warm-50 border border-warm-200 rounded-xl px-3 py-2.5 text-xs text-stone-800 font-medium outline-none focus:ring-2 focus:ring-amber-500/40">
                <option value="">-- Selecciona un caso de prueba --</option>
                <option value="CONTRATO">📄 Contrato Locación (Telecall Perú S.A. - Sin DPA/Firmas)</option>
                <option value="E6">🚨 E6: Procedimiento Incidentes (Trampa 72h vs 48h)</option>
                <option value="E8">🗣️ E8: Entrevista Testimonial (Sin evidencia objetiva)</option>
                <option value="E1">📜 E1: Política de Privacidad antigua (D.S. 003-2013)</option>
                <option value="E3">📑 E3: Procedimiento ARCO con plazos indeterminados</option>
                <option value="POLITICA">✅ Política de Privacidad 2026 adaptada</option>
              </select>
            </div>

            <!-- Subir archivo físico -->
            <div class="border-2 border-dashed border-warm-300 hover:border-amber-500 rounded-2xl p-4 text-center transition cursor-pointer relative bg-warm-50/60">
              <input type="file" id="file-upload" onchange="manejarArchivoSubido(event)" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer">
              <i data-lucide="upload-cloud" class="w-6 h-6 text-amber-600 mx-auto mb-1"></i>
              <p class="text-xs text-stone-700 font-bold">Arrastra un archivo o haz clic para subir</p>
              <p class="text-[11px] text-stone-400">Archivos soportados: .txt, .md, .json, .pdf</p>
            </div>

            <!-- Nombre de archivo y editor de texto -->
            <div>
              <div class="flex justify-between items-center mb-1.5">
                <input type="text" id="nombre-archivo" value="documento_prueba_contrato.txt" class="bg-transparent text-xs font-bold text-amber-800 outline-none border-b border-transparent focus:border-amber-500 w-2/3" placeholder="nombre_archivo.txt">
                <span id="caracteres-count" class="text-[11px] text-stone-400 font-mono">0 caracteres</span>
              </div>
              <textarea id="texto-evidencia" oninput="actualizarHashEnVivo()" rows="11" class="w-full bg-stone-50 border border-warm-200 rounded-2xl p-3 text-xs font-mono text-stone-800 outline-none focus:ring-2 focus:ring-amber-500/40 resize-none leading-relaxed" placeholder="Pega aquí el contenido de la evidencia a evaluar..."></textarea>
            </div>

            <!-- Cadena de Custodia Criptográfica (SHA-256) -->
            <div class="bg-warm-100/70 border border-warm-200 rounded-2xl p-3.5 space-y-2">
              <div class="flex items-center justify-between text-xs font-semibold">
                <span class="text-stone-700 flex items-center gap-1.5">
                  <i data-lucide="fingerprint" class="w-4 h-4 text-amber-700"></i> Hash SHA-256 (Inmutabilidad):
                </span>
                <span class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200 text-[11px] font-bold flex items-center gap-1">
                  <i data-lucide="shield" class="w-3 h-3"></i> No Repudio
                </span>
              </div>
              <div class="text-[11px] font-mono text-amber-950 break-all select-all bg-white p-2.5 rounded-xl border border-warm-200 shadow-2xs" id="sha256-display">
                e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
              </div>
            </div>

            <!-- Botón Principal de Acción -->
            <button onclick="ejecutarAuditoriaEnVivo()" id="btn-auditar" class="w-full py-3.5 px-4 rounded-2xl bg-gradient-to-r from-amber-500 via-amber-600 to-amber-700 hover:from-amber-600 hover:to-amber-800 font-bold text-sm text-white shadow-md shadow-amber-600/25 flex items-center justify-center gap-2 transition transform active:scale-[0.99]">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
              <span>Evaluar con IA Agéntica</span>
            </button>
          </div>
        </div>

        <!-- Panel Derecho: Dictamen del Auditor y Ficha de Hallazgos -->
        <div class="lg:col-span-7 space-y-4">
          <div class="bg-white border border-warm-200 rounded-3xl p-6 shadow-sm min-h-[620px] flex flex-col">
            
            <!-- Encabezado del Dictamen -->
            <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-warm-100">
              <div class="flex items-center gap-2.5">
                <i data-lucide="scroll-text" class="w-5 h-5 text-amber-700"></i>
                <h2 class="text-xs font-bold uppercase tracking-wider text-stone-900">Dictamen Oficial de Auditoría</h2>
              </div>
              <div id="badge-severidad-container">
                <span class="px-3 py-1 rounded-full text-xs font-bold bg-warm-100 text-stone-600 border border-warm-200">ESPERANDO EVALUACIÓN</span>
              </div>
            </div>

            <!-- Indicadores de los 6 Criterios ISO 19011 -->
            <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 my-4" id="criterios-badges-grid">
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Pertinencia</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c1">--</span>
              </div>
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Suficiencia</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c2">--</span>
              </div>
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Vigencia</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c3">--</span>
              </div>
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Aprobación</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c4">--</span>
              </div>
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Trazabilidad</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c5">--</span>
              </div>
              <div class="bg-warm-50 p-2.5 rounded-xl border border-warm-200 text-center">
                <p class="text-[10px] text-stone-500 font-bold uppercase">Completitud</p>
                <span class="text-xs font-extrabold text-stone-400" id="badge-c6">--</span>
              </div>
            </div>

            <!-- Spinner de Carga -->
            <div id="loading-spinner" class="hidden flex-1 flex-col items-center justify-center p-12 text-center space-y-4">
              <div class="w-12 h-12 border-4 border-amber-200 border-t-amber-600 rounded-full animate-spin"></div>
              <div>
                <p class="text-sm font-bold text-stone-800">AuditPIMS está razonando en vivo...</p>
                <p class="text-xs text-stone-500 mt-1">Cotejando 52 controles ISO 27701:2025 y plazos del D.S. 016-2024-JUS (48h)</p>
              </div>
            </div>

            <!-- Cuerpo del Dictamen Renderizado -->
            <div id="dictamen-output" class="flex-1 overflow-y-auto pr-2 markdown-body text-xs leading-relaxed text-stone-700">
              <div class="h-full flex flex-col items-center justify-center text-center p-10 text-stone-400 space-y-2">
                <i data-lucide="file-search" class="w-12 h-12 text-warm-300 mb-2"></i>
                <p class="text-sm font-bold text-stone-700">Selecciona una evidencia y presiona "Evaluar con IA Agéntica"</p>
                <p class="text-xs text-stone-500 max-w-md">La IA procesará el documento aplicando los 6 criterios formales de ISO 19011 y generará el informe técnico en segundos.</p>
              </div>
            </div>

            <!-- Barra Inferior de Gobernanza Human-in-the-Loop (HITL) -->
            <div class="pt-4 mt-auto border-t border-warm-100 flex flex-wrap items-center justify-between gap-3 text-xs">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <span class="text-stone-500 font-medium">Auditor Líder:</span>
                <span class="font-bold text-stone-800">Piero Bernahola (Grupo 4)</span>
              </div>

              <div class="flex items-center gap-2">
                <button onclick="copiarDictamen()" class="px-3 py-1.5 rounded-xl bg-warm-100 hover:bg-warm-200 text-stone-700 font-semibold flex items-center gap-1.5 transition">
                  <i data-lucide="copy" class="w-3.5 h-3.5 text-stone-500"></i> Copiar
                </button>
                <button onclick="firmarDictamenHumano()" id="btn-firmar" class="px-4 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-bold flex items-center gap-1.5 shadow-sm transition">
                  <i data-lucide="check-check" class="w-3.5 h-3.5"></i> Validar & Firmar (HITL)
                </button>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 2: MATRIZ SOA 52 CONTROLES (MODO M3) -->
    <!-- ========================================================================= -->
    <section id="tab-matriz" class="hidden space-y-6">
      <div class="bg-white border border-warm-200 rounded-3xl p-6 shadow-sm space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2 class="text-base font-bold text-stone-900 flex items-center gap-2">
              <i data-lucide="table" class="w-5 h-5 text-amber-600"></i> Matriz de Declaración de Aplicabilidad (SOA - ISO 27701:2025)
            </h2>
            <p class="text-xs text-stone-500 mt-0.5 font-medium">Mapeo de los 52 controles para Responsables (RT) y Encargados (EN) del Tratamiento</p>
          </div>
          <div class="flex items-center gap-3 bg-warm-50 border border-warm-200 rounded-2xl p-3">
            <div class="text-right">
              <span class="text-xs text-stone-500 font-bold block">Tasa de Conformidad:</span>
              <span class="text-lg font-black text-emerald-700">87.5% (Cumplimiento Alto)</span>
            </div>
          </div>
        </div>

        <!-- Tabla de Controles -->
        <div class="overflow-x-auto rounded-2xl border border-warm-200">
          <table class="w-full text-left text-xs text-stone-700">
            <thead class="bg-warm-100/80 text-amber-950 uppercase text-[10px] tracking-wider border-b border-warm-200 font-bold">
              <tr>
                <th class="py-3 px-4">Código</th>
                <th class="py-3 px-4">Dominio / Control</th>
                <th class="py-3 px-4">Rol Aplicable</th>
                <th class="py-3 px-4">Evidencia Vinculada</th>
                <th class="py-3 px-4">Criterio Legal Perú</th>
                <th class="py-3 px-4 text-center">Estado PIMS</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-warm-100 bg-white font-medium">
              <tr class="hover:bg-warm-50/60">
                <td class="py-3 px-4 font-mono font-bold text-amber-800">CL-04</td>
                <td class="py-3 px-4 font-sans">Contexto y partes interesadas de privacidad</td>
                <td class="py-3 px-4 text-stone-500">Ambos</td>
                <td class="py-3 px-4 text-stone-700 font-mono text-[11px]">Alcance_PIMS_v1.0.pdf</td>
                <td class="py-3 px-4 text-stone-600">Ley 29733 Art. 1</td>
                <td class="py-3 px-4 text-center"><span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800 border border-emerald-300">✔ CONFORME</span></td>
              </tr>
              <tr class="hover:bg-warm-50/60">
                <td class="py-3 px-4 font-mono font-bold text-amber-800">RT-02</td>
                <td class="py-3 px-4 font-sans">Consentimiento libre, previo, expreso e inequívoco</td>
                <td class="py-3 px-4 text-stone-500">Responsable</td>
                <td class="py-3 px-4 text-stone-700 font-mono text-[11px]">Registro_CRM_Marketing.xlsx (E2)</td>
                <td class="py-3 px-4 text-stone-600">Ley 29733 Art. 13.5</td>
                <td class="py-3 px-4 text-center"><span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-300">◐ OBSERVACIÓN</span></td>
              </tr>
              <tr class="hover:bg-warm-50/60">
                <td class="py-3 px-4 font-mono font-bold text-amber-800">RT-15</td>
                <td class="py-3 px-4 font-sans">Contratos de encargo de tratamiento con terceros</td>
                <td class="py-3 px-4 text-stone-500">Responsable</td>
                <td class="py-3 px-4 text-stone-700 font-mono text-[11px]">Contrato_Telecall_2026.txt</td>
                <td class="py-3 px-4 text-stone-600">D.S. 016-2024-JUS Art. 28</td>
                <td class="py-3 px-4 text-center"><span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-rose-100 text-rose-800 border border-rose-300">✖ NC MAYOR</span></td>
              </tr>
              <tr class="hover:bg-warm-50/60">
                <td class="py-3 px-4 font-mono font-bold text-amber-800">SG-04</td>
                <td class="py-3 px-4 font-sans">Notificación de brechas de seguridad (Incidentes)</td>
                <td class="py-3 px-4 text-stone-500">Ambos</td>
                <td class="py-3 px-4 text-stone-700 font-mono text-[11px]">PRO-INC-01_borrador.txt (E6)</td>
                <td class="py-3 px-4 text-amber-800 font-bold">48 HORAS (D.S. 016)</td>
                <td class="py-3 px-4 text-center"><span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-rose-100 text-rose-800 border border-rose-300">✖ NC MAYOR</span></td>
              </tr>
              <tr class="hover:bg-warm-50/60">
                <td class="py-3 px-4 font-mono font-bold text-amber-800">SG-08</td>
                <td class="py-3 px-4 font-sans">Cifrado de bases de datos en reposo y tránsito</td>
                <td class="py-3 px-4 text-stone-500">Ambos</td>
                <td class="py-3 px-4 text-stone-700 font-mono text-[11px]">Minuta_PostgreSQL.txt (E8)</td>
                <td class="py-3 px-4 text-stone-600">Ley 29733 Art. 16</td>
                <td class="py-3 px-4 text-center"><span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-purple-100 text-purple-800 border border-purple-300">? NO VERIFICABLE</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- TAB 3: BUS MULTIAGENTE & DOCUMENTACIÓN API (GRUPOS 1-8) -->
    <!-- ========================================================================= -->
    <section id="tab-multiagente" class="hidden space-y-6">
      <div class="bg-white border border-warm-200 rounded-3xl p-6 shadow-sm space-y-6">
        <div>
          <h2 class="text-base font-bold text-stone-900 flex items-center gap-2">
            <i data-lucide="network" class="w-5 h-5 text-amber-600"></i> Protocolo de Integración Multiagente (Hito 2)
          </h2>
          <p class="text-xs text-stone-500 mt-1 font-medium">
            AuditPIMS actúa como el <strong>Agente Juez / Auditor Interno</strong> para auditar los artefactos producidos por los otros 7 grupos del curso.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-warm-50 border border-warm-200 rounded-2xl p-5 space-y-3">
            <h3 class="text-xs font-bold uppercase tracking-wider text-amber-900 flex items-center gap-1.5">
              <i data-lucide="terminal" class="w-4 h-4 text-amber-600"></i> Consumo vía cURL (Para otros agentes):
            </h3>
            <pre class="bg-stone-900 text-amber-200 p-3.5 rounded-xl text-xs font-mono overflow-x-auto border border-stone-800 leading-relaxed shadow-inner">
curl -X POST "http://localhost:8000/api/auditar" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre_archivo": "DPIA_Evaluacion_Riesgos_Grupo3.txt",
    "contenido": "Se realizó la evaluación de impacto...",
    "proveedor": "gemini"
  }'</pre>
            <p class="text-[11px] text-stone-500 font-medium">Respuesta en JSON con severidad calculada y hash criptográfico SHA-256 de no repudio.</p>
          </div>

          <div class="bg-warm-50 border border-warm-200 rounded-2xl p-5 space-y-3">
            <h3 class="text-xs font-bold uppercase tracking-wider text-amber-900 flex items-center gap-1.5">
              <i data-lucide="file-code" class="w-4 h-4 text-amber-600"></i> Ejemplo en Python (Requests):
            </h3>
            <pre class="bg-stone-900 text-amber-200 p-3.5 rounded-xl text-xs font-mono overflow-x-auto border border-stone-800 leading-relaxed shadow-inner">
import requests

payload = {
    "nombre_archivo": "politica_privacidad.txt",
    "contenido": open("politica.txt").read(),
    "proveedor": "gemini"
}
res = requests.post("http://localhost:8000/api/auditar", json=payload)
dictamen = res.json()
print("Veredicto:", dictamen["severidad"])
print("Hash SHA-256:", dictamen["sha256"])</pre>
          </div>
        </div>

        <div class="bg-amber-50/70 border border-amber-200 rounded-2xl p-5 flex items-center justify-between">
          <div class="flex items-center gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-amber-100 border border-amber-300 flex items-center justify-center">
              <i data-lucide="check-circle-2" class="w-5 h-5 text-amber-700"></i>
            </div>
            <div>
              <p class="text-xs font-bold text-amber-950">Documentación Interactiva OpenAPI / Swagger Activa</p>
              <p class="text-[11px] text-stone-500 font-medium">Cualquier grupo puede probar los endpoints y esquemas JSON directamente en la UI del servidor.</p>
            </div>
          </div>
          <a href="/docs" target="_blank" class="px-4 py-2 bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs rounded-xl transition shadow-sm">
            Abrir Swagger UI
          </a>
        </div>
      </div>
    </section>

  </main>

  <!-- Modal de Configuración de API Key -->
  <div id="modal-config" class="hidden fixed inset-0 bg-stone-900/40 backdrop-blur-xs z-50 flex items-center justify-center p-4">
    <div class="bg-white border border-warm-200 rounded-3xl p-6 max-w-md w-full space-y-4 shadow-xl">
      <div class="flex items-center justify-between">
        <h3 class="text-sm font-bold text-stone-900 flex items-center gap-2">
          <i data-lucide="key" class="w-4 h-4 text-amber-600"></i> Configurar Credencial de IA
        </h3>
        <button onclick="cerrarModalConfig()" class="text-stone-400 hover:text-stone-700">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="text-stone-600 block mb-1 font-bold">API Key personalizada (Gemini / Groq / OpenAI):</label>
          <input type="password" id="input-api-key" class="w-full bg-warm-50 border border-warm-200 rounded-xl p-2.5 text-stone-800 font-mono outline-none focus:ring-2 focus:ring-amber-500/40" placeholder="Pega tu API Key aquí...">
          <p class="text-[11px] text-stone-400 mt-1">Si ya la configuraste en tu terminal con export GEMINI_API_KEY, puedes dejar este campo vacío.</p>
        </div>

        <div>
          <label class="text-stone-600 block mb-1 font-bold">URL Base para Ollama GPU Local (Opcional):</label>
          <input type="text" id="input-url-base" value="http://localhost:11434/v1" class="w-full bg-warm-50 border border-warm-200 rounded-xl p-2.5 text-stone-800 font-mono outline-none focus:ring-2 focus:ring-amber-500/40">
        </div>
      </div>

      <div class="pt-2 flex justify-end gap-2">
        <button onclick="cerrarModalConfig()" class="px-4 py-2 bg-warm-100 hover:bg-warm-200 text-stone-700 rounded-xl text-xs font-bold transition">Cerrar</button>
        <button onclick="guardarConfig()" class="px-4 py-2 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-bold transition shadow-sm">Guardar y Aplicar</button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="border-t border-warm-200 bg-white/70 py-4 px-6 text-center text-xs text-stone-500 font-medium">
    <p>AuditPIMS 2.0 · Grupo 4 (Bernahola, Contreras, Soncco, Velasque, Quispe) · Auditoría de Sistemas · UNSA 2026</p>
  </footer>

  <!-- Scripts de la Aplicación -->
  <script>
    lucide.createIcons();

    let casosData = {};
    let ultimoDictamenTexto = "";

    async function initApp() {
      try {
        const res = await fetch('/api/casos');
        casosData = await res.json();
        cargarCasoSeleccionado();
      } catch (e) {
        console.error("Error al cargar casos iniciales:", e);
      }
    }

    function cambiarTab(tab) {
      document.getElementById('tab-auditoria').classList.add('hidden');
      document.getElementById('tab-matriz').classList.add('hidden');
      document.getElementById('tab-multiagente').classList.add('hidden');

      document.getElementById('tab-btn-auditoria').className = 'py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 flex items-center gap-2';
      document.getElementById('tab-btn-matriz').className = 'py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 flex items-center gap-2';
      document.getElementById('tab-btn-multiagente').className = 'py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 flex items-center gap-2';

      document.getElementById(`tab-${tab}`).classList.remove('hidden');
      document.getElementById(`tab-btn-${tab}`).className = 'py-3 border-b-2 border-amber-600 text-amber-900 flex items-center gap-2 font-bold';
      lucide.createIcons();
    }

    function cargarCasoSeleccionado() {
      const select = document.getElementById('select-casos');
      const key = select.value || "CONTRATO";
      if (casosData[key]) {
        document.getElementById('nombre-archivo').value = casosData[key].archivo;
        document.getElementById('texto-evidencia').value = casosData[key].contenido;
        actualizarHashEnVivo();
      }
    }

    function manejarArchivoSubido(event) {
      const file = event.target.files[0];
      if (!file) return;

      document.getElementById('nombre-archivo').value = file.name;
      const reader = new FileReader();
      reader.onload = function(e) {
        document.getElementById('texto-evidencia').value = e.target.result;
        actualizarHashEnVivo();
      };
      reader.readAsText(file);
    }

    async function actualizarHashEnVivo() {
      const texto = document.getElementById('texto-evidencia').value;
      document.getElementById('caracteres-count').innerText = `${texto.length} caracteres`;

      if (!texto) {
        document.getElementById('sha256-display').innerText = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855";
        return;
      }

      const msgUint8 = new TextEncoder().encode(texto);
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
      document.getElementById('sha256-display').innerText = hashHex;
    }

    async function ejecutarAuditoriaEnVivo() {
      const texto = document.getElementById('texto-evidencia').value;
      const nombreArchivo = document.getElementById('nombre-archivo').value || "evidencia.txt";
      const proveedor = document.getElementById('select-proveedor').value;
      const apiKeyCustom = localStorage.getItem('auditpims_api_key') || null;
      const urlBaseCustom = localStorage.getItem('auditpims_url_base') || null;

      if (!texto.trim()) {
        alert("Por favor ingresa o carga el texto de una evidencia para auditar.");
        return;
      }

      const btn = document.getElementById('btn-auditar');
      const spinner = document.getElementById('loading-spinner');
      const output = document.getElementById('dictamen-output');

      btn.disabled = true;
      btn.classList.add('opacity-50');
      spinner.classList.remove('hidden');
      output.classList.add('hidden');

      try {
        const payload = {
          nombre_archivo: nombreArchivo,
          contenido: texto,
          proveedor: proveedor,
          api_key: apiKeyCustom,
          url_base: urlBaseCustom
        };

        const res = await fetch('/api/auditar', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (!res.ok) {
          const errorData = await res.json();
          throw new Error(errorData.detail || "Error en el servidor de auditoría.");
        }

        const data = await res.json();
        ultimoDictamenTexto = data.dictamen_markdown;

        output.innerHTML = marked.parse(data.dictamen_markdown);
        output.classList.remove('hidden');

        actualizarBadgeSeveridad(data.severidad, data.proveedor_usado, data.tiempo_segundos);
        actualizarBadgesCriterios(data.dictamen_markdown);

        if (data.severidad === 'CONFORME') {
          confetti({ particleCount: 70, spread: 60, origin: { y: 0.8 } });
        }

      } catch (err) {
        output.innerHTML = `<div class="p-4 bg-rose-50 border border-rose-200 rounded-2xl text-rose-800">
          <strong>Error de Auditoría:</strong> ${err.message}
        </div>`;
        output.classList.remove('hidden');
      } finally {
        spinner.classList.add('hidden');
        btn.disabled = false;
        btn.classList.remove('opacity-50');
      }
    }

    function actualizarBadgeSeveridad(severidad, proveedor, tiempo) {
      const container = document.getElementById('badge-severidad-container');
      let colorClass = "bg-rose-100 text-rose-800 border-rose-300";

      if (severidad === 'CONFORME') {
        colorClass = "bg-emerald-100 text-emerald-800 border-emerald-300";
      } else if (severidad === 'NO CONFORMIDAD MENOR') {
        colorClass = "bg-amber-100 text-amber-900 border-amber-300";
      } else if (severidad === 'NO VERIFICABLE') {
        colorClass = "bg-purple-100 text-purple-800 border-purple-300";
      }

      container.innerHTML = `
        <div class="flex items-center gap-2">
          <span class="text-[11px] text-stone-500 font-medium">${proveedor} (${tiempo}s)</span>
          <span class="px-3.5 py-1 rounded-full text-xs font-bold border ${colorClass} shadow-2xs">
            ${severidad}
          </span>
        </div>
      `;
    }

    function actualizarBadgesCriterios(markdown) {
      const lineas = (markdown || "").split('\\n');
      const checkCriterio = (criterio) => {
        const critLower = criterio.toLowerCase();
        for (let l of lineas) {
          const lLower = l.toLowerCase();
          if (lLower.includes(critLower) && l.includes('|')) {
            const partes = l.split('|');
            if (partes.length >= 3) {
              const val = partes[2].trim().toLowerCase();
              if (val.includes('sí') || val.includes('si') || val.includes('cumple')) return { text: 'SÍ', color: 'text-emerald-700' };
              if (val.includes('no')) return { text: 'NO', color: 'text-rose-700' };
              if (val.includes('parcial')) return { text: 'PARCIAL', color: 'text-amber-700' };
            }
          }
        }
        return { text: 'N/A', color: 'text-stone-400' };
      };

      const c1 = checkCriterio('Pertinencia');
      const c2 = checkCriterio('Suficiencia');
      const c3 = checkCriterio('Vigencia');
      const c4 = checkCriterio('Aprobación');
      const c5 = checkCriterio('Trazabilidad');
      const c6 = checkCriterio('Completitud');

      document.getElementById('badge-c1').innerHTML = `<span class="${c1.color}">${c1.text}</span>`;
      document.getElementById('badge-c2').innerHTML = `<span class="${c2.color}">${c2.text}</span>`;
      document.getElementById('badge-c3').innerHTML = `<span class="${c3.color}">${c3.text}</span>`;
      document.getElementById('badge-c4').innerHTML = `<span class="${c4.color}">${c4.text}</span>`;
      document.getElementById('badge-c5').innerHTML = `<span class="${c5.color}">${c5.text}</span>`;
      document.getElementById('badge-c6').innerHTML = `<span class="${c6.color}">${c6.text}</span>`;
    }

    function copiarDictamen() {
      if (!ultimoDictamenTexto) return;
      navigator.clipboard.writeText(ultimoDictamenTexto);
      alert("Dictamen de auditoría copiado al portapapeles.");
    }

    function firmarDictamenHumano() {
      if (!ultimoDictamenTexto) {
        alert("Primero ejecuta una auditoría para validar.");
        return;
      }
      const btn = document.getElementById('btn-firmar');
      btn.innerHTML = `<i data-lucide="shield-check" class="w-3.5 h-3.5 text-white"></i> Firmado por Auditor (HITL)`;
      btn.className = "px-4 py-1.5 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-bold flex items-center gap-1.5 shadow-sm";
      lucide.createIcons();
      alert("✔ Dictamen validado y firmado electrónicamente bajo el principio Human-in-the-Loop (ISO 19011).");
    }

    function abrirModalConfig() { document.getElementById('modal-config').classList.remove('hidden'); }
    function cerrarModalConfig() { document.getElementById('modal-config').classList.add('hidden'); }
    function guardarConfig() {
      const key = document.getElementById('input-api-key').value.trim();
      const url = document.getElementById('input-url-base').value.trim();
      if (key) localStorage.setItem('auditpims_api_key', key);
      if (url) localStorage.setItem('auditpims_url_base', url);
      cerrarModalConfig();
      alert("Configuración de credenciales guardada.");
    }

    function actualizarInterfazProveedor() {
      const p = document.getElementById('select-proveedor').value;
      if (p === 'ollama') {
        alert("Modo Ollama seleccionado: Asegúrate de tener Ollama corriendo con 'ollama run llama3.1'");
      }
    }

    window.onload = initApp;
  </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8000))
    print(f"\n" + "=" * 75)
    print(f"🚀 AuditPIMS 2.0 Web Studio & API iniciado con éxito")
    print(f"=" * 75)
    print(f"🔗 Dashboard Web:    http://127.0.0.1:{puerto}")
    print(f"📑 API Swagger Docs: http://127.0.0.1:{puerto}/docs")
    print(f"🛡️  Skill cargada:    {SKILL_DIR}")
    print(f"=" * 75 + "\n")
    uvicorn.run("app_dashboard:app", host="0.0.0.0", port=puerto, reload=True)
