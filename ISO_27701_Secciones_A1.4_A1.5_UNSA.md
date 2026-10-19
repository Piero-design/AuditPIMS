# ISO/IEC 27701:2025 — TABLA A.1: CONTROLES PARA RESPONSABLES DE TRATAMIENTO (PII CONTROLLERS)

## SECCIONES EVALUADAS:
* **SECCIÓN A.1.4: *Privacy by design and privacy by default* (Privacidad desde el diseño y por defecto)** — Controles A.1.4.2 al A.1.4.10
* **SECCIÓN A.1.5: *PII sharing, transfer and disclosure* (Compartición, transferencia y divulgación de datos personales)** — Controles A.1.5.2 al A.1.5.5

---

### CASO DE ESTUDIO: UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA (UNSA)
* **Entidad Evaluada:** Universidad Nacional de San Agustín de Arequipa (UNSA)
* **Marco Normativo Nacional:** Ley N° 29733 (Ley de Protección de Datos Personales - LPDP), Decreto Supremo N° 016-2024-JUS (Nuevo Reglamento de la LPDP), Ley N° 30220 (Ley Universitaria), Ley N° 27806 (Ley de Transparencia y Acceso a la Información Pública), Directiva de Seguridad de la Información (R.D. N° 019-2013-JUS/DGPDP).
* **Auditor Líder / Perfil Profesional:** Ing. Rafael (MSc. Ciberseguridad & Auditoría de Sistemas, Lead Auditor ISO/IEC 27001, CISA, CRISC). 10 años de experiencia en auditoría forense, aseguramiento de la información y cumplimiento de privacidad en el sector público universitario.

---

## ÍNDICE EJECUTIVO Y MATRIZ DE CONTROL DE RIESGOS

| Código | Control ISO/IEC 27701:2025 | Dominio / Tema Central | Madurez UNSA (1-5) | Nivel de Riesgo | Base Normativa Peruana |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **A.1.4.2** | Limit collection | Minimización de campos en recolección | Nivel 2 | **Medio** | Art. 6 Ley 29733 (Proporcionalidad) |
| **A.1.4.3** | Limit processing | Finalidad legítima y no reutilización indebida | Nivel 2 | **Alto** | Art. 5 Ley 29733 (Finalidad) |
| **A.1.4.4** | Accuracy and quality | Calidad, exactitud y actualización de datos | Nivel 3 | **Medio** | Art. 8 Ley 29733 / PIDE-RENIEC |
| **A.1.4.5** | PII minimization objectives | Metas de minimización y seudonimización | Nivel 1 | **Alto** | D.S. 016-2024-JUS (Seudonimización) |
| **A.1.4.6** | PII de-identification and deletion at end of processing | Anonimización y purga de postulantes / egresados | Nivel 1 | **Alto** | Art. 21 Ley 29733 / D.S. 016-2024-JUS |
| **A.1.4.7** | Temporary files | Ciclo de vida y destrucción de archivos temporales | Nivel 2 | **Medio** | Directiva de Seguridad ANPDP |
| **A.1.4.8** | Retention | Plazos de retención y tablas de conservación | Nivel 2 | **Alto** | Ley 30220 / Sistema Nac. de Archivos |
| **A.1.4.9** | Disposal | Procedimientos de desecho físico y borrado seguro | Nivel 1 | **Crítico** | Directiva de Seguridad ANPDP / NIST 800-88 |
| **A.1.4.10** | PII transmission controls | Cifrado en tránsito y enlaces entre sedes (VPN/TLS) | Nivel 2 | **Alto** | Directiva de Seguridad ANPDP (Cifrado) |
| **A.1.5.2** | Identify basis for PII transfer between jurisdictions | Licitud de Flujo Transfronterizo (Cloud Computing) | Nivel 1 | **Crítico** | Art. 15 Ley 29733 / Arts. 65-72 D.S. 016-2024 |
| **A.1.5.3** | Countries and international organizations for transfer | Mapeo de países y convenios internacionales (Erasmus/Purdue) | Nivel 2 | **Medio** | D.S. 016-2024-JUS (Nivel adecuado) |
| **A.1.5.4** | Records of transfer of PII | Bitácora y contratos DPA con Banco de la Nación/Aseguradoras | Nivel 1 | **Alto** | Arts. 50-54 D.S. 016-2024-JUS (Encargo) |
| **A.1.5.5** | Records of PII disclosures to third parties | Registro de entregas judiciales, policiales y fiscalía | Nivel 2 | **Alto** | Ley 27806 / Art. 14 Ley 29733 |

---

# BLOQUE I: SECCIÓN A.1.4 — PRIVACY BY DESIGN AND PRIVACY BY DEFAULT

---

## CONTROL A.1.4.2: LIMIT COLLECTION (LIMITAR LA RECOPILACIÓN)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall limit the collection of PII to the minimum that is relevant, proportional and necessary for the identified purposes."*
> *(La organización debe limitar la recopilación de datos personales al mínimo que sea relevante, proporcional y necesario para los fines identificados).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Significa que la organización no debe pedir información "por si acaso" ni por inercia histórica. Si vas a prestar un servicio, debes pedir estrictamente los datos indispensables para cumplir esa función y nada más.
* **Analogía de la vida real:** Si vas a comprar pan a una panadería, el vendedor solo necesita que le des el dinero y le digas qué pan quieres; pedirte tu tipo de sangre, estado civil, dirección domiciliaria y religión para venderte pan sería un exceso absurdo y desproporcionado.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA OBLIGATORIAMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Fundamento en el **Principio de Proporcionalidad** del Art. 6 de la Ley N° 29733 y Art. 12 del D.S. N° 016-2024-JUS: todo tratamiento de datos debe ser adecuado, relevante y no excesivo en relación a la finalidad.
  * **Estado en la UNSA:** Cumplimiento parcial (Nivel 2). Tradicionalmente, las fichas socioeconómicas de la Dirección Universitaria de Desarrollo Estudiantil y Bienestar (DUS), los formularios de admisión y las matrículas en SISCA arrastran campos innecesarios (orientación religiosa, ocupaciones detalladas de parientes no dependientes o datos de salud sin fin médico específico).

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** En el marco de la simplificación administrativa (D.S. 004-2019-JUS) y los lineamientos de la Secretaría de Gobierno y Transformación Digital (SGTD), la UNSA debe depurar sus formularios en el ecosistema SISCA y portal de postulantes.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En la fase de diseño de formularios web, previo al lanzamiento de cada proceso de admisión y al inicio de la matrícula semestral.
  * **HOW (Cómo):** Mediante una revisión de campos en la base de datos de SISCA y formularios web, eliminando campos obligatorios no indispensables y justificando documentalmente cada atributo solicitado en la ficha de recolección.
  * **WHO (Quién):** Dirección Universitaria de Informática y Comunicaciones (DUIC), Oficina Universitaria de Admisión y Dirección de Bienestar Universitario (DUS).
  * **WHAT (Qué entregables):** Matriz de Justificación de Datos por Formulario e inventario de campos aprobados por el Oficial de Datos Personales.
  * **WHERE (Dónde):** En los módulos de captura de datos de SISCA Docente/Estudiante y en la plataforma web de Admisión UNSA.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2 (Gestionado informalmente).
