# GUION MAESTRO DE EXPOSICIÓN – HITO 1 (GRUPO 4)
## AuditPIMS: Agente de Evidencia y Auditoría
**Curso:** Auditoría de Sistemas – UNSA (2026)  
**Docente:** Edward Vicente Zarate Carlos  
**Integrantes:**
- Bernahola Vilca Piero Javier
- Contreras Huamani, Paul Michaell
- Soncco Mamani Max Junior
- Velasque Arcos Mikhail
- Quispe Madariaga Jeferson

---

## 🎯 ESTRATEGIA DE PRESENTACIÓN ("Show me the code")
* **Cero diapositivas:** No proyectar PowerPoint.
* **Qué proyectar:** 
  1. En la primera mitad: El **Informe Técnico en PDF** (páginas clave de arquitectura y criterios).
  2. En la segunda mitad: **VS Code con la carpeta de la Skill** y la **Terminal en vivo** ejecutando la prueba técnica.
* **Dinámica del equipo:** Este guion tiene un solo hilo conductor fluido. Puede exponerlo uno solo con el apoyo del grupo, o repartirse las secciones entre los 5 integrantes. Todos deben dominar la misma narrativa.

---

## ⏱️ GUION MINUTO A MINUTO (5 a 7 minutos)

### 📌 PARTE 1: Introducción, Problema y Base Normativa (1:30 min)
*(Proyectar en pantalla: Portada y Sección 1 y 2 del Informe Técnico)*

**Qué decir:**
> "Buenos días profesor. Somos el Grupo 4 y nuestro proyecto es **AuditPIMS: Agente de Evidencia y Auditoría**.
>
> En un Sistema de Gestión de Privacidad de la Información (PIMS), el mayor cuello de botella no es definir políticas, sino **demostrar con evidencias objetivas** que los controles realmente se cumplen en el día a día.
>
> Para este Hito 1, nos fundamentamos en dos marcos normativos estrictamente vigentes:
> 1. La nueva norma internacional **ISO/IEC 27701:2025** (2.ª edición, publicada en octubre de 2025), cuya principal revolución es que ahora es un estándar **independiente y certificable por sí mismo**, sin exigir previamente ISO 27001.
> 2. El marco legal peruano obligatorio: la **Ley N.º 29733** y su nuevo Reglamento aprobado mediante el **D.S. N.º 016-2024-JUS** (vigente desde marzo de 2025), que introduce exigencias críticas como el reporte de brechas de seguridad en un plazo perentorio de 48 horas y la designación obligatoria del Oficial de Datos Personales."

---

### 📌 PARTE 2: De Prompt Improvisado a Skill Modular (1:30 min)
*(Proyectar en pantalla: Sección 3 del informe y abrir en VS Code la carpeta `auditoria-evidencias-pims`)*

**Qué decir:**
> "El primer reto técnico del Hito 1 fue transformar la tarea: pasar **de un prompt improvisado a una skill estructurada y reutilizable**.
>
> Si un auditor lanza un prompt suelto a ChatGPT como: *'Revisa esta política y dime si cumple ISO 27701'*, el modelo comete errores graves: responde con generalidades, no cita fragmentos probatorios, no distingue si la empresa es Responsable o Encargada, y cada vez usa criterios diferentes. No es un resultado auditable.
>
> Para resolverlo, construimos la skill técnica **`auditoria-evidencias-pims`**. Como pueden ver aquí en el editor, está compuesta por:
> * **`SKILL.md`:** Que define el disparador contextual y divide la auditoría en **3 Modos de Trabajo**:
>   * **M1 (Planificar):** Genera checklists de evidencias requeridas según el rol.
>   * **M2 (Evaluar):** Analiza evidencias concretas bajo **6 criterios formales de ISO 19011**: *Pertinencia, Suficiencia, Vigencia, Aprobación, Trazabilidad y Completitud*.
>   * **M3 (Consolidar):** Agrupa los hallazgos en una matriz y emite el informe final según severidad.
> * **Carpeta `references/`:** Base de conocimiento modular con 52 controles estructurados, el catálogo de criterios y el resumen legal peruano.
> * **Carpeta `assets/`:** Plantillas formales de matriz e informe de hallazgos."

---

### 📌 PARTE 3: DEMOSTRACIÓN EN VIVO – "SHOW ME THE CODE" (2:30 min)
*(Proyectar en pantalla: La terminal de VS Code o la interfaz de Claude)*

**Qué decir:**
> "Profesor, siguiendo el principio de *'Talk is cheap. Show me the code'*, vamos a ver la evaluación técnica en vivo sobre nuestro banco de pruebas de 'Organización Ejemplo S.A.C.'."

#### 🔹 Caso 1: Detección de Falla Legal Crítica (Evidencia E6)
*(En la terminal, ejecutar: `python probar_auditor.py --evaluar E6`)*

**Qué explicar mientras se ve el resultado en pantalla:**
> "En este caso, auditamos el Procedimiento de Incidentes (E6). El asistente evaluó los 6 criterios y detectó dos fallas severas:
> 1. Es un borrador sin firmas (falla de Aprobación).
> 2. **La falla legal más crítica:** El procedimiento fijaba un plazo de 72 horas para notificar a la autoridad (copiando el RGPD europeo). La skill detectó que bajo el **D.S. 016-2024-JUS de Perú**, el plazo legal obligatorio es de **48 horas**.
> Por tanto, dictaminó automáticamente **No Conformidad Mayor**, citando textualmente la desviación y proponiendo la acción correctiva."

#### 🔹 Caso 2: Regla de Oro – "Sin Evidencia no hay Conformidad" (Evidencia E8)
*(En la terminal, ejecutar: `python probar_auditor.py --evaluar E8`)*

