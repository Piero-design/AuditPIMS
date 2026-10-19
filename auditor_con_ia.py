#!/usr/bin/env python3
"""
AuditPIMS con IA Real (OpenAI / Gemini / Groq / Ollama)
ISO/IEC 27701:2025 | ISO 19011:2018 | Ley 29733 (D.S. 016-2024-JUS)
Grupo 4 - Universidad Nacional de San Agustín (UNSA) - 2026
"""

import os
import sys
import argparse
from pathlib import Path

# Colores para la terminal
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

BASE_DIR = Path(__file__).resolve().parent
SKILL_DIR = BASE_DIR / "auditoria-evidencias-pims"

def cargar_contexto_skill():
    """Carga los archivos de referencia reales de la Skill para inyectarlos en el prompt de la IA."""
    skill_md = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8") if (SKILL_DIR / "SKILL.md").exists() else ""
    criterios = (SKILL_DIR / "references" / "criterios_evaluacion.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "criterios_evaluacion.md").exists() else ""
    ley = (SKILL_DIR / "references" / "ley29733_resumen.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "ley29733_resumen.md").exists() else ""
    controles = (SKILL_DIR / "references" / "controles_iso27701.md").read_text(encoding="utf-8") if (SKILL_DIR / "references" / "controles_iso27701.md").exists() else ""
    
    system_prompt = f"""Eres AuditPIMS, un Auditor Interno Senior de Sistemas de Gestión de Privacidad de la Información (PIMS) especializado en ISO/IEC 27701:2025, ISO 19011:2018 y la Ley 29733 de Perú con su nuevo reglamento D.S. N.º 016-2024-JUS (vigente desde marzo de 2025).

INSTRUCCIONES Y REGLAS DE LA SKILL:
{skill_md}

CRITERIOS FORMALES DE AUDITORÍA (ISO 19011):
{criterios}

MARCO LEGAL PERÚ (Ley 29733 y D.S. 016-2024-JUS):
{ley}

CATÁLOGO DE CONTROLES:
{controles}

REGLAS OBLIGATORIAS:
1. Sin evidencia no hay conformidad. Nunca declares Conforme si no hay evidencia tangible (declaraciones verbales son 'No verificable').
2. Cita siempre fragmentos textuales exactos entrecomillados.
3. Evalúa con rigor los 6 criterios: Pertinencia, Suficiencia, Vigencia, Aprobación, Trazabilidad, Completitud.
4. Si detectas incumplimientos a la normativa peruana (por ejemplo plazos de 72h frente a las 48h que exige el D.S. 016-2024-JUS), dictamina NO CONFORMIDAD MAYOR.
5. Emite la FICHA DE EVALUACIÓN DE EVIDENCIA formal.
6. Cierra recordando que el resultado es una propuesta técnica para validación del auditor humano.
"""
    return system_prompt

# Banco de evidencias del Hito 1 para probar en vivo
CASOS_PRUEBA = {
    "E1": (
        "POLÍTICA DE PRIVACIDAD - Organización Ejemplo S.A.C. Versión 1.0 (Aprobada en marzo 2021).\n"
        "Alcance: Tratamiento de datos de alumnos y docentes de cursos virtuales.\n"
        "Marco Legal: En estricto cumplimiento del Reglamento de la Ley 29733 aprobado mediante D.S. 003-2013-JUS.\n"
        "Revisión: Esta política se revisará cuando la gerencia lo considere conveniente.\n"
        "Atención: Para ejercer sus derechos escribir a contacto@ejemplo.pe. No se cuenta con Oficial de Datos Personales."
    ),
    "E2": (
        "REGISTRO CRM MARKETING - Organización Ejemplo S.A.C.\n"
        "Muestra evaluada: 12 titulares registrados en campañas web y telefónicas.\n"
        "Filas 1-2, 4-6, 8, 10, 12: Fecha, canal web (checkbox log) y hash de términos aceptados v2.\n"
        "Filas 3, 7, 9, 11: Registros migrados de base antigua. Campos 'Fecha_Consentimiento', 'Canal_Captación' y 'Versión_Aviso' están en blanco (NULL).\n"
        "Nota: Contiene DNI y teléfonos reales en archivo original sin anonimizar."
    ),
    "E3": (
        "PROCEDIMIENTO DE DERECHOS ARCO - PRO-ARCO-01 v2.0 (Enero 2026).\n"
        "Elaborado por: Asesoría Legal. Aprobado por: Gerente de Operaciones.\n"
        "Flujo: Recepción vía formulario web o correo arco@ejemplo.pe.\n"
        "Plazos: 'Las solicitudes serán respondidas conforme a los plazos previstos en el reglamento vigente'.\n"
        "Registro: Se mantendrá un archivo Excel con correlativo, titular y tipo de derecho solicitado."
    ),
    "E6": (
        "PROCEDIMIENTO DE INCIDENTES DE PRIVACIDAD - PRO-INC-01 v0.3 (Borrador de trabajo).\n"
        "Objetivo: Responder ante fugas o accesos no autorizados a datos personales.\n"
        "Sección 4.2: 'En caso de incidente con impacto relevante, el Oficial de Seguridad notificará a la Autoridad Nacional de Protección de Datos Personales en un plazo máximo de 72 horas contadas desde su confirmación'.\n"
        "Anexos: El formulario REG-INC-01 (Registro de Incidentes) no se encuentra adjunto ni implementado."
    ),
    "E8": (
        "MINUTA DE REUNIÓN DE AUDITORÍA - 28/09/2026.\n"
        "Auditor: '¿Cómo garantizan la confidencialidad de la base de datos de postulantes?'.\n"
        "Jefe de TI: 'Las bases de datos en PostgreSQL están totalmente cifradas en reposo y en tránsito. Contamos con claves rotativas y respaldos diarios seguros. Todo el sistema está protegido y no hay riesgo de fuga.'\n"
        "Documentos de respaldo adjuntos: Ninguno. No se aportaron capturas de configuración, políticas de cifrado ni certificados SSL/TLS."
    )
}

def inicializar_cliente_llm():
    """Detecta las credenciales disponibles (OpenAI, Gemini o Groq) e inicializa el cliente."""
    try:
        from openai import OpenAI
    except ImportError:
        print(f"{Color.RED}Error: La librería 'openai' no está instalada. Ejecuta: pip install openai{Color.RESET}")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = None
    modelo = "gpt-4o-mini"
    proveedor = "OpenAI"

    # 1. Verificar si hay clave de Gemini (Prioridad recomendada - IA real activa)
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        api_key = gemini_key
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        modelo = "gemini-3.8-flash"
        proveedor = "Google Gemini (gemini-3.8-flash)"

    # 2. Verificar si hay clave de OpenAI
    elif os.environ.get("OPENAI_API_KEY"):
        api_key = os.environ.get("OPENAI_API_KEY")
        proveedor = f"OpenAI ({modelo})"

    # 3. Verificar si hay clave de Groq
    elif os.environ.get("GROQ_API_KEY"):
        api_key = os.environ.get("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1"
        modelo = "llama-3.3-70b-versatile"
        proveedor = "Groq Llama 3.3 70B"

    # 4. Verificar si hay token de GitHub
    elif os.environ.get("GITHUB_TOKEN"):
        api_key = os.environ.get("GITHUB_TOKEN")
        base_url = "https://models.github.ai/inference"
        modelo = "gpt-4o-mini"
        proveedor = "GitHub Models (GPT-4o-mini / Student Pack)"

    # 5. Si no hay variable de entorno, pedirla en consola
    else:
        print(f"{Color.YELLOW}{Color.BOLD}>>> CONFIGURACIÓN DE IA EN VIVO <<<{Color.RESET}")
        print("Para que la IA razone en tiempo real, ingresa una API Key o Token:")
        print("1. GitHub Token (ghp_... con GitHub Student Pack)")
        print("2. Google Gemini (Gratis en https://aistudio.google.com/apikey)")
        print("3. Groq (Gratis en https://console.groq.com)")
        print("4. OpenAI (ChatGPT API)")
        print("-" * 65)
        api_key = input("Pega tu API Key / Token aquí (o presiona Enter para salir): ").strip()
        if not api_key:
            print(f"{Color.RED}No se proporcionó credencial. Cancelando.{Color.RESET}")
            sys.exit(0)

        if api_key.startswith("ghp_") or api_key.startswith("github_pat_"):
            base_url = "https://models.github.ai/inference"
            modelo = "gpt-4o-mini"
            proveedor = "GitHub Models (GPT-4o-mini / Student Pack)"
        elif api_key.startswith("AIza") or api_key.startswith("AQ.") or "AIza" in api_key or "AQ." in api_key:
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
            modelo = "gemini-3.8-flash"
            proveedor = "Google Gemini (gemini-3.8-flash)"
        elif api_key.startswith("gsk_"):
            base_url = "https://api.groq.com/openai/v1"
            modelo = "llama-3.3-70b-versatile"
            proveedor = "Groq Llama 3.3 70B"
        else:
            proveedor = "OpenAI"

    client = OpenAI(api_key=api_key, base_url=base_url)
    return client, modelo, proveedor

def auditar_texto_o_archivo(texto_evidencia, nombre_evidencia="Documento Externo"):
    import hashlib
    sha256_hash = hashlib.sha256(texto_evidencia.encode('utf-8')).hexdigest()

    print(f"\n{Color.CYAN}{Color.BOLD}========================================================================{Color.RESET}")
    print(f"{Color.CYAN}{Color.BOLD}      AuditPIMS: Evaluación con IA Generativa en Tiempo Real           {Color.RESET}")
    print(f"{Color.CYAN}{Color.BOLD}========================================================================{Color.RESET}\n")

    client, modelo, proveedor = inicializar_cliente_llm()
    print(f"{Color.BLUE}Conectado a:{Color.RESET} {Color.GREEN}{proveedor}{Color.RESET}")
    print(f"{Color.BLUE}Evidencia auditada:{Color.RESET} {nombre_evidencia}")
    print(f"{Color.BLUE}Integridad (Hash SHA-256):{Color.RESET} {Color.CYAN}{sha256_hash}{Color.RESET}")
    print(f"{Color.BLUE}Cargando Skill y Base de Conocimiento de:{Color.RESET} {SKILL_DIR}")

    system_prompt = cargar_contexto_skill()

    user_prompt = f"""Por favor, audita la siguiente evidencia presentada por una organización en el marco de ISO/IEC 27701:2025 y la Ley 29733 de Perú (con su reglamento D.S. N.º 016-2024-JUS):

DOCUMENTO PRESENTADO COMO EVIDENCIA:
\"\"\"
{texto_evidencia}
\"\"\"

Aplica estrictamente el Modo M2 de la skill:
1. Identifica el tipo de documento y el control ISO 27701 más probable.
2. Evalúa los 6 criterios (Pertinencia, Suficiencia, Vigencia, Aprobación, Trazabilidad, Completitud) citando fragmentos textuales exactos.
3. Dictamina el resultado formal (Conforme, Oportunidad de mejora, No conformidad menor, No conformidad mayor o No verificable).
4. Redacta el hallazgo según ISO 19011 (Requisito + Evidencia + Desviación).
5. Indica la base legal peruana aplicable y recomendaciones de mitigación."""

    print(f"\n{Color.YELLOW}Enviando evidencia a la IA y esperando razonamiento en vivo...{Color.RESET}\n")

    if "gemini" in modelo:
        modelos_intentos = ["gemini-3.8-flash", "gemini-3.8-flash-lite"]
    elif "gpt" in modelo:
        modelos_intentos = ["gpt-4o-mini", "openai/gpt-4o-mini", "gpt-4o"]
    else:
        modelos_intentos = [modelo]

    import time
    respuesta_obtenida = False

    for m in modelos_intentos:
        for intento in range(2):
            try:
                print(f"Probando modelo: {Color.CYAN}{m}{Color.RESET} (intento {intento + 1})...")
                response = client.chat.completions.create(
                    model=m,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.1
                )
                if isinstance(response, str):
                    try:
                        import json
                        data = json.loads(response)
                        if isinstance(data, dict) and "choices" in data and len(data["choices"]) > 0:
                            resultado_ia = data["choices"][0]["message"]["content"]
                        else:
                            resultado_ia = response
                    except Exception:
                        resultado_ia = response
                elif hasattr(response, 'choices') and len(response.choices) > 0:
                    resultado_ia = response.choices[0].message.content
                elif isinstance(response, dict) and 'choices' in response and len(response['choices']) > 0:
                    resultado_ia = response['choices'][0]['message']['content']
                else:
                    resultado_ia = str(response)

                print(f"\n{Color.BOLD}>>> DICTAMEN DE AUDITORÍA GENERADO POR LA IA ({m}):{Color.RESET}\n")
                print(resultado_ia)
                print(f"\n{Color.GREEN}✔ Auditoría completada con éxito por la IA.{Color.RESET}\n")
                respuesta_obtenida = True
                break
            except Exception as e:
                err_str = str(e)
                if "503" in err_str or "high demand" in err_str:
                    print(f"{Color.YELLOW}El modelo {m} tiene alta demanda (503). Reintentando en 2 segundos...{Color.RESET}")
                    time.sleep(2)
                elif "404" in err_str or "NOT_FOUND" in err_str:
                    print(f"{Color.YELLOW}El modelo {m} no está disponible (404). Pasando al siguiente modelo...{Color.RESET}")
                    break
                else:
                    print(f"{Color.RED}Error con {m}: {err_str}{Color.RESET}")
                    break
        if respuesta_obtenida:
            break

    if not respuesta_obtenida:
        print(f"\n{Color.RED}[AVISO]{Color.RESET} Los servidores están temporalmente saturados. Usa el modo local:")
        print(f"  {Color.GREEN}python3 probar_auditor.py --evaluar E6{Color.RESET}")

def main():
    parser = argparse.ArgumentParser(description="AuditPIMS con IA Real en Vivo - Grupo 4")
    parser.add_argument("--evaluar", type=str, help="Caso de prueba del banco (ej. E1, E2, E3, E6, E8)")
    parser.add_argument("--archivo", type=str, help="Ruta de un archivo de texto o documento para auditar")
    parser.add_argument("--interactivo", action="store_true", help="Pega o escribe tu propio documento en la consola")

    args = parser.parse_args()

    if args.archivo:
        ruta = Path(args.archivo)
        if not ruta.exists():
            print(f"{Color.RED}Error: El archivo '{args.archivo}' no existe.{Color.RESET}")
            sys.exit(1)
        texto = ruta.read_text(encoding="utf-8", errors="ignore")
        auditar_texto_o_archivo(texto, nombre_evidencia=str(ruta.name))

    elif args.interactivo:
        print(f"\n{Color.CYAN}Modo interactivo: Pega o escribe el texto del documento a auditar.{Color.RESET}")
        print(f"{Color.YELLOW}(Presiona Enter dos veces o escribe 'FIN' en una línea nueva para terminar):{Color.RESET}\n")
        lineas = []
        while True:
            try:
                linea = input()
                if linea.strip() == "FIN":
                    break
                if not linea and lineas and not lineas[-1]:
                    break
                lineas.append(linea)
            except EOFError:
                break
        texto = "\n".join(lineas).strip()
        if not texto:
            print(f"{Color.RED}No se ingresó texto.{Color.RESET}")
            sys.exit(0)
        auditar_texto_o_archivo(texto, nombre_evidencia="Entrada de usuario")

    elif args.evaluar:
        caso = args.evaluar.upper()
        if caso not in CASOS_PRUEBA:
            print(f"{Color.RED}Caso '{caso}' no encontrado. Disponibles: {list(CASOS_PRUEBA.keys())}{Color.RESET}")
            sys.exit(1)
        auditar_texto_o_archivo(CASOS_PRUEBA[caso], nombre_evidencia=f"Caso de Prueba {caso}")

    else:
        # Por defecto si no se pasa nada, evalúa E6
        auditar_texto_o_archivo(CASOS_PRUEBA["E6"], nombre_evidencia="Caso de Prueba E6 (Procedimiento Incidentes)")

if __name__ == "__main__":
    main()