* **Nivel de Riesgo:** **Medio**. Riesgo de multas por infracción grave ante la Autoridad Nacional de Protección de Datos Personales (ANPDP) por recolección excesiva de datos sensibles.
* **Observación de Auditoría (GAP):** Se constata que la ficha socioeconómica del Comedor Universitario y las encuestas sociofamiliares de bienestar solicitan información detallada de filiación política, credos y bienes familiares sin una justificación de proporcionalidad vinculada al servicio alimentario.
* **Recomendaciones de Remediación:**
  1. Realizar una auditoría técnica de atributos en los formularios de captura y suprimir inmediatamente los campos no esenciales.
  2. Implementar una directiva interna de "Diseño de Formularios Basados en Minimización" que obligue a los desarrolladores de la DUIC a justificar todo nuevo campo en la base de datos PostgreSQL.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"Como universidad pública, la UNSA garantiza que los formularios en SISCA y los procesos de admisión no recojan datos superfluos. Estamos en una campaña de simplificación digital donde solo se exige lo estrictamente necesario para registrar al estudiante y validar su condición académica y socioeconómica, erradicando preguntas invasivas heredadas del pasado."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Durante la evaluación técnica encontramos que la UNSA aún solicita información excesiva en trámites de comedor y bienestar, como antecedentes de parientes o filiaciones que no aportan al servicio. El estándar ISO 27701 y la Ley 29733 sancionan pedir datos 'por si acaso'. Se debe podar el modelo de datos en la base de producción."*

---

## CONTROL A.1.4.3: LIMIT PROCESSING (LIMITAR EL TRATAMIENTO)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall limit the processing of PII to that which is adequate, relevant and necessary for the identified purposes."*
> *(La organización debe limitar el tratamiento de datos personales a aquel que sea adecuado, relevante y necesario para los fines identificados).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Si recopilaste datos para un fin puntual (por ejemplo, registrar las notas de un alumno), no puedes usarlos para otros fines distintos como campañas proselitistas, análisis comerciales o cruces de bases de datos arbitrarios sin autorización.
* **Analogía de la vida real:** Si dejas tu número telefónico en la recepción de una clínica para que te avisen cuando esté listo un análisis de laboratorio, y luego el personal usa tu teléfono para mandarte publicidad de masajes o invitarte a una encuesta electoral.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Amparado en el **Principio de Finalidad** (Art. 5 Ley 29733 y Art. 11 D.S. 016-2024-JUS): los datos no pueden usarse para finalidades distintas a aquellas que motivaron su obtención, salvo consentimiento libre e inequívoco.
  * **Estado en la UNSA:** Cumplimiento deficiente (Nivel 2). Es común que correos electrónicos institucionales `@unsa.edu.pe` o padrones de alumnos sean utilizados para enviar invitaciones proselitistas de listas electorales universitarias, ferias externas o encuestas académicas no autorizadas por los alumnos.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Directivas de Ética en la Función Pública y Estatuto Universitario de la UNSA, que prohíben el desvío de recursos informáticos para fines no institucionales.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En cada consulta SQL, generación de reportes masivos y ejecución de procesos batch en la infraestructura de bases de datos.
  * **HOW (Cómo):** Estableciendo controles de acceso basados en roles (RBAC) estrictos, segregando permisos en bases de datos y prohibiendo extracciones completas de tablas de estudiantes sin visto bueno de Asesoría Jurídica y la DUIC.
  * **WHO (Quién):** Administrador de Base de Datos (DBA) de la DUIC, Oficial de Seguridad de la Información (CISO) y Secretaría General.
  * **WHAT (Qué entregables):** Política de Uso Aceptable de Bases de Datos y bitácora de auditoría de consultas (`Audit Logs`) de PostgreSQL/Oracle.
  * **WHERE (Dónde):** En los servidores de base de datos de producción ubicados en el Data Center Central de la UNSA (Pabellón San Agustín).

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2.
* **Nivel de Riesgo:** **Alto**. Riesgo de sanción por tratamiento indebido e incompatibilidad de finalidades ante la ANPDP.
* **Observación de Auditoría (GAP):** No existen restricciones lógicas a nivel de base de datos para impedir que dependencias administrativas o directores de escuela exporten padrones estudiantiles completos y los reutilicen para comunicaciones no académicas o proyectos personales de investigación sin consentimiento previo.
* **Recomendaciones de Remediación:**
  1. Configurar vistas de base de datos restringidas (Views) y mecanismos de enmascaramiento dinámico de datos (Dynamic Data Masking).
  2. Implementar un módulo formal de solicitudes de reportes donde se exija declarar la finalidad legal y técnica antes de autorizar cualquier descarga masiva de información.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"En la UNSA velamos por el principio de finalidad. Los datos del alumno matriculado solo se procesan para su formación académica, acreditación universitaria y servicios de biblioteca o comedor, impidiendo que su correo o legajo sea comercializado o manipulado para intereses ajenos a la vida universitaria."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Como auditor, observo que cualquier docente o jefe de departamento con acceso a SISCA puede descargar hojas de cálculo con correos y teléfonos y usarlas para enviar encuestas o comunicados gremiales. La ISO 27701 exige barreras técnicas efectivas que impidan el tratamiento para fines secundarios no autorizados."*

---

## CONTROL A.1.4.4: ACCURACY AND QUALITY (EXACTITUD Y CALIDAD)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall ensure and document that PII is as accurate, complete and up to date as necessary for the purposes for which it is processed, throughout the life cycle of the PII."*
> *(La organización debe garantizar y documentar que los datos personales sean exactos, completos y actualizados según sea necesario para los fines de su tratamiento, a lo largo de todo su ciclo de vida).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Los datos deben ser correctos, verdaderos y mantenerse al día. Un error en una letra del apellido, un número de DNI o un correo desactualizado puede causar que un alumno sea perjudicado en la emisión de su título, pierda una beca o reciba sanciones por error de identidad.
* **Analogía de la vida real:** Si en un banco escriben mal un dígito de tu documento de identidad y por ese error transfieren tu sueldo a un desconocido o te reportan erróneamente a una central de riesgos crediticios.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE.
* **Sustento Legal y Técnico Peruano:**
  * **Principio de Calidad** (Art. 8 Ley 29733 y Art. 14 D.S. 016-2024-JUS): los datos deben ser veraces, exactos y actualizarse permanentemente. Art. 47 de la Ley Universitaria 30220 sobre emisión fidedigna de grados y títulos ante SUNEDU.
  * **Estado en la UNSA:** Cumplimiento moderado (Nivel 3). Existe interoperabilidad con RENIEC mediante la PIDE para validar DNI y nombres en grados y títulos, pero los datos de contacto (número celular, domicilio actual, correos de emergencia) se encuentran severamente desactualizados en el SISCA.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Integración a la Plataforma de Interoperabilidad del Estado Peruano (PIDE) promovida por la Presidencia del Consejo de Ministros (PCM) para validación de identidad con el Registro Nacional de Identificación y Estado Civil (RENIEC).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En la postulación al examen de admisión, al inicio de cada proceso de matrícula y previo a la emisión de grados de bachiller y título profesional.
  * **HOW (Cómo):** Mediante consumo de web services SOAP/REST de RENIEC a través de la PIDE, sincronizando automáticamente nombres, apellidos, fecha de nacimiento y estado civil; y habilitando un portal de auto-actualización obligatoria de datos de contacto cada semestre.
  * **WHO (Quién):** Oficina de Grados y Títulos, Dirección Universitaria de Informática y Comunicaciones (DUIC) y Mesa de Partes.
  * **WHAT (Qué entregables):** Reportes de validación de identidad digital y protocolo de cotejo de datos biográficos.
  * **WHERE (Dónde):** Módulo de Registro Académico de SISCA y pasarela de interoperabilidad institucional.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 3 (Definido en identidad formal, deficiente en datos de contacto).