**Qué explicar mientras se ve el resultado en pantalla:**
> "Aquí probamos el control de cifrado en base de datos. Solo se presentó una entrevista donde el Jefe de TI afirma verbalmente: *'Las bases de datos en PostgreSQL están totalmente cifradas'*.
> Un chatbot común diría 'Conforme'. Nuestra skill aplica la regla de oro: **una declaración testimonial aislada carece de evidencia objetiva**. El dictamen es **'No Verificable'** y exige configuraciones técnicas y reportes reales."

#### 🔹 Caso 3: Consolidación Automática de Matriz (Modo M3)
*(En la terminal, ejecutar: `python probar_auditor.py --consolidar`)*

**Qué explicar mientras se ve el resultado en pantalla:**
> "Finalmente, ejecutamos el Modo M3. La skill recopila las 8 evidencias, evalúa los 6 criterios por cada una, genera la matriz con simbología ISO (✔, ◐, ✖) y calcula la tasa de conformidad del PIMS, ordenando los hallazgos por severidad para el plan de acción de la gerencia."

---

### 📌 PARTE 4: Conclusiones y Salto al Hito 2 (1:00 min)
*(Proyectar en pantalla: Tabla de Resultados y Conclusiones del informe)*

**Qué decir:**
> "En las pruebas alcanzamos un **87.5% de coincidencia** con la clave de auditoría. La única discrepancia en la evidencia E3 demostró que la skill fue incluso más estricta que la clave, detectando vacíos en plazos y registros.
>
> **¿Qué representa este Hito 1?** Un Skill y un Asistente funcional que asiste al auditor humano.
>
> **¿Qué haremos en el Hito 2 (Proyecto Agéntico)?**
> Darle **autonomía completa**. El agente no esperará a que un usuario pegue documentos; utilizará herramientas **MCP (Model Context Protocol)** y scripts automatizados para consultar repositorios, calcular hashes criptográficos SHA-256 de integridad de las evidencias y auditar de forma continua el PIMS de la organización.
>
> Muchas gracias. Quedamos atentos a sus preguntas."

---

## 🛡️ BANCO DE PREGUNTAS TRAMPA DEL DOCENTE (Y CÓMO RESPONDER)

### ❓ Pregunta 1: "¿Por qué crearon identificadores propios (CL-04, RT-02, SG-04) y no usaron la numeración exacta de la ISO 27701?"
> **Respuesta:**  
> *"Por dos motivos técnicos y éticos: primero, el texto íntegro de la norma ISO/IEC 27701:2025 está protegido por derechos de autor y copyright de ISO, por lo que estandarizamos el conocimiento con resúmenes propios. Segundo, organizamos los controles en categorías funcionales de auditoría: `CL` para Cláusulas del sistema de gestión, `RT` para Responsables del tratamiento, `EN` para Encargados y `SG` para controles de Seguridad compartidos. En el informe dejamos explícita la regla de que estos identificadores son referenciales para la organización."*

### ❓ Pregunta 2: "¿Por qué dicen que esto es una Skill y no un prompt largo pegado en ChatGPT?"
> **Respuesta:**  
> *"Un prompt suelto vive y muere en una sola sesión de chat, se desconfigura con el contexto y no tiene separación de responsabilidades. Una **Skill** es arquitectura de software: tiene un archivo de metadatos (`SKILL.md`) que el motor de IA indexa, se dispara por intención semántica solo cuando la tarea lo requiere, carga los archivos de referencia de forma modular (Lazy Loading para no saturar la ventana de contexto) y garantiza trazabilidad mediante plantillas inmutables."*

### ❓ Pregunta 3: "¿Por qué en la evidencia E3 el asistente dio 'No conformidad menor' si su clave decía 'Conforme'?"
> **Respuesta:**  
> *"Esa discrepancia demostró la solidez del sistema. El documento de prueba PRO-ARCO-01 decía que respondería 'conforme a los plazos del reglamento', pero no ponía los días hábiles numéricos. Nuestro asistente aplicó con rigor el criterio de **Suficiencia y Completitud**: un auditor no puede medir la eficacia de un proceso si el procedimiento no fija plazos cuantificables. La discrepancia fue un aporte de rigor de la IA que el auditor humano consideró válido."*

### ❓ Pregunta 4: "¿Qué le falta a este Hito 1 para ser verdaderamente un Agente (Hito 2)?"
> **Respuesta:**  
> *"Le falta autonomía en el entorno y herramientas activas. En el Hito 1, el asistente aún requiere que un humano le entregue el documento y le pida la acción. En el Hito 2, el **Agente de Evidencia** tendrá un bucle continuo de percepción-acción: tendrá herramientas (Tools/MCP) para monitorear una base de datos o carpeta de red, extraerá automáticamente logs y documentos, calculará su hash SHA-256 para garantizar inmutabilidad (control A.3.14) y emitirá alertas sin intervención humana."*

### ❓ Pregunta 5: "¿Cómo evitan que la IA alucine o invente cumplimientos?"
> **Respuesta:**  
> *"Mediante las **7 Reglas Obligatorias** inyectadas en la Skill:
> 1. 'Sin evidencia no hay conformidad' (si no hay archivo, es No Verificable).
> 2. 'Cita siempre' (cada hallazgo exige citar entrecomillado el fragmento exacto).
> 3. 'No inventar' (fechas, firmas o artículos que no existan en el texto se consideran faltantes inmediatos).
> 4. 'El auditor humano decide' (la IA propone hallazgos, no certifica ni emite dictámenes vinculantes)."*