* **Nivel de Riesgo:** **Medio**. Riesgo de vicios de nulidad en notificaciones administrativas o rechazo de diplomas ante SUNEDU.
* **Observación de Auditoría (GAP):** Si bien la validación de DNI está automatizada con RENIEC para títulos, el 68% de los registros de estudiantes de años avanzados en SISCA presentan teléfonos y domicilios obsoletos sin validar, impidiendo notificaciones válidas de actos administrativos.
* **Recomendaciones de Remediación:**
  1. Configurar un bloqueo de matrícula en SISCA que exija al estudiante validar o actualizar su número celular y dirección mediante verificación por código OTP (One-Time Password) semestral.
  2. Implementar un log de trazabilidad que documente quién, cuándo y con qué sustento documental modificó un dato sensible o académico en el sistema.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"En la UNSA garantizamos la calidad de los datos de nuestros estudiantes conectándonos en tiempo real con RENIEC a través de la PIDE. De este modo, los nombres y números de documento que van a SUNEDU y a los títulos universitarios son 100% exactos y coincidentes con el registro civil nacional."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Felicito la integración con RENIEC para grados y títulos, pero la calidad del dato abarca todo el ciclo de vida. Los teléfonos y domicilios de los alumnos en SISCA no se actualizan desde que postulan, lo que invalida notificaciones de bienestar o de procesos sancionadores. La exactitud debe ser integral."*

---

## CONTROL A.1.4.5: PII MINIMIZATION OBJECTIVES (OBJETIVOS DE MINIMIZACIÓN DE DATOS)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall define and document data minimization objectives and what mechanisms (such as de-identification) are used to meet those objectives."*
> *(La organización debe definir y documentar objetivos de minimización de datos y qué mecanismos (como la desidentificación) se utilizan para cumplir dichos objetivos).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** La organización debe establecer metas formales y escritas para reducir la cantidad de datos personales que maneja en sus sistemas, y definir técnicas específicas (como seudonimizar o disociar) para que los sistemas procesen identificadores ficticios en vez de los datos reales de las personas.
* **Analogía de la vida real:** Una empresa que se propone la meta de reducir el consumo de papel en 50% este año y compra destructoras y software digital para lograrlo. Aquí la meta es reducir el volumen de datos personales y usar códigos en lugar de nombres.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA.
* **Sustento Legal y Técnico Peruano:**
  * Fomento expreso de la **Seudonimización y Disociación** en el D.S. N° 016-2024-JUS como salvaguarda técnica fundamental de privacidad desde el diseño.
  * **Estado en la UNSA:** No implementado formalmente (Nivel 1). No existen objetivos métricos ni directivas documentadas en el Plan de Gobierno Digital de la UNSA para desidentificar datos en investigaciones o proyectos de software.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Plan de Gobierno Digital Institucional y políticas de ciencia abierta del CONCYTEC para proyectos de investigación con datos estadísticos.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Al formular la arquitectura de software de nuevos sistemas y al suministrar conjuntos de datos para tesistas o estudios del Vicerrectorado de Investigación (VRI).
  * **HOW (Cómo):** Aplicando algoritmos criptográficos hash (SHA-256) sobre los números de DNI para generar identificadores unívocos opacos (tokens/UUID) que permitan análisis estadístico sin exponer la identidad personal.
  * **WHO (Quién):** Vicerrectorado de Investigación (VRI), Comité de Gobierno Digital y Equipo de Desarrollo de Software de la DUIC.
  * **WHAT (Qué entregables):** Política Universitaria de Minimización y Seudonimización de Datos y catálogo de datasets desidentificados.
  * **WHERE (Dónde):** En el repositorio de datos de investigación y servidores analíticos de la UNSA.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 1 (Inicial / Ad-hoc).
* **Nivel de Riesgo:** **Alto**. Riesgo de exposición masiva de identidad en papers científicos o tesis de grado.
* **Observación de Auditoría (GAP):** En las investigaciones cuantitativas de las facultades de Medicina, Enfermería y Ciencias Sociales de la UNSA se manipulan bases de datos reales en hojas de cálculo sin aplicar mecanismos de seudonimización ni contar con metas documentadas de minimización.
* **Recomendaciones de Remediación:**
  1. Definir formalmente en la política de SGSI/SGIP un indicador clave de desempeño (KPI): *"100% de datasets entregados para fines de investigación o evaluación docente deben ser seudonimizados mediante tokenización reversible restringida al Oficial de Datos"*.
  2. Implementar entornos de prueba (Staging/QA) donde la data de producción esté completamente ofuscada mediante técnicas de enmascaramiento estático de datos (Static Data Masking).

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"La universidad está incorporando la desidentificación como estándar de trabajo. En las investigaciones del Vicerrectorado de Investigación y en la analítica de deserción estudiantil, los nombres y DNI son sustituidos por identificadores aleatorios, permitiendo que la ciencia avance sin comprometer la identidad de los estudiantes."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Actualmente no hay ninguna meta documentada en la UNSA para minimizar datos. Encontré bases de datos de pacientes del policlínico universitario y de notas compartidas con tesistas en texto claro. La norma exige metas claras de minimización y tecnologías de seudonimización antes de explotar la información."*

---

## CONTROL A.1.4.6: PII DE-IDENTIFICATION AND DELETION AT END OF PROCESSING (DESIDENTIFICACIÓN Y ELIMINACIÓN AL FINAL DEL TRATAMIENTO)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall either delete PII or render it in a form which does not permit identification or re-identification of PII principals, as soon as the original PII is no longer necessary for the identified purpose(s)."*
> *(La organización debe eliminar los datos personales o transformarlos de manera que no permita la identificación o reidentificación de los titulares, tan pronto como los datos originales ya no sean necesarios para los fines identificados).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Cuando se cumple la meta por la cual te entregaron un dato (por ejemplo, terminó el examen de admisión para los postulantes que no ingresaron), la institución tiene que borrar esos datos de forma irreversible o anonimizarlos para que nadie pueda volver a saber a quién pertenecían.
* **Analogía de la vida real:** Tratar en una trituradora el contrato de alquiler cuando ya te mudaste, devolviste la llave y liquidaste las garantías, o borrar las cintas de videovigilancia de un restaurante pasados los 30 días reglamentarios.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA.
* **Sustento Legal y Técnico Peruano:**
  * Exigencia del Art. 21 de la Ley N° 29733 (Cancelación por cumplimiento de finalidad) y Art. 19 del D.S. N° 016-2024-JUS (Bloqueo y posterior supresión o anonimización irreversible).
  * **Estado en la UNSA:** Deficiente (Nivel 1). Los datos biométricos, fotografías, domicilios y certificados de postulantes no admitidos a procesos de admisión se acumulan en bases de datos desde hace más de una década sin que exista un proceso de depuración o anonimización.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Normas del Archivo General de la Nación (AGN) sobre depuración de documentos auxiliares y directivas de la ANPDP sobre disociación definitiva.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** A los doce (12) meses de culminado cada proceso de admisión ordinario o extraordinario, respecto de los postulantes que no obtuvieron vacante.
  * **HOW (Cómo):** Mediante rutinas SQL programadas que anonimizan los registros (transformando nombres y DNI en cadenas nulas o hash no reversibles) y eliminan del storage las imágenes faciales y huellas dactilares, reteniendo únicamente estadísticas agregadas de postulaciones.
  * **WHO (Quién):** Oficina Universitaria de Admisión en coordinación técnica con la DUIC y el Archivo Central.
  * **WHAT (Qué entregables):** Script automatizado de anonimización y Acta de Depuración Segura de Bases de Datos de Postulantes.
  * **WHERE (Dónde):** En la base de datos MySQL/PostgreSQL del sistema de admisión y servidores de almacenamiento de imágenes adjuntas.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 1.
* **Nivel de Riesgo:** **Alto**. Riesgo de contingencia legal por almacenar datos sensibles y biométricos de menores de edad (postulantes escolares) sin necesidad legítima.
* **Observación de Auditoría (GAP):** Se evidenció la presencia de más de 120,000 registros de postulantes no ingresantes de los años 2015 al 2024 con fotos de alta resolución, huellas biométricas e información familiar completa almacenados sin cifrar ni anonimizar.
* **Recomendaciones de Remediación:**
  1. Ejecutar de inmediato una purga controlada con técnicas de anonimización estadística para los postulantes no admitidos de periodos anteriores a 2024.
  2. Documentar e institucionalizar el procedimiento de "Disociación Automatizada de Postulantes no Ingresantes" con aprobación de Consejo Universitario.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"Entendemos que los postulantes que no ingresaron a la universidad no tienen por qué permanecer fichados indefinidamente. La UNSA está estableciendo un protocolo de anonimización para que, pasado un año del examen, sus datos biométricos y personales se eliminen, conservando únicamente indicadores de vacantes y postulaciones."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Tener almacenadas huellas y fotos de 120,000 postulantes que no ingresaron hace años es un pasivo gravísimo. Si esa base de datos sufre una filtración, la universidad enfrentará demandas colectivas y multas astronómicas. Cumplir el control A.1.4.6 exige anonimizar o destruir cuando el fin concluye."*

---

## CONTROL A.1.4.7: TEMPORARY FILES (ARCHIVOS TEMPORALES)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall ensure that temporary files created as a result of the processing of PII are disposed of (e.g. erased or destroyed) following documented procedures within a specified, documented period."*
> *(La organización debe garantizar que los archivos temporales creados como resultado del tratamiento de datos personales se eliminen (p. ej., se borren o destruyan) siguiendo procedimientos documentados dentro de un período específico y documentado).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Cuando un sistema informático trabaja (por ejemplo, al exportar un listado de notas a Excel, generar un carné en PDF o procesar un pago), crea archivos temporales en el disco duro o en el servidor. Esos archivos deben ser borrados automáticamente y no quedarse tirados en carpetas olvidadas donde cualquiera pueda abrirlos.
* **Analogía de la vida real:** Fotocopiar tu DNI en un centro de copiado y que el encargado deje una copia adicional en la bandeja o en el tacho de basura sin triturar al alcance de cualquier cliente que entre después de ti.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Directiva de Seguridad de la Información (ANPDP), acápite de gestión de soportes y almacenamiento seguro; Art. 38 del D.S. N° 016-2024-JUS sobre medidas de seguridad en el ciclo de vida del dato.
  * **Estado en la UNSA:** Cumplimiento parcial/informal (Nivel 2). Los servidores web del SISCA y las computadoras del personal administrativo acumulan exportaciones temporales en formatos `.xlsx`, `.csv` y `.pdf` en las carpetas de descargas y directorios `/tmp` sin políticas de limpieza periódica.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Buenas prácticas de administración de servidores gubernamentales promovidas por el Centro Nacional de Seguridad Digital (CNSD) de la PCM.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Diariamente en ejecución automática nocturna (02:00 hrs) y al cierre de cada sesión de procesamiento de reportes.
  * **HOW (Cómo):** Mediante tareas programadas (`cron jobs` en servidores Linux y directivas de grupo GPO en Windows) que ejecutan borrado seguro (`shred` / purga de archivos) en directorios temporales `/tmp`, `/var/www/temp/` y carpetas locales de usuario con antigüedad mayor a 24 horas.
  * **WHO (Quién):** Administradores de Sistemas e Infraestructura de la DUIC.
  * **WHAT (Qué entregables):** Script de purga automatizada de temporales y registro de ejecución (`Log de Depuración`).
  * **WHERE (Dónde):** En los servidores de aplicaciones del SISCA, contenedores Docker y computadoras de escritorio de las secretarías académicas.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2 (Parcialmente gestionado).
* **Nivel de Riesgo:** **Medio / Alto**. Riesgo de fuga de información por persistencia de copias no controladas en el servidor.
* **Observación de Auditoría (GAP):** Se encontraron más de 45 GB de archivos temporales con padrones de alumnos, notas y declaraciones juradas en el directorio temporal `/var/tmp/reports/` del servidor web principal de la UNSA, con fechas de creación que datan del año 2021.
* **Recomendaciones de Remediación:**
  1. Configurar un parámetro estricto de Tiempo de Vida (TTL) de máximo 24 horas para todos los archivos generados en directorios temporales, con sobreescritura segura.
  2. Implementar una directiva de puesto de trabajo limpio que restrinja la descarga masiva a discos duros locales en las áreas administrativas.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"En los servidores de la UNSA hemos programado tareas automáticas que barren diariamente los directorios temporales. Todo PDF o Excel generado para una consulta de trámite es destruido automáticamente a las 24 horas para no dejar rastros de datos en los discos del servidor."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"En la auditoría de servidores encontramos 45 gigabytes de reportes temporales con nombres, notas y teléfonos acumulados desde el 2021. La creación de temporales sin una rutina de destrucción documentada es una de las brechas más comunes aprovechadas por ciberdelincuentes."*

---

## CONTROL A.1.4.8: RETENTION (RETENCIÓN)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall not retain PII for longer than is necessary for the purposes for which the PII is processed."*
> *(La organización no debe retener datos personales por más tiempo del necesario para los fines para los cuales son tratados).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** La organización debe definir una fecha de caducidad para los datos que guarda. No puede guardar todo para siempre; cuando la necesidad legal o de servicio termina, la información debe eliminarse o archivarse de forma restringida.
* **Analogía de la vida real:** Guardar en la gaveta de tu casa las recetas médicas de la gripe que tuviste a los 6 años cuando ya eres un adulto de 35 años. No tiene ningún sentido ni utilidad médica conservarlas activas.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA (Con armonización normativa especial).
* **Sustento Legal y Técnico Peruano:**
  * **Principio de Limitación del Plazo de Conservación** (Art. 13 D.S. N° 016-2024-JUS).
  * *Intersección jurídica especial:* La Ley Universitaria 30220 y las normas del Archivo General de la Nación (AGN) exigen conservación histórica permanente de actas de notas y grados académicos; sin embargo, datos de salud estudiantil, grabaciones de videovigilancia y registros de visitas deben tener plazos estrictos de retención y eliminación.
  * **Estado en la UNSA:** Cumplimiento parcial (Nivel 2). La universidad tiende a asumir erróneamente que "todo debe guardarse por siempre", conservando videos de vigilancia y fichas de salud pasadas sin categorización.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Tabla de Retención Documental del Sistema Nacional de Archivos del Perú y lineamientos de acreditación de SUNEDU.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Al momento del diseño de las bases de datos y en la revisión semestral del inventario de bancos de datos personales.
  * **HOW (Cómo):** Aprobando la Tabla de Retención y Conservación de Datos Personales de la UNSA, estableciendo periodos diferenciados: Actas de notas (Permanente), Grabaciones de cámaras de seguridad (45 días calendario), Datos médicos de bienestar (5 años post egreso), Registros de control de acceso físico (1 año).
  * **WHO (Quién):** Archivo Central de la UNSA, Secretaría General, Dirección de Asuntos Académicos y Oficial de Seguridad de la Información.
  * **WHAT (Qué entregables):** Política Universitaria de Retención de Datos y Tabla de Plazos de Conservación por Banco de Datos.
  * **WHERE (Dónde):** En el Archivo Central institucional y en las bases de datos transaccionales del SISCA y sistemas de videovigilancia.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2.
* **Nivel de Riesgo:** **Alto**. Riesgo de sanciones de la ANPDP por retención excesiva de datos de terceros ajenos a la función histórica de archivo.
* **Observación de Auditoría (GAP):** No existe un documento formal que regule el ciclo de retención de datos en la UNSA. Se guardan grabaciones de cámaras de seguridad de años pasados y legajos de personal jubilado de hace décadas en servidores accesibles desde la red interna sin políticas de caducidad.
* **Recomendaciones de Remediación:**
  1. Diseñar y someter a aprobación del Consejo Universitario la Tabla de Retención de Datos Personales armonizada con la Ley 29733 y la Ley del Sistema Nacional de Archivos.
  2. Implementar purga lógica automática en el sistema de videovigilancia para sobreescribir grabaciones mayores a 45 días calendario.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"La UNSA custodia la historia académica de Arequipa y por ley de SUNEDU nuestras actas de notas son eternas. No obstante, en cumplimiento de la ISO 27701, hemos normado que los datos no académicos, como videos de seguridad y citas médicas de bienestar, caduquen y se eliminen en plazos definidos."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Es un error común en la administración pública creer que todo dato es eterno. Las notas se guardan permanentemente por ley, pero mantener videos de vigilancia de hace 3 años o fichas de postulantes de hace una década vulnera el principio de limitación de conservación de la norma internacional."*

---

## CONTROL A.1.4.9: DISPOSAL (ELIMINACIÓN / DESECHO SEGURO)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall have documented policies, procedures or mechanisms for the disposal of PII."*
> *(La organización debe disponer de políticas, procedimientos o mecanismos documentados para la eliminación de datos personales).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Cuando llega el momento de botar información personal, no puedes simplemente mandar el papel al tacho de basura o poner "eliminar archivo" en Windows. Debe existir un procedimiento formal de destrucción segura (trituración física de papeles o borrado magnético de discos) que garantice que nadie pueda reconstruir la información.
* **Analogía de la vida real:** Si vas a deshacerte de tus tarjetas de crédito viejas o estados de cuenta bancarios, no los dejas intactos en la bolsa de basura de la calle; los cortas en pedacitos diminutos con una tijera o los quemas para evitar que los recolectores de basura te roben la identidad.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA OBLIGATORIAMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Directiva de Seguridad de la Información (R.D. 019-2013-JUS/DGPDP, medidas de destrucción segura de medios físicos y digitales); Arts. 38 y 39 del D.S. N° 016-2024-JUS.
  * **Estado en la UNSA:** No implementado formalmente (Nivel 1). Los discos duros dados de baja en Control Patrimonial se almacenan o rematan sin formateo de bajo nivel certificado, y se han detectado fichas de exámenes y matrículas arrojadas en sacos de basura comunes en los pabellones.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Directiva del Organismo Supervisor de las Contrataciones del Estado (OSCE) y la Superintendencia Nacional de Bienes Estatales (SBN) sobre baja y disposición final de bienes muebles estatales (RAEE).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En los procesos anuales de baja patrimonial de equipos de cómputo y en la depuración periódica de archivos documentales caducos.
  * **HOW (Cómo):** Aplicando borrado criptográfico y sobreescritura de 3 pasos (estándar NIST SP 800-88 / DoD 5220.22-M) para medios magnéticos mediante software certificado (`DBAN` / `BleachBit`), y contratando trituración industrial de corte cruzado (Norma DIN 66399 Nivel P-4) para documentos impresos.
  * **WHO (Quién):** Oficina de Control Patrimonial en coordinación obligatoria con el Área de Soporte Técnico de la DUIC y el Oficial de Seguridad.
  * **WHAT (Qué entregables):** Procedimiento Operativo Estándar (POE) de Destrucción Segura de Medios y Actas Notariadas de Destrucción de Soportes.
  * **WHERE (Dónde):** En los almacenes centrales de Control Patrimonial (Parque Industrial) y en los centros de datos de la DUIC.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 1 (Inicial).
* **Nivel de Riesgo:** **Crítico**. Riesgo inminente de fuga masiva de datos por técnicas de "Dumpster Diving" (recolección de basura) o recuperación forense de discos en desuso.
* **Observación de Auditoría (GAP):** Se inspeccionaron computadoras dadas de baja en el almacén de patrimonio y se constató que los discos mecánicos aún contenían bases de datos de planillas de docentes y legajos de estudiantes sin ningún tratamiento de borrado seguro.
* **Recomendaciones de Remediación:**
  1. Aprobar de urgencia la "Directiva de Borrado Seguro y Disposición Final de Soportes de Almacenamiento con Datos Personales".
  2. Adquirir una máquina desmagnetizadora (Degausser) y una destructora trituradora institucional de nivel P-4 para el tratamiento de papel sensible y tarjetas plásticas.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"En la UNSA estamos modernizando los protocolos de disposición patrimonial. Ninguna computadora sale de la universidad para remate o reciclaje sin que antes la DUIC aplique un borrado seguro de nivel militar a sus discos y emita un certificado de destrucción de datos conforme a ley."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Durante la auditoría física encontramos discos duros en almacenes de patrimonio que contenían planillas y notas totalmente recuperables con herramientas gratuitas. Tirar papeles al tacho o vender PCs viejas sin borrado criptográfico certificado es una vulnerabilidad crítica que expone a la universidad a demandas millonarias."*

---

## CONTROL A.1.4.10: PII TRANSMISSION CONTROLS (CONTROLES DE TRANSMISIÓN DE DATOS)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall subject PII transmitted (e.g. sent to another organization) over a data-transmission network to appropriate controls designed to ensure that the data reaches its intended destination."*
> *(La organización debe someter los datos personales transmitidos (p. ej., enviados a otra organización) a través de una red de transmisión de datos a controles adecuados diseñados para garantizar que los datos lleguen a su destino previsto).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Cuando envías datos personales por internet o por una red entre oficinas (por ejemplo, enviando las listas de alumnos a SUNEDU, las planillas al banco o conectando la sede central con las sedes provinciales de Camaná o Mollendo), debes protegerlos para que viajen cifrados, nadie los espíe en el camino y lleguen exactamente a quien deben llegar.
* **Analogía de la vida real:** Enviar una joya valiosa o un fajo de dinero usando un camión blindado con candados digitales y custodia armada, en lugar de meterlo en un sobre abierto y enviarlo con un mensajero desconocido en bicicleta.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Directiva de Seguridad de la Información (ANPDP, medidas de seguridad en redes y telecomunicaciones: cifrado obligatorio en tránsito); Art. 40 del D.S. N° 016-2024-JUS.
  * **Estado en la UNSA:** Cumplimiento parcial (Nivel 2). Las conexiones web principales tienen certificados SSL/TLS, pero existen comunicaciones inter-sedes y envíos masivos de padrones por correo electrónico común o protocolos no cifrados (FTP o HTTP interno).

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Red Nacional del Estado Peruano (REDDAP) y directrices de interoperabilidad segura de la Secretaría de Gobierno y Transformación Digital (SGTD-PCM).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En tiempo real durante cada sesión de usuario en la red y en cada transmisión masiva de datos entre servidores o con entidades externas.
  * **HOW (Cómo):** Forzando el protocolo TLS 1.3 con suites criptográficas robustas en todos los portales web (HSTS activado), implementando túneles cifrados VPN IPsec con AES-256 entre el campus central de Arequipa y las sedes periféricas (Camaná, Mollendo, Majes), y utilizando protocolos SFTP con autenticación por llave pública para transferir datos al Banco de la Nación y SUNEDU.
  * **WHO (Quién):** Área de Redes, Servidores y Seguridad de la DUIC.
  * **WHAT (Qué entregables):** Política de Cifrado en Comunicaciones y certificados de seguridad TLS vigentes.
  * **WHERE (Dónde):** En los enlaces de fibra óptica inter-campus, enlaces WAN interprovinciales y pasarelas de red perimetrales (Firewalls Fortinet/Palo Alto).

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2.
* **Nivel de Riesgo:** **Alto**. Riesgo de ataques tipo "Man-in-the-Middle" (MitM) e intercepción de credenciales y datos estudiantiles en tránsito.
* **Observación de Auditoría (GAP):** Se detectó que funcionarios de bienestar y admisión envían hojas de cálculo con datos de alumnos por correo electrónico sin cifrado adicional, y que existen subdominios institucionales de facultades que aún operan sobre protocolo HTTP plano sin cifrar.
* **Recomendaciones de Remediación:**
  1. Habilitar la política HSTS (HTTP Strict Transport Security) de forma global en el dominio `unsa.edu.pe` para forzar HTTPS en el 100% de las comunicaciones.
  2. Implementar una solución institucional de transferencia segura de archivos (Managed File Transfer - MFT) cifrada de extremo a extremo para intercambios con el Banco de la Nación, EsSalud y SUNEDU.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"En la UNSA protegemos los datos que viajan por nuestras redes. Toda la interacción del estudiante con SISCA y con nuestras filiales de Camaná y Mollendo está protegida con cifrado TLS y túneles VPN privados, evitando que un atacante pueda interceptar información en el camino."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Si bien el portal principal tiene candado verde, identifiqué que subdominios de escuelas y transferencias de padrones a entidades bancarias se hacen por canales sin cifrado robusto o por correos vulnerables. La ISO 27701 exige controles criptográficos estrictos para que ningún dato personal viaje desnudo por la red."*

---

# BLOQUE II: SECCIÓN A.1.5 — PII SHARING, TRANSFER AND DISCLOSURE

---

## CONTROL A.1.5.2: IDENTIFY BASIS FOR PII TRANSFER BETWEEN JURISDICTIONS (IDENTIFICAR LA BASE LEGAL PARA TRANSFERENCIA TRANSFRONTERIZA)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall identify and document the relevant basis for transfers of PII between jurisdictions."*
> *(La organización debe identificar y documentar la base legal pertinente para las transferencias de datos personales entre diferentes jurisdicciones).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Si vas a enviar o alojar datos fuera de las fronteras de tu país (por ejemplo, porque contrataste el correo en la nube de Google, servidores de Microsoft Azure, Amazon AWS o convenios universitarios internacionales), debes tener un fundamento legal claro y documentado conforme a las leyes de tu país para autorizar esa salida de información.
* **Analogía de la vida real:** Si vas a mandar a tu hijo menor de edad de viaje al extranjero para un intercambio escolar, necesitas presentar un permiso notarial de viaje firmado y fundamentado ante migraciones; no puedes subirlo a un avión internacional sin sustento legal.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE Y ES CRÍTICO.
* **Sustento Legal y Técnico Peruano:**
  * Régimen de **Flujo Transfronterizo de Datos Personales** normado en el Art. 15 de la Ley N° 29733 y regulado exhaustivamente en los Arts. 65 al 72 del D.S. N° 016-2024-JUS (obligación de declarar las transferencias internacionales ante la ANPDP y verificar garantías adecuadas).
  * **Estado en la UNSA:** Incumplimiento grave (Nivel 1). La UNSA utiliza masivamente Google Workspace for Education (Gmail, Drive) y Microsoft Azure para su infraestructura cloud, cuyos centros de datos están en Estados Unidos y Europa, pero **NO tiene registrado el flujo transfronterizo ante el Ministerio de Justicia y Derechos Humanos (ANPDP)**.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Directivas de la ANPDP sobre Flujo Transfronterizo y Marco de Adopción de Nube de la Secretaría de Gobierno y Transformación Digital (SGTD-PCM).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Con carácter previo a la contratación de cualquier servicio cloud y anualmente en la actualización del Registro Nacional de Bancos de Datos Personales.
  * **HOW (Cómo):** Suscribiendo con los proveedores tecnológicos Cláusulas Contractuales Tipo (Standard Contractual Clauses - SCC) avaladas por la ANPDP, documentando la necesidad operativa del servicio educativo y presentando el formulario oficial de notificación de flujo transfronterizo ante el MINJUSDH.
  * **WHO (Quién):** Oficina de Asesoría Jurídica, DUIC y el Oficial de Protección de Datos Personales de la UNSA.
  * **WHAT (Qué entregables):** Expediente de Análisis de Impacto de Transferencia Internacional (TIA) y Registro de Flujo Transfronterizo ante la ANPDP.
  * **WHERE (Dónde):** En la Dirección de Registro de la Autoridad Nacional de Protección de Datos Personales (Lima/Mesa Virtual) y en los contratos suscritos con Google y Microsoft.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 1 (Inicial).
* **Nivel de Riesgo:** **Crítico**. Riesgo inminente de sanción pecuniaria de hasta 50 UIT (aprox. S/ 257,500) por parte de la ANPDP por operar flujo transfronterizo clandestino o no registrado.
* **Observación de Auditoría (GAP):** La UNSA almacena información de más de 27,000 alumnos y docentes en la nube de Google y Microsoft en el extranjero sin haber fundamentado la base de licitud ni haber registrado el flujo transfronterizo ante la autoridad competente.
* **Recomendaciones de Remediación:**
  1. Iniciar inmediatamente el procedimiento administrativo de comunicación de flujo transfronterizo ante la ANPDP amparándose en el Art. 67 del D.S. 016-2024-JUS (prestación de servicios tecnológicos esenciales).
  2. Obtener y archivar formalmente los Acuerdos de Privacidad de Datos (Data Processing Addendums) firmados digitalmente con Google LLC y Microsoft Corp.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"La UNSA ha adoptado tecnologías líderes como Google Workspace for Education para brindar la mejor enseñanza digital. Fundamentamos la transferencia internacional en la necesidad pedagógica y en que dichos proveedores cuentan con certificaciones de seguridad ISO 27001 y cláusulas estándar de protección internacional."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"Tener contratado a Google o Microsoft no exime a la UNSA de la ley peruana. Almacenar los datos de 27,000 agustinos en servidores de EE.UU. sin haber registrado el flujo transfronterizo ante la ANPDP es una falta grave según el nuevo reglamento D.S. 016-2024-JUS que expone a la universidad a fuertes multas."*

---

## CONTROL A.1.5.3: COUNTRIES AND INTERNATIONAL ORGANIZATIONS TO WHICH PII CAN BE TRANSFERRED (PAÍSES Y ORGANISMOS DE DESTINO)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall specify and document the countries and international organizations to which PII can possibly be transferred."*
> *(La organización debe especificar y documentar los países y las organizaciones internacionales a los que posiblemente se transfieran los datos personales).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** La organización debe tener una lista oficial, pública y clara de a qué países y a qué instituciones del exterior viajan o pueden viajar los datos personales. No puede haber misterio ni ambigüedad sobre en qué lugares del mapa mundial terminan los datos.
* **Analogía de la vida real:** Si depositas tu dinero en una cooperativa de ahorros, tienes derecho a saber si tu dinero está custodiado en Perú o si lo han colocado en fondos de inversión en Panamá o las Islas Caimán.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA.
* **Sustento Legal y Técnico Peruano:**
  * **Principio de Información** (Art. 18 Ley 29733 y Art. 15 D.S. 016-2024-JUS): los titulares deben ser informados expresamente de los destinatarios nacionales e internacionales de sus datos.
  * **Estado en la UNSA:** Cumplimiento deficiente (Nivel 2). La UNSA mantiene convenios de doble titulación, investigación y movilidad con universidades de EE.UU. (Purdue University), España, Francia (Erasmus+) y la Alianza del Pacífico, pero ningún alumno de intercambio es informado documentalmente sobre qué jurisdicciones foráneas custodiarán sus datos ni con qué nivel de protección.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Convenios bilaterales universitarios aprobados en el marco de la Ley Universitaria 30220 y directrices de internacionalización de SUNEDU.
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Al momento de celebrar cada convenio de cooperación internacional y en las convocatorias semestrales de becas de movilidad académica.
  * **HOW (Cómo):** Creando y publicando el Catálogo Institucional de Países y Organismos Receptores de Datos, indicando si el país receptor cuenta con un nivel adecuado de protección (reconocido por la ANPDP o la Comisión Europea) o si se aplican salvaguardas contractuales específicas.
  * **WHO (Quién):** Dirección Universitaria de Cooperación, Convenios y Relaciones Internacionales (DUCCRI) y Asesoría Jurídica.
  * **WHAT (Qué entregables):** Anexo Informativo de Transferencias Internacionales incorporado en las bases de postulación a becas y convenios.
  * **WHERE (Dónde):** En el Portal de Transparencia de la UNSA y en los contratos de becas de movilidad internacional.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2.
* **Nivel de Riesgo:** **Medio**. Riesgo de reclamos ante la ANPDP por falta de transparencia informativa respecto al destino geográfico de datos.
* **Observación de Auditoría (GAP):** No se encuentra publicado ni formalizado el listado de países destinatarios de datos personales derivados de las plataformas en la nube ni de los programas de movilidad estudiantil con Purdue, convenios Erasmus o la Alianza del Pacífico.
* **Recomendaciones de Remediación:**
  1. Especificar en la Política de Privacidad de la web de la UNSA los países receptores de datos: Estados Unidos (Google/Azure/Purdue), España (Convenios de doble grado), Colombia/México/Chile (Alianza del Pacífico).
  2. Evaluar el nivel de adecuación de privacidad de cada destino conforme a la lista oficial de países con nivel adecuado emitida por la ANPDP.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"La UNSA es una universidad con presencia global que fomenta pasantías con Estados Unidos y Europa. Mapeamos formalmente cada país receptor de convenios, garantizando que cuando un estudiante viaja a Purdue o a la Complutense de Madrid, su información personal sea tratada con estándares internacionales de privacidad."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"El control A.1.5.3 exige que los países destinatarios estén claramente especificados y documentados. Actualmente, ningún estudiante agustino sabe con certeza en qué servidores del mundo están sus notas y correos ni qué países procesan sus legajos de intercambio. La transparencia geográfica es un deber normativo."*

---

## CONTROL A.1.5.4: RECORDS OF TRANSFER OF PII (REGISTROS DE TRANSFERENCIAS DE DATOS)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall record transfers of PII to or from third parties and ensure cooperation with those parties to support future requests related to obligations to the PII principals."*
> *(La organización debe registrar las transferencias de datos personales hacia o desde terceros y garantizar la cooperación con dichas partes para respaldar futuras solicitudes relacionadas con las obligaciones hacia los titulares de los datos).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Cada vez que entregas datos personales a un tercero (por ejemplo, al Banco de la Nación para cobros, a una compañía de seguros estudiantiles o a una clínica), debes llevar una bitácora que registre exactamente qué datos entregaste, a quién y en qué fecha; y además tener un contrato firmado donde el tercero se comprometa a ayudarte si un alumno pide borrar, corregir o acceder a sus datos.
* **Analogía de la vida real:** El cuaderno de control de una garita de seguridad de un condominio privado: toda persona o empresa de mudanza que retira un mueble debe firmar fecha, hora, placa del camión y autorización, para que si un propietario reclama, la administración sepa a quién pedir cuentas y cooperar en la recuperación.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA TOTALMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Régimen de los **Encargados del Tratamiento** y deber de diligencia (Arts. 50 al 54 del D.S. N° 016-2024-JUS): exigencia de contratos formales de encargo que regulen la cooperación y prohibición de uso para fines propios.
  * **Estado en la UNSA:** Incumplimiento crítico (Nivel 1). Se transfieren bases de datos de estudiantes y docentes al Banco de la Nación (recaudación y tarjetas), aseguradoras de accidentes y clínicas privadas sin una bitácora centralizada de envíos ni convenios que obliguen al tercero a responder a solicitudes de derechos ARCO en plazos legales.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Ley de Contrataciones del Estado (Ley 30225) y directivas de recaudación de tesorería del Ministerio de Economía y Finanzas (MEF).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** En cada remisión periódica de padrones a terceros y al momento de suscribir contratos o convenios de cooperación con entidades financieras o de seguros.
  * **HOW (Cómo):** Implementando el Libro Digital de Registro de Transferencias Externas de Datos y anexando a todos los contratos la "Adenda de Protección de Datos Personales y Cláusula de Deber de Cooperación ARCO".
  * **WHO (Quién):** Oficina de Abastecimiento, Dirección General de Administración (DGA), DUIC y Secretaría General.
  * **WHAT (Qué entregables):** Bitácora Inmutable de Transferencias Masivas y Contratos con Cláusulas de Encargo de Tratamiento (Data Processing Agreements - DPA).
  * **WHERE (Dónde):** En el Sistema Integrado de Gestión Administrativa de la UNSA y módulo de logs de la DUIC.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 1.
* **Nivel de Riesgo:** **Alto**. Riesgo de responsabilidad solidaria ante la ANPDP por infracciones cometidas por terceros contratados.
* **Observación de Auditoría (GAP):** La UNSA carece de una bitácora formal de transferencias de datos. Se remiten archivos planos con datos de matrícula a aseguradoras y empresas de transporte sin dejar constancia del hash de integridad del archivo entregado ni estipular el deber de asistencia mutua frente a solicitudes ARCO.
* **Recomendaciones de Remediación:**
  1. Crear un sistema centralizado de registro de remisiones de datos que capture: fecha, destinatario, volumen de registros, justificación legal y funcionario autorizante.
  2. Modificar las bases estándar de contratación pública de la UNSA para incluir como requisito indispensable la Cláusula de Cooperación frente a Derechos ARCO bajo penalidad contractual.

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"Cada vez que la UNSA coordina con el Banco de la Nación para las pensiones o con la aseguradora de salud estudiantil, aseguramos la trazabilidad de los datos entregados y exigimos convenios donde el proveedor se compromete a respetar la confidencialidad y atender cualquier reclamo del alumno."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"En la auditoría solicité el registro de transferencias a empresas de seguros y bancos del último ciclo y no existía un libro de actas ni log de envíos. Si un alumno pide cancelar sus datos y el tercero contratado se niega a cooperar, la UNSA es legalmente responsable por falta de diligencia."*

---

## CONTROL A.1.5.5: RECORDS OF PII DISCLOSURES TO THIRD PARTIES (REGISTROS DE DIVULGACIONES A TERCEROS)

### 1. Texto Normativo (ISO/IEC 27701:2025)
> *"The organization shall record disclosures of PII to third parties, including which PII has been disclosed, to whom and at what time."*
> *(La organización debe registrar las divulgaciones de datos personales a terceros, incluyendo qué datos personales se han divulgado, a quién y en qué momento).*

### 2. Explicación General del Control
* **¿Qué significa en lenguaje sencillo?:** Si la organización tiene que entregar información personal por mandato legal (por ejemplo, porque la Policía, la Fiscalía, el Poder Judicial, la SUNAT o un ciudadano mediante la Ley de Transparencia piden un expediente), se debe llevar un registro estricto que anote: qué datos exactos se dieron, a qué autoridad o persona, qué día y a qué hora.
* **Analogía de la vida real:** Si la policía llega a pedir las grabaciones de seguridad de un edificio por una investigación penal, el conserje no les entrega el USB sin anotar en el libro de actas el número de placa del patrullero, el nombre del fiscal, la orden judicial y la hora exacta de entrega.

### 3. ¿Aplica en la UNSA y cuál es su estado actual?
* **Diagnóstico de Aplicabilidad:** SÍ APLICA OBLIGATORIAMENTE.
* **Sustento Legal y Técnico Peruano:**
  * Excepciones al consentimiento por mandato judicial o legal (Art. 14 Ley 29733); Ley N° 27806 (Ley de Transparencia y Acceso a la Información Pública); Arts. 23 y 24 del D.S. N° 016-2024-JUS sobre deber de registro de excepciones y confidencialidad.
  * **Estado en la UNSA:** Cumplimiento parcial (Nivel 2). La Secretaría General responde oficios judiciales y solicitudes de transparencia, pero no existe una base de datos centralizada de divulgaciones de datos personales; en muchas facultades, decanos o directores entregan listas a comisarías locales sin dejar registro central.

### 4. Perspectiva de la Universidad (UNSA) — Implementación
* **Marco y Antecedentes Estatales:** Portal de Transparencia Estándar (PTE) del Estado Peruano y directivas del Tribunal de Transparencia y Acceso a la Información Pública (TTAIP).
* **Modelo Operativo 5W:**
  * **WHEN (Cuándo):** Inmediatamente al momento de notificar la respuesta a un mandato judicial, requerimiento fiscal, fiscalización de SUNAT o pedido ciudadano de acceso a la información.
  * **HOW (Cómo):** Tipificando en el Sistema de Gestión Documentaria (SGD UNSA) el tipo de expediente *"Divulgación de Datos Personales por Mandato Legal"*, donde se adjunta el oficio judicial, se listan los campos revelados y se estampa firma digital con sello de tiempo del funcionario responsable.
  * **WHO (Quién):** Secretaría General, Mesa de Partes Central y Dirección de Asesoría Jurídica.
  * **WHAT (Qué entregables):** Libro de Registro Digital de Revelaciones y Divulgaciones Institucionales de Datos Personales.
  * **WHERE (Dónde):** En el Sistema de Gestión Documentaria (SGD) de la UNSA y repositorio seguro de resoluciones y oficios.

### 5. Perspectiva del Auditor (Ing. Rafael)
* **Estado de Madurez:** Nivel 2.
* **Nivel de Riesgo:** **Alto**. Riesgo de demandas por violación del secreto profesional o entrega ilegítima de datos personales sin amparo procesal.
* **Observación de Auditoría (GAP):** Se evidenciaron casos donde directores de departamento respondieron directamente oficios policiales remitiendo direcciones domiciliarias y teléfonos de docentes o estudiantes sin pasar por el filtro legal de Secretaría General ni registrar los datos específicos entregados en una bitácora institucional.
* **Recomendaciones de Remediación:**
  1. Emitir una resolución rectoral que prohíba expresamente a facultades y escuelas entregar información personal directamente a terceros sin validación jurídica centralizada.
  2. Implementar un módulo obligatorio en el SGD que impida cerrar un oficio de requerimiento fiscal sin antes consignar los metadatos requeridos por el control A.1.5.5 (Quién, Qué datos exactos, Cuándo y Base legal).

### 6. Guiones de Exposición Oral
* **Guión Como Universidad (UNSA):**
  > *"Toda entrega de información requerida por el Poder Judicial, la Fiscalía o pedidos de transparencia se gestiona a través de Secretaría General. Dejamos constancia documentada del número de oficio, la autoridad solicitante y la fecha exacta de entrega, resguardando la legalidad institucional."*
* **Guión Como Auditor (Ing. Rafael):**
  > *"He encontrado que en las facultades se entregan fichas de alumnos a la policía o a particulares por simple petición escrita en ventanilla sin registrar qué datos se expusieron. El control A.1.5.5 exige una bitácora inmutable: qué dato se dio, a quién y en qué segundo exacto, para evitar abusos y filtraciones ilegales."*

---

## CONCLUSIONES FINALES Y DICTAMEN DEL AUDITOR LÍDER

1. **Diagnóstico General de los Bloques A.1.4 y A.1.5:**
   * La Universidad Nacional de San Agustín (UNSA) presenta un nivel de madurez promedio de **1.62 sobre 5 (Nivel Inicial con prácticas gestionadas informalmente)**.
   * Las mayores debilidades críticas radican en la **omisión del registro de flujo transfronterizo ante la ANPDP (A.1.5.2)**, la **ausencia de procedimientos de borrado seguro y destrucción patrimonial (A.1.4.9)** y la **acumulación histórica indefinida de datos de postulantes y archivos temporales (A.1.4.6 y A.1.4.7)**.

2. **Articulación Estratégica con el Proyecto TIF-DSAR:**
   * Los controles de esta sección cierran el círculo de protección de los datos que son solicitados a través del agente de IA para DSAR. 
   * Mientras que la Sección A.1.3 empodera al titular para ejercer sus derechos de acceso, rectificación y supresión, los controles de las secciones **A.1.4 (Minimización, Retención y Desecho)** y **A.1.5 (Transferencias y Divulgaciones)** establecen los límites técnicos y las fronteras operativas del tratamiento de datos en la UNSA.

3. **Dictamen de Auditoría (Ing. Rafael, Lead Auditor):**
   * Se emite una calificación de **NO CONFORMIDAD MAYOR** respecto al control **A.1.5.2 (Flujo Transfronterizo)** y **A.1.4.9 (Disposición Segura)**, otorgándose un plazo perentorio de 60 días calendario para la regularización de registros ante la ANPDP y la aprobación institucional de las directivas de ciclo de vida de la información.
