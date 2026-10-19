# 📋 ISO/IEC 27701:2025 — TABLA A.1 (PII CONTROLLERS)
## Sección: Obligaciones hacia los Titulares de PII (Obligations to PII Principals)
### Caso de Estudio: Universidad Nacional de San Agustín de Arequipa (UNSA)

---

> **Objetivo de la Sección A.1.3 (ISO/IEC 27701:2025):**  
> *"To ensure that PII principals are provided with appropriate information about the processing of their PII, and to meet any other applicable obligations to PII principals related to the processing of their PII."*  
> *(Garantizar que los titulares de PII reciban la información adecuada sobre el tratamiento de sus datos personales y cumplir con todas las demás obligaciones aplicables relacionadas con dicho tratamiento, en especial el ejercicio de Derechos ARCO).*

---

## 📑 ÍNDICE DE CONTROLES ANALIZADOS
1. [A.1.3.2 — Determining and fulfilling obligations to PII principals (Determinar y cumplir obligaciones hacia los titulares)](#control-a132--determining-and-fulfilling-obligations-to-pii-principals)
2. [A.1.3.3 — Determining information for PII principals (Determinar la información para los titulares)](#control-a133--determining-information-for-pii-principals)
3. [A.1.3.4 — Providing information to PII principals (Proporcionar información a los titulares)](#control-a134--providing-information-to-pii-principals)
4. [A.1.3.5 — Providing mechanism to modify or withdraw consent (Mecanismo para modificar o revocar consentimiento)](#control-a135--providing-mechanism-to-modify-or-withdraw-consent)
5. [A.1.3.6 — Providing mechanism to object to PII processing (Mecanismo para oponerse al tratamiento - Derecho de Oposición)](#control-a136--providing-mechanism-to-object-to-pii-processing)
6. [A.1.3.7 — Access, correction or erasure (Acceso, rectificación o supresión - Derechos ARCO)](#control-a137--access-correction-or-erasure)
7. [A.1.3.8 — PII controllers' obligations to inform third parties (Obligación de informar a terceros cesionarios)](#control-a138--pii-controllers-obligations-to-inform-third-parties)
8. [A.1.3.9 — Providing copy of PII processed (Proporcionar copia de la PII tratada - Derecho de Acceso / Portabilidad)](#control-a139--providing-copy-of-pii-processed)
9. [A.1.3.10 — Handling requests (Gestión y resolución de solicitudes DSAR)](#control-a1310--handling-requests)
10. [A.1.3.11 — Automated decision making (Decisiones automatizadas y perfilamiento)](#control-a1311--automated-decision-making)
11. [Matriz Global de Madurez, Riesgos y Hoja de Ruta TIF-DSAR](#matriz-global-y-hoja-de-ruta)

---

---

# CONTROL A.1.3.2 — Determining and fulfilling obligations to PII principals
### *« Determinar y cumplir obligaciones hacia los titulares de PII »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall determine and document its legal, regulatory and business obligations to PII principals related to the processing of their PII and provide the means to meet these obligations."*  
> *(La organización debe determinar y documentar sus obligaciones legales, regulatorias y operativas hacia los titulares de PII relacionadas con el tratamiento de sus datos, y proporcionar los medios para cumplir con estas obligaciones).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Antes de esperar a que un usuario venga a quejarse o pedir algo, la organización debe tener una lista oficial y completa de **TODOS LOS DERECHOS Y DEBERES** que tiene frente a los dueños de los datos (alumnos, docentes, clientes), y debe asegurar el presupuesto, los sistemas y el personal para cumplirlos.
* **Analogía de la vida real:** Si abres una aerolínea comercial, la ley de aviación te exige respetar los derechos de los pasajeros (reembolsos por vuelos cancelados, transporte de equipaje, atención médica a bordo). No puedes decir "no sabía que tenía que reembolsar pasajes"; tienes que documentar esas obligaciones en tu manual de operaciones y poner módulos de atención al cliente en el aeropuerto con personal capacitado.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO ⚠️**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA está obligada por la **Ley N° 29733** y el **D.S. N° 016-2024-JUS** a respetar los derechos de los titulares. En el Portal de Transparencia Estándar y en su portal web cuenta con una política de privacidad básica que menciona que existen los derechos ARCO.
  * **¿Por qué está parcialmente implementado?:** Porque solo los menciona como texto informativo genérico. No tiene una **Directiva Institucional aprobada por Resolución Rectoral** que establezca los "medios operativos" (*provide the means*): no hay ventanilla especializada, ni presupuesto asignado, ni plazos internos definidos para responder.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Marco Legal Peruano Aplicable
* **Ley N° 29733** (Título III: Derechos de los Titulares de Datos Personales).
* **Decreto Supremo N° 016-2024-JUS** (Reglamento: Artículos sobre deberes del titular del banco de datos públicos).
* **Ley N° 27444** (Ley del Procedimiento Administrativo General - plazos y debido procedimiento administrativo).
* **Ley N° 30220** (Ley Universitaria - deber de transparencia y servicio al estudiante).

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En los primeros **60 días calendario** del despliegue del PIMS. Revisión anual obligatoria o ante modificaciones de directivas de la ANPD.
* **HOW (Cómo):**
  1. Identificar todas las obligaciones legales derivadas de la Ley 29733 (información, acceso, rectificación, cancelación, oposición, indemnización).
  2. Redactar el **Reglamento Institucional de Protección de Datos Personales y Derechos de los Titulares de la UNSA**.
  3. Formalizar el reglamento vía Resolución Rectoral.
  4. Habilitar los canales de atención: mesa de partes presencial y módulo virtual dentro del Portal del Estudiante (SISUNSA).
* **WHO (Quién):** Oficina de Asesoría Jurídica y Secretaría General (redacción del reglamento), OTI (implementación técnica de canales), y Rectorado (aprobación).
* **WHAT (Qué entregables):**
  1. Reglamento Institucional de Derechos de los Titulares de Datos.
  2. Resolución Rectoral de aprobación y promulgación.
  3. Catálogo de obligaciones frente al estudiante, docente y personal administrativo.
* **WHERE (Dónde se ubica):** Portal de Transparencia Estándar de la UNSA, página web oficial, mesa de partes general y Secretaría General.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Perfil:** *Ing. Rafael (MSc. Ciberseguridad & Auditoría TI, Lead Auditor ISO 27001, CISA, CRISC).*
* **Observaciones de Auditoría (GAP):** La universidad reconoce que los estudiantes tienen derechos en su política web, pero no provee los medios (*means*): si un alumno acude a Mesa de Partes a pedir formalmente la cancelación de sus datos de una base secundaria, el personal administrativo no sabe qué trámite seguir ni a qué oficina derivarlo.
* **Recomendaciones:** Aprobar el Reglamento de Derechos de Titulares por Consejo Universitario y designar formalmente al Oficial de Protección de Datos (DPO) con facultades de resolución.
* **Dictamen:** **PARCIALMENTE IMPLEMENTADO ⚠️ | Nivel de Riesgo: MEDIO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"Buenas tardes, profesor y compañeros. Iniciamos la sección de **Obligaciones hacia los Titulares** con el control **A.1.3.2: Determinar y cumplir obligaciones hacia los titulares**.  
> Para la UNSA, este control significa que no basta con saber que la Ley 29733 existe; la universidad debe tener un documento oficial que liste todas sus obligaciones frente a los estudiantes, docentes y egresados, y poner los medios reales para cumplirlas.  
> Hoy en día la UNSA menciona los derechos ARCO en su página web, pero no tiene una directiva clara ni una ventanilla específica.  
> Con las 5W proponemos: emitir un Reglamento Institucional de Derechos del Titular aprobado por Resolución Rectoral (WHAT), habilitar canales en SISUNSA y mesas de partes (WHERE), liderado por Asesoría Jurídica y OTI (WHO), en un plazo de 60 días (WHEN) mediante flujos estandarizados (HOW)."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor líder, evalúo este control como **PARCIALMENTE IMPLEMENTADO con nivel de riesgo MEDIO**.  
> La norma ISO 27701 exige dos cosas: determinar las obligaciones y proveer los medios para cumplirlas (*provide the means*). La UNSA cumple lo primero a nivel teórico porque la ley peruana lo fija, pero falla en los medios: no hay personal asignado para tramitar derechos de los alumnos, ni formularios específicos, ni presupuesto para notificaciones formales. Recomiendo institucionalizar la Unidad de Protección de Datos en un plazo máximo de 60 días."*

---

---

# CONTROL A.1.3.3 — Determining information for PII principals
### *« Determinar la información a proporcionar a los titulares »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall determine and document the information to be provided to PII principals regarding the processing of their PII and the timing of such a provision."*  
> *(La organización debe determinar y documentar la información que se proporcionará a los titulares respecto al tratamiento de su PII y el momento oportuno de dicha entrega).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Tienes que definir de antemano **QUÉ DATOS EXACTOS** le vas a contar al usuario sobre el tratamiento (quién es el responsable, para qué se usan, a quién se transfieren, cuánto tiempo se guardan) y **EN QUÉ MOMENTO** se lo vas a decir (casi siempre, al momento exacto en que te entrega los datos).
* **Analogía de la vida real:** Cuando compras un medicamento en la farmacia, la ley exige que la caja contenga un prospecto con la información obligatoria: composición, dosis, efectos adversos y fecha de vencimiento. El laboratorio farmacéutico tuvo que definir con precisión qué información incluir en ese papelito antes de imprimir la caja.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO ⚠️**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * Aplica a todos los puntos de recolección de la UNSA (matrícula, admisión, bolsa de trabajo, biblioteca, tópico).
  * **Situación actual:** La UNSA redactó una política general en la web institucional, pero no ha determinado el paquete informativo obligatorio para cada punto de contacto ni el *timing* exacto. En los exámenes de admisión, por ejemplo, no se entrega información previa al postulante sobre la conservación o publicación de sus puntajes.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Contenido Mínimo Informativo Exigido por Ley 29733 (Art. 18)
1. Identidad y domicilio del titular del banco de datos (UNSA - Calle Santa Catalina N° 117).
2. Finalidad específica del tratamiento.
3. Destinatarios de transferencias (ej. SUNEDU, MINEDU, bancos recaudadores).
4. Carácter obligatorio o facultativo de cada respuesta.
5. Consecuencias de negarse a entregar los datos.
6. Tiempo de conservación previsto.
7. Posibilidad y procedimiento para ejercer Derechos ARCO.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En la fase de rediseño de formularios y procesos de recolección (plazo 45 días). Información entregada **de manera previa o simultánea** a la recolección.
* **HOW (Cómo):** Diseñar una "Estructura Informativa Multinivel": Nivel 1 (aviso corto y directo al pie del formulario con finalidad y derechos) + Nivel 2 (enlace QR o URL a la política detallada).
* **WHO (Quién):** OTI (diseño de interfaces), Asesoría Jurídica (redacción legal) y Dirección de Comunicación e Imagen Institucional.
* **WHAT (Qué entregables):**
  1. Estándar Informativo para Recolección de Datos de la UNSA.
  2. Plantillas de Avisos de Privacidad Multinivel (físicos y digitales).
  3. Matriz de Momento Informativo (*Timing Matrix*).
* **WHERE (Dónde se ubica):** Fichas de inscripción de admisión, formularios web SISUNSA, carteles informativos en áreas de videovigilancia y boletas de pago.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** En los módulos de postulación a becas de comedor y bolsas de trabajo se solicitan datos socioeconómicos íntimos sin informar previamente el tiempo que serán conservados ni si serán compartidos con el SISFOH/MIDIS.
* **Recomendaciones:** Homologar todos los formularios físicos y digitales de recolección con la estructura informativa de la Ley 29733 (Art. 18).
* **Dictamen:** **PARCIALMENTE IMPLEMENTADO ⚠️ | Nivel de Riesgo: MEDIO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"Para el control **A.1.3.3: Determinar la información para los titulares**, la universidad debe definir qué le informa al alumno y en qué momento.  
> La Ley 29733, en su artículo 18, exige que al momento de pedir un dato digamos: quién es el responsable, para qué se usará, a quién se transferirá y cómo ejercer derechos ARCO.  
> Lo que implementaremos es una política informativa en dos niveles: un aviso corto con código QR en cada formulario de admisión y matrícula, y la política completa en el portal web. Así, el estudiante siempre sabrá las condiciones antes de entregar sus datos."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, califico este punto como **PARCIALMENTE IMPLEMENTADO con riesgo MEDIO**.  
> El control no solo pide tener una política, sino determinar el 'timing': el momento exacto en que se entrega la información. En la UNSA el alumno se entera de las políticas si busca en el pie de página de la web, pero no se le informa en el momento crítico de la recolección, como al postular o matricularse. Exijo la incorporación de la matriz informativa multinivel en 45 días."*

---

---

# CONTROL A.1.3.4 — Providing information to PII principals
### *« Proporcionar información a los titulares de PII »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall provide PII principals with clear and easily accessible information identifying the PII controller and describing the processing of their PII."*  
> *(La organización debe proporcionar a los titulares de PII información clara y de fácil acceso que identifique al responsable del tratamiento y describa el tratamiento de su PII).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Este control es la **ENTREGA REAL Y ACCESIBLE** de la información. No sirve esconder un texto de 40 páginas en letra tamaño 6 al final de una página web. La información debe estar en lenguaje claro (comprensible para cualquier persona sin ser abogado), visible a simple vista y accesible sin costo ni barreras.
* **Analogía de la vida real:** Es como los letreros de salida de emergencia en un cine o centro comercial: tienen que ser grandes, con color verde llamativo y estar ubicados donde cualquiera los vea al instante, no guardados en un cajón cerrado de la gerencia.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO ⚠️**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA tiene publicada una Política de Privacidad en su portal web oficial (`unsa.edu.pe`).
  * **¿Por qué es parcial?:** Porque la información está redactada en lenguaje jurídico complejo, no está adaptada para personas con discapacidad visual, y en los campus físicos no existen letreros informativos (por ejemplo, en las zonas vigiladas por cámaras de seguridad no hay carteles de zona videovigilada con la información del responsable conforme exige la directiva de la ANPD).

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** Implementación en **30 días calendario** y actualización continua cada vez que cambien los datos del responsable o los sistemas.
* **HOW (Cómo):**
  1. Rediseñar la sección web de Protección de Datos Personales con lenguaje sencillo y diseño accesible (W3C / accesibilidad web).
  2. Instalar carteles físicos normalizados en todas las puertas de ingreso a los campus (Área de Ingenierías, Biomédicas y Sociales) con el aviso de videovigilancia de la Ley 29733.
  3. Colocar banners informativos en el inicio de sesión de SISUNSA y el aula virtual.
* **WHO (Quién):** Oficina de Comunicación e Imagen Institucional (diseño y redacción clara), OTI (portal web) y Oficina de Mantenimiento y Servicios Generales (cartelería física).
* **WHAT (Qué entregables):**
  1. Portal Web Accesible de Privacidad de la UNSA.
  2. Cartelería física de videovigilancia y protección de datos en los tres campus.
  3. Guía rápida ilustrada sobre derechos de privacidad para el estudiante.
* **WHERE (Dónde se ubica):** Página de inicio de `unsa.edu.pe`, campus universitarios físicos (puertas y pabellones) y sistemas virtuales.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** Existen más de 100 cámaras de seguridad en los tres campus de la UNSA y no se encontró ningún cartel de advertencia de videovigilancia que identifique al responsable del banco de datos, lo cual constituye una infracción leve-grave tipificada ante la ANPD.
* **Recomendaciones:** Instalar de forma urgente la cartelería física homologada de videovigilancia y rediseñar la política web en lenguaje accesible.
* **Dictamen:** **PARCIALMENTE IMPLEMENTADO ⚠️ | Nivel de Riesgo: MEDIO-ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.4: Proporcionar información a los titulares**, exige que la información sea fácil de encontrar y de entender.  
> No ganamos nada teniendo una política de privacidad perfecta si está escondida. Para cumplir este control en la UNSA, vamos a rediseñar la sección web haciéndola amigable y comprensible para cualquier estudiante.  
> Además, instalaremos carteles visibles en las puertas de los campus de Ingenierías, Sociales y Biomédicas que avisen que es una zona videovigilada por la UNSA y dónde consultar la política. Así cumplimos con el estándar internacional y la directiva de la ANPD."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, levanto una observación formal calificada como **PARCIALMENTE IMPLEMENTADO con riesgo MEDIO-ALTO**.  
> El hallazgo principal en campo es la omisión total de carteles de videovigilancia en los campus universitarios, a pesar de operar un sistema de monitoreo permanente. Los estudiantes no tienen manera de saber quién controla las grabaciones ni por cuánto tiempo se conservan. Se ordena subsanar la cartelería en un plazo perentorio de 30 días."*

---

---

# CONTROL A.1.3.5 — Providing mechanism to modify or withdraw consent
### *« Proporcionar mecanismo para modificar o revocar el consentimiento »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall provide a mechanism for PII principals to modify or withdraw their consent."*  
> *(La organización debe proporcionar un mecanismo para que los titulares de PII modifiquen o revoquen su consentimiento).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Dar tu consentimiento no es una condena perpetua; tienes derecho a cambiar de opinión en cualquier momento. La organización debe darte un botón o canal tan fácil de usar para **RETIRAR O MODIFICAR TU PERMISO** como lo fue para darlo. Si te tomó un clic aceptar, debe tomarte un clic revocar.
* **Analogía de la vida real:** Es como suscribirte a un boletín o membresía en línea: si pudiste suscribirte con un clic en una página web, debe haber un botón visible que diga *"Cancelar suscripción"*. Sería abusivo e ilegal que para cancelar la suscripción te obliguen a enviar una carta notarial a otra ciudad.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO ❌**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * Aplica para todos los tratamientos que se basan en consentimiento en la universidad (datos de salud para becas deportivas/alimentarias, fotos en campañas promocionales, recepción de correos con eventos de terceros).
  * **Situación actual:** La UNSA no dispone de ningún mecanismo en SISUNSA ni en sus formularios que permita a un estudiante o egresado cambiar de opinión o desmarcar una autorización previamente dada.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Regla de Equivalencia de Medios (D.S. 016-2024-JUS)
El reglamento peruano establece que el mecanismo para revocar el consentimiento debe ser **gratuito, accesible y de facilidad equivalente** al medio utilizado para recabarlo. Si se recabó digitalmente, debe poder revocarse digitalmente.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** Desarrollo e implementación en **60 días calendario** en la plataforma virtual del estudiante.
* **HOW (Cómo):**
  1. Habilitar en el panel de perfil del estudiante en SISUNSA una pestaña de *"Mis Permisos de Privacidad"*.
  2. Permitir activar o desactivar casillas (*toggles*) para tratamientos voluntarios (envío de ofertas laborales de terceros, uso de fotos en redes sociales).
  3. Configurar que al revocar el consentimiento, el sistema actualice automáticamente la base de datos y excluya al titular de los envíos o publicaciones.
  4. Habilitar formulario impreso en mesa de partes para quienes deseen hacerlo presencialmente.
* **WHO (Quién):** OTI (desarrollo informático) y Asesoría Jurídica (reglas de negocio sobre qué tratamientos son revocables y cuáles no por ser obligatorios por ley).
* **WHAT (Qué entregables):**
  1. Módulo Web de Gestión de Consentimientos en SISUNSA.
  2. Formulario de Revocatoria de Consentimiento para mesa de partes.
  3. Procedimiento interno de ejecución automática de revocatorias.
* **WHERE (Dónde se ubica):** Menú de configuración de perfil de SISUNSA y Mesa de Partes física de la universidad.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** No existe ningún botón, enlace o procedimiento en los sistemas de la universidad para que un usuario retire su consentimiento. Si un egresado no desea seguir recibiendo publicidad de posgrados, no tiene opción de *opt-out*.
* **Recomendaciones:** Implementar el módulo de preferencias de privacidad en SISUNSA y agregar el enlace de desuscripción automática al pie de los correos masivos institucionales.
* **Dictamen:** **NO IMPLEMENTADO ❌ | Nivel de Riesgo: ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.5: Mecanismo para modificar o revocar consentimiento**, garantiza que el estudiante sea dueño de su decisión.  
> Si un alumno autorizó el uso de su imagen para un video promocional de la universidad o aceptó recibir información de eventos, tiene todo el derecho de cambiar de opinión.  
> La implementación consiste en agregar una pestaña en SISUNSA llamada 'Mis Permisos', donde con un solo clic pueda desactivar las autorizaciones voluntarias. Así cumplimos la regla de la ley peruana: revocar el consentimiento debe ser tan fácil y rápido como fue otorgarlo."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, declaro este control como **NO IMPLEMENTADO con nivel de riesgo ALTO**.  
> El principio de revocabilidad es un pilar de la Ley 29733 y la ISO 27701. Actualmente los correos masivos de la UNSA y los sistemas institucionales carecen de cualquier mecanismo para revocar autorizaciones. Retener datos contra la voluntad del titular sin una base legal imperativa constituye una infracción grave ante la ANPD. Se exige el despliegue del módulo de gestión de consentimiento en 60 días."*

---

---

# CONTROL A.1.3.6 — Providing mechanism to object to PII processing
### *« Mecanismo para oponerse al tratamiento (Derecho de Oposición) »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall provide a mechanism for PII principals to object to the processing of their PII."*  
> *(La organización debe proporcionar un mecanismo para que los titulares de PII se opongan al tratamiento de su PII).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Aunque una entidad tenga permiso o base legal para procesar tus datos, si tú tienes un **motivo legítimo y fundado de peso personal** (por ejemplo, riesgo a tu seguridad, acoso o afectación a tu dignidad), tienes derecho a exigir: *"¡dejen de usar mis datos para esa actividad específica!"*, y la entidad debe tener un proceso para evaluar tu pedido y suspender el tratamiento si tu motivo es justificado.
* **Analogía de la vida real:** Si una empresa publica el directorio telefónico y dirección de todos sus empleados en su intranet general, pero una trabajadora tiene una orden de alejamiento judicial contra una expareja violenta, ella tiene derecho a oponerse a que su dirección figure en el directorio. La empresa está obligada a retirar sus datos de inmediato para proteger su vida.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO ❌**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * El **Derecho de Oposición** es uno de los cuatro derechos ARCO fundamentales reconocidos por el Artículo 22 de la Ley N° 29733. Aplica cuando un estudiante o docente tiene motivos fundados para que sus datos no se traten para un fin particular (ejemplo: publicación de listas de notas con nombres completos en vitrinas públicas o publicación de sueldo/dirección en anuarios).
  * **Situación actual:** La UNSA no cuenta con un procedimiento formal, formulario ni canal específico para tramitar solicitudes de oposición. Si un estudiante solicita que no se publique su nombre en listas de mérito por razones de seguridad personal, la universidad no tiene un protocolo establecido.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Plazos Legales en el Perú (Ley 29733 y D.S. 016-2024-JUS)
* **Plazo de respuesta al Derecho de Oposición:** **10 días hábiles** desde la recepción de la solicitud.
* Si la oposición es procedente, la entidad debe cesar el tratamiento inmediatamente.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En un plazo de **60 días calendario** para el procedimiento y con vigencia permanente.
* **HOW (Cómo):**
  1. Diseñar el **Procedimiento Operativo de Atención del Derecho de Oposición**.
  2. Crear el formulario oficial de Solicitud de Oposición (físico y virtual).
  3. Establecer el protocolo de análisis legal de procedencia (ponderación entre el deber institucional y el riesgo del titular).
  4. Capacitar a Secretaría General y jefaturas académicas para ejecutar el cese de tratamiento en un máximo de 10 días hábiles.
* **WHO (Quién):** Oficina de Asesoría Jurídica (evaluación de motivos fundados), Secretaría General (recepción) y OTI (bloqueo técnico de datos).
* **WHAT (Qué entregables):**
  1. Directiva Institucional para el Ejercicio del Derecho de Oposición.
  2. Formulario Normalizado de Oposición de Tratamiento de PII.
  3. Matriz de criterios para ponderar la procedencia de oposiciones.
* **WHERE (Dónde se ubica):** Mesa de partes física, mesa de partes virtual de la UNSA y módulo de trámites del estudiante.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** No existe canal normado para ejercer el derecho de oposición. En auditorías previas se observó la publicación de listas de calificaciones y promedios en murales físicos de pabellones con nombres y números de DNI completos, sin permitir a los estudiantes oponerse por razones de privacidad.
* **Recomendaciones:** Prohibir la exhibición pública de DNI en listas de calificaciones y aprobar el procedimiento formal de oposición.
* **Dictamen:** **NO IMPLEMENTADO ❌ | Nivel de Riesgo: ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.6: Mecanismo para oponerse al tratamiento**, corresponde a la letra 'O' de los derechos ARCO: el Derecho de Oposición.  
> Aunque la UNSA tenga derecho a procesar datos, un estudiante puede tener motivos legítimos para oponerse: por ejemplo, si sufre acoso o amenazas y no desea que su nombre figure en murales públicos de la facultad.  
> La implementación consiste en crear el formulario oficial de oposición y un procedimiento administrativo claro: la universidad tiene un plazo legal de 10 días hábiles para evaluar el pedido y, si está fundado, cesar inmediatamente el tratamiento de esos datos específicos."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, califico este punto como **NO IMPLEMENTADO con nivel de riesgo ALTO**.  
> El derecho de oposición está garantizado por la legislación peruana bajo apercibimiento de sanción grave de la ANPD si se deniega injustificadamente. En la UNSA los estudiantes no tienen una vía para oponerse a publicaciones públicas de notas o datos de contacto. Exijo emitir la directiva y el formulario de oposición en 60 días."*

---

---

# CONTROL A.1.3.7 — Access, correction or erasure
### *« Acceso, rectificación o supresión (Derechos ARCO) »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall implement policies, procedures or mechanisms to meet its obligations to PII principals to access, correct or erase their PII."*  
> *(La organización debe implementar políticas, procedimientos o mecanismos para cumplir con sus obligaciones hacia los titulares de acceder, rectificar o suprimir su PII).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Es el núcleo de los **Derechos ARCO**:
  1. **Acceso:** Derecho a saber qué datos tuyos tiene la organización y cómo los usa.
  2. **Rectificación (Corrección):** Derecho a que corrijan datos erróneos, inexactos o desactualizados.
  3. **Cancelación (Supresión / Borrado):** Derecho a exigir que borren tus datos cuando ya no sean necesarios o se traten de forma ilícita.
  La entidad debe tener un mecanismo operativo real para que la persona pueda ejercer estos tres derechos.
* **Analogía de la vida real:** Si vas al banco o a una central de riesgo (como Infocorp) y tu apellido está mal escrito o figura una deuda que ya pagaste, tienes derecho a que corrijan tu nombre y borren la deuda registrada. La entidad no puede decirte "el sistema no lo permite"; está legalmente obligada a corregir o borrar.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO ⚠️**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA tramita rectificaciones de nombres o notas mediante trámites administrativos tradicionales (FUT - Formulario Único de Trámite en Mesa de Partes).
  * **¿Por qué está parcialmente implementado?:** Porque el trámite actual es burocrático, lento y no está alineado a los plazos perentorios de la Ley 29733 (Acceso: 20 días hábiles; Rectificación y Cancelación: 10 días hábiles). Además, no existe un procedimiento de supresión de datos (cancelación) para bases accesorias (postulantes no admitidos, CVs no seleccionados de convocatorias CAS).

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Plazos Legales Peruanos (Art. 54 y 55 del Reglamento Ley 29733)
* **Derecho de Acceso:** Máximo **20 días hábiles** desde la presentación.
* **Derecho de Rectificación:** Máximo **10 días hábiles**.
* **Derecho de Cancelación (Supresión):** Máximo **10 días hábiles**.
* **Gratuidad:** El ejercicio de los derechos ARCO es **completamente gratuito**. La universidad no puede cobrar tasas administrativas (TUPA) por atender solicitudes ARCO.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En **60 días calendario** para la aprobación del reglamento y vigencia permanente con monitoreo de plazos.
* **HOW (Cómo):**
  1. Integrar en el TUPA de la UNSA el trámite gratuito de "Ejercicio de Derechos ARCO".
  2. Implementar un módulo digital en SISUNSA para solicitudes ARCO con seguimiento en tiempo real del estado de atención.
  3. Crear el procedimiento técnico de supresión segura y anonimización de datos en las bases de datos de la OTI.
  4. Capacitar al personal de mesa de partes para que no cobren aranceles por este trámite.
* **WHO (Quién):** Oficial de Protección de Datos (DPO), Secretaría General (recepción), OTI (ejecución técnica en bases de datos) y Asesoría Jurídica.
* **WHAT (Qué entregables):**
  1. Procedimiento Operativo de Atención de Derechos ARCO (Acceso, Rectificación y Cancelación).
  2. Formulario Único de Solicitud ARCO gratuito.
  3. Protocolo de Eliminación y Anonimización Segura de Datos.
* **WHERE (Dónde se ubica):** Mesa de partes física de todas las facultades, Mesa de Partes Virtual y módulo SISUNSA.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** Actualmente los trámites de rectificación de datos personales en Secretaría General pueden demorar hasta 45 o 60 días, superando holgadamente los 10 días hábiles que fija la ley peruana. No existe protocolo para atender solicitudes de supresión de datos de postulantes o exalumnos.
* **Recomendaciones:** Rediseñar el flujo administrativo para cumplir estrictamente con los plazos de 10 y 20 días hábiles, y eliminar cualquier costo arancelario asociado.
* **Dictamen:** **PARCIALMENTE IMPLEMENTADO ⚠️ | Nivel de Riesgo: ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.7: Acceso, rectificación o supresión**, representa el corazón de los Derechos ARCO.  
> Un estudiante tiene derecho a saber qué datos tiene la UNSA sobre él (Acceso), corregir si su DNI o nombre tienen un error (Rectificación), o pedir que borren sus datos si postuló hace años y no ingresó (Cancelación).  
> La implementación consiste en crear un trámite formal, 100% gratuito según la Ley 29733, con plazos estrictos: 20 días para acceso y 10 días para rectificación y cancelación. Lo habilitaremos de forma digital en SISUNSA para que el alumno no tenga que hacer largas colas con papeles."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, califico este control como **PARCIALMENTE IMPLEMENTADO con riesgo ALTO**.  
> El gran problema de la UNSA no es que no corrija errores, sino el TIEMPO que demora: los trámites burocráticos sobrepasan los plazos legales de 10 y 20 días hábiles. Si un titular denuncia esta demora ante la ANPD, la universidad incurre en infracción grave sancionable con multas de hasta 50 UIT. Mi dictamen exige implementar un sistema automatizado de gestión de solicitudes ARCO con alertas tempranas de vencimiento."*

---

---

# CONTROL A.1.3.8 — PII controllers' obligations to inform third parties
### *« Obligación de informar a terceros cesionarios »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall inform third parties with whom PII has been shared of any modification, withdrawal or objections pertaining to the shared PII, and implement appropriate policies, procedures or mechanisms to do so."*  
> *(La organización debe informar a los terceros con quienes se haya compartido PII sobre cualquier modificación, revocatoria u objeción relativa a la PII compartida, e implementar mecanismos para hacerlo).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Si la organización compartió tus datos con otra empresa o entidad del Estado (por ejemplo, con un banco o un ministerio), y luego tú solicitas corregir tu apellido o cancelar tus datos, la organización tiene la obligación de **AVISARLE A ESE TERCERO** para que también actualice o borre tus datos en sus propios sistemas. No se vale corregirlo solo en casa y dejar que el tercero mantenga el dato errado.
* **Analogía de la vida real:** Es el "efecto dominó": si cambiaste legalmente de nombre en el RENIEC, no basta con que el RENIEC lo actualice en sus oficinas; el RENIEC notifica a la SUNAT, Migraciones y la Policía para que en todos lados figures con tu nuevo nombre correcto.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO ❌**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA comparte información constante con entidades externas: **SUNEDU** (registro de grados y títulos), **MINEDU**, **Bancos recaudadores** (pagos de matrículas), **EsSalud** (seguros médicos estudiantiles) y **PRONABEC** (becarios).
  * **Situación actual:** Si un estudiante rectifica su nombre o género en la UNSA, no existe un procedimiento formal ni automatizado para notificar a los terceros cesionarios sobre esa rectificación.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En un plazo de **90 días calendario** y ejecución automática en un máximo de **10 días hábiles** tras ejecutarse una rectificación o supresión.
* **HOW (Cómo):**
  1. Mantener un registro de trazabilidad de transferencias (saber qué datos se enviaron a qué entidades).
  2. Diseñar el **Protocolo de Comunicación de Modificaciones a Terceros Cesionarios**.
  3. Establecer mecanismos de notificación electrónica formal (oficios digitales o APIs de sincronización) hacia SUNEDU, bancos y entidades asociadas.
  4. Dejar constancia documental en el expediente del titular de que se notificó a los terceros.
* **WHO (Quién):** Dirección de Asuntos Académicos (DUFA), Secretaría General, OTI y Asesoría Jurídica.
* **WHAT (Qué entregables):**
  1. Protocolo de Notificación a Terceros Receptores de Datos.
  2. Registro de Transferencias y Notificaciones de Modificación.
  3. Modelo de Oficio de Comunicación de Derechos ARCO a Terceros.
* **WHERE (Dónde se ubica):** Secretaría General de la UNSA y módulos de interoperabilidad de la OTI.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** Cuando un estudiante rectifica administrativamente sus apellidos por cambio de filiación o adopción, la UNSA actualiza su base local pero no emite notificaciones a los bancos con los que comparte el padrón de cobranzas, lo que genera rechazos de pago y desactualización en bases externas.
* **Recomendaciones:** Elaborar el protocolo de notificación a terceros y crear un log de interoperabilidad de transferencias.
* **Dictamen:** **NO IMPLEMENTADO ❌ | Nivel de Riesgo: MEDIO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.8: Obligación de informar a terceros**, evita que los errores queden flotando en otras instituciones.  
> La UNSA comparte datos de los alumnos con SUNEDU, con PRONABEC para becas y con los bancos para el pago de matrículas. Si un estudiante corrige su nombre o cancela un dato en la UNSA, la universidad está obligada por la norma ISO 27701 a avisarle a esos terceros para que también actualicen sus sistemas.  
> La implementación consiste en un protocolo de notificación formal: cada vez que se apruebe una rectificación o cancelación, Secretaría General envía un oficio digital a las entidades que recibieron esos datos."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor líder, determino este control como **NO IMPLEMENTADO con nivel de riesgo MEDIO**.  
> La cadena de custodia y exactitud de la información se rompe si la UNSA no notifica a los terceros con quienes comparte bases de datos. Si un alumno corrige judicialmente sus datos y la UNSA no avisa a SUNEDU o a las entidades bancarias, se producen perjuicios directos al titular. Mi recomendación exige articular el protocolo de notificación inmediata en un plazo de 60 días."*

---

---

# CONTROL A.1.3.9 — Providing copy of PII processed
### *« Proporcionar copia de la PII tratada (Derecho de Acceso y Portabilidad) »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall be able to provide a copy of the PII that is processed, when requested by the PII principal."*  
> *(La organización debe ser capaz de proporcionar una copia de la PII que se procesa, cuando lo solicite el titular de PII).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Si un usuario te dice: *"quiero una copia de todos los datos que tienes sobre mí"*, la organización debe estar en capacidad técnica de generar y entregarle un reporte completo con toda su información personal en un formato legible, estructurado y seguro (por ejemplo, en PDF o archivo digital común).
* **Analogía de la vida real:** Es como solicitar tu Historia Clínica completa en un hospital o el estado de tu cuenta de ahorros de los últimos 5 años en un banco. La institución está obligada a entregarte una copia íntegra de tu expediente sin ocultar información.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: PARCIALMENTE IMPLEMENTADO ⚠️**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA entrega certificados de estudios, récords académicos y constancias de matrícula a través del sistema virtual y ventanillas.
  * **¿Por qué está parcialmente implementado?:** Porque solo entrega datos académicos tradicionales mediante el pago de tasas. Si un estudiante solicita copia de sus datos de salud del tópico, sus registros de control biométrico de asistencia, o sus registros de navegación en el campus, la universidad no tiene un mecanismo para extraer y entregar esa información de forma gratuita conforme exige la Ley 29733.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En un plazo de **60 días calendario** para el desarrollo técnico y entrega de la copia en un máximo de **20 días hábiles** tras la solicitud (plazo legal del Derecho de Acceso).
* **HOW (Cómo):**
  1. Desarrollar en SISUNSA una funcionalidad automatizada: *"Descargar Mi Expediente de Datos Personales"*.
  2. El sistema compila en un archivo PDF o ZIP cifrado con contraseña: datos de matrícula, notas, asistencias, registros de biblioteca y atenciones de bienestar.
  3. Para solicitudes presenciales, generar el reporte consolidado impreso sin costo arancelario para el titular.
* **WHO (Quién):** OTI (desarrollo de scripts de extracción de datos) y Secretaría General (entrega presencial).
* **WHAT (Qué entregables):**
  1. Módulo digital de auto-descarga de expediente de PII en SISUNSA.
  2. Formato estandarizado del "Reporte Maestro de Datos Personales del Titular".
  3. Protocolo de entrega segura con verificación de identidad.
* **WHERE (Dónde se ubica):** Menú del estudiante en SISUNSA y Mesa de Partes General de la UNSA.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** Actualmente la universidad condiciona la entrega de información personal al cobro de aranceles (ej. récord de notas), lo cual vulnera la gratuidad absoluta del Derecho de Acceso estipulada en la Ley 29733. No existe capacidad técnica para entregar copias de registros biométricos o de videovigilancia.
* **Recomendaciones:** Implementar la descarga gratuita del expediente de datos personales en SISUNSA y definir el protocolo de entrega de copias de registros especiales (imágenes/biometría).
* **Dictamen:** **PARCIALMENTE IMPLEMENTADO ⚠️ | Nivel de Riesgo: MEDIO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"Para el control **A.1.3.9: Proporcionar copia de la PII tratada**, la universidad debe tener la capacidad técnica de entregarle al alumno una copia completa de toda su información.  
> Hoy en día la UNSA entrega certificados de notas, pero cobra tasas y solo entrega lo académico. Si un alumno pide copia de sus registros de asistencia biométrica o de sus fichas de bienestar, no hay cómo dárselos.  
> Lo que implementaremos es una opción en SISUNSA para que el estudiante pueda descargar gratuitamente su Expediente de Privacidad en PDF con todos sus datos consolidados, verificando previamente su identidad con su correo institucional y doble factor."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor, evalúo este control como **PARCIALMENTE IMPLEMENTADO con nivel de riesgo MEDIO**.  
> La Ley 29733 prohíbe taxativamente cobrar dinero por el ejercicio del derecho de acceso. La UNSA cobra derechos de trámite por copias de expedientes, lo cual es pasible de sanción por la ANPD. Además, la OTI debe poder exportar los datos en formatos estructurados estándar. Recomiendo habilitar la función de exportación gratuita de datos en SISUNSA en 60 días."*

---

---

# CONTROL A.1.3.10 — Handling requests
### *« Gestión y resolución de solicitudes de los titulares (DSAR) »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall define and document policies and procedures for handling and responding to legitimate requests from PII principals."*  
> *(La organización debe definir y documentar políticas y procedimientos para gestionar y responder a solicitudes legítimas de los titulares de PII).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Este control es el **MANUAL DE PROCEDIMIENTOS COMPLETO** para gestionar cualquier solicitud de derechos (conocidas internacionalmente como **DSAR** - *Data Subject Access Requests*). Define: cómo se valida que quien pide los datos es realmente el titular y no un impostor, cómo se registra el trámite, quién investiga internamente, quién redacta la respuesta formal y cómo se cumplen los plazos legales sin demoras.
* **Analogía de la vida real:** Es como el Libro de Reclamaciones de una empresa: no basta con tener el libro en el mostrador; la empresa tiene un procedimiento obligatorio por ley que dice que cada hoja se numera, se remite al área responsable, se investiga y se responde por escrito al usuario en un plazo máximo e improrrogable.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO (Formalmente) ❌**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA recibe solicitudes mediante el Formulario Único de Trámite (FUT), pero se tramitan como peticiones administrativas genéricas bajo la Ley 27444 (que tienen plazo general de 30 días hábiles), **violando los plazos más estrictos de protección de datos (10 y 20 días hábiles)**.
  * **Conexión con el proyecto TIF de los alumnos:** Este control es el corazón exacto del proyecto **TIF-DSAR** (*Agente de Derechos de Titulares mediante IA*). La universidad necesita un procedimiento automatizado que clasifique solicitudes, verifique identidad, detecte información faltante y redacte borradores de respuesta.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Fases del Procedimiento DSAR Institucional
1. **Recepción y Validación de Identidad:** Verificación de DNI / carné universitario del titular o poder notarial del representante legal.
2. **Clasificación del Pedido:** Identificar si es Acceso, Rectificación, Cancelación, Oposición o Revocatoria.
3. **Control de Plazos:** Asignación automática de temporizadores (10 días para rectificación/cancelación/oposición; 20 días para acceso).
4. **Búsqueda Interna:** Requerimiento a las dependencias que custodian los datos (OTI, Bienestar, Personal).
5. **Emisión de Resolución y Notificación:** Notificación formal motivada al titular.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En los primeros **60 días calendario** para el procedimiento administrativo y tecnológico.
* **HOW (Cómo):**
  1. Aprobar la **Directiva de Procedimiento de Atención de Solicitudes de Derechos ARCO / DSAR**.
  2. Implementar un flujo digitalizado con numeración única de expediente de privacidad.
  3. Incorporar el prototipo del **Agente de IA (TIF-DSAR)** para preclasificar solicitudes, validar documentos y redactar borradores automáticos.
  4. Capacitar a los asistentes de Mesa de Partes en la recepción sin trabas.
* **WHO (Quién):** Oficial de Protección de Datos (DPO), Secretaría General, Asesoría Jurídica y OTI.
* **WHAT (Qué entregables):**
  1. Manual de Procedimientos DSAR de la UNSA.
  2. Libro Digital de Registro de Solicitudes ARCO.
  3. Modelos de cartas de respuesta fundada, improcedente o ampliación de plazo excepcional.
* **WHERE (Dónde se ubica):** Sistema de Trámite Documentario (STD) de la UNSA y Mesa de Partes Virtual.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** La universidad carece de un procedimiento especial para solicitudes de datos personales. Las peticiones se mezclan con quejas académicas y solicitudes de trámites generales, perdiendo trazabilidad y venciendo los plazos de la Ley 29733.
* **Recomendaciones:** Separar el flujo de solicitudes de privacidad en el Sistema de Trámite Documentario y desplegar un sistema de seguimiento automatizado con semáforos de plazos.
* **Dictamen:** **NO IMPLEMENTADO ❌ | Nivel de Riesgo: ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"El control **A.1.3.10: Gestión y resolución de solicitudes (DSAR)**, es el procedimiento operativo que hace realidad los derechos de los estudiantes.  
> Hoy en día en la UNSA, si alguien presenta un pedido sobre sus datos personales, entra por Mesa de Partes como un trámite genérico y se pierde entre miles de expedientes.  
> Lo que proponemos es un flujo especializado: cuando ingresa una solicitud de derechos, se valida la identidad del estudiante, se clasifica si es acceso o cancelación, se activa un reloj de 10 o 20 días hábiles y se genera la respuesta formal. Aquí es donde se integra perfectamente nuestro proyecto de investigación con el agente inteligente para automatizar la atención de solicitudes."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor líder, determino este control como **NO IMPLEMENTADO con nivel de riesgo ALTO**.  
> El talón de Aquiles de las instituciones públicas peruanas en materia de protección de datos es la atención de solicitudes de los ciudadanos. No contar con un procedimiento documentado de atención a titulares expone a la universidad a multas coercitivas automáticas de la ANPD ante el primer reclamo no atendido. Dictamino implementar de inmediato el protocolo DSAR y su libro de control en 45 días."*

---

---

# CONTROL A.1.3.11 — Automated decision making
### *« Decisiones automatizadas y perfilamiento de titulares »*

> **Texto Normativo ISO/IEC 27701:2025:**  
> *"The organization shall identify obligations, including legal obligations, to the PII principals resulting from decisions made by the organization which are related to the PII principal based solely on automated processing of PII, and be able to demonstrate how it addresses these obligations."*  
> *(La organización debe identificar sus obligaciones frente a los titulares de PII derivadas de decisiones basadas únicamente en el tratamiento automatizado de datos, y demostrar cómo cumple con dichas obligaciones).*

---

### 1. 💡 Explicación General del Control (Antes de entrar a la UNSA)
* **¿Qué significa en palabras simples?:** Si una computadora o un algoritmo de Inteligencia Artificial toma una **decisión que afecta la vida de una persona SIN que ningún ser humano intervenga** (por ejemplo, rechazar automáticamente una beca, suspender una matrícula o calificar con un algoritmo), la organización debe cumplir obligaciones estrictas: explicarle a la persona qué lógica usó el algoritmo, darle derecho a pedir una revisión con un ser humano real, y permitirle impugnar la decisión.
* **Analogía de la vida real:** Si postulas a un crédito bancario y una Inteligencia Artificial rechaza tu solicitud en 2 segundos basándose en tu código postal o edad, el banco no puede decirte simplemente "el sistema dijo no". Tienes derecho a saber por qué fuiste rechazado y exigir que un analista humano revise tu expediente manualmente.

---

### 2. ⚖️ ¿Aplica en la UNSA y cuál es su situación actual?
* **Diagnóstico:** **APLICA DIRECTAMENTE — Nivel actual: NO IMPLEMENTADO ❌**
* **¿Por qué aplica y qué tiene ya la UNSA?:**
  * La UNSA utiliza sistemas automatizados para:
    1. Asignación automática de turnos de matrícula basados en promedio ponderado y créditos.
    2. Filtrado y evaluación automática de postulantes al comedor universitario y becas socioeconómicas en SISUNSA.
    3. Sistemas de corrección automática de fichas ópticas en exámenes de admisión.
    4. Posible uso futuro de algoritmos de alerta temprana de deserción académica.
  * **Situación actual:** La universidad no tiene un protocolo que reconozca el derecho del alumno a impugnar una decisión algorítmica ni a solicitar la intervención y revisión de un humano.

---

### 3. 🏛️ Perspectiva de la Universidad (UNSA) — Implementación

#### Obligaciones Frente a Decisiones Automatizadas (ISO 27701 y Marco Legal)
1. **Transparencia Algorítmica:** Explicar los criterios y variables del cálculo automatizado (ejemplo: fórmula del turno de matrícula o del puntaje socioeconómico del comedor).
2. **Derecho a la Intervención Humana:** Garantizar que todo estudiante pueda pedir que un funcionario revise la decisión tomada por el sistema.
3. **Derecho a Impugnar y Expresar su Punto de Vista:** Permitir presentar descargos o documentos que el sistema automatizado no contempló.

#### Plan de Implementación bajo el Enfoque 5W
* **WHEN (Cuándo):** En un plazo de **60 días calendario** para la auditoría de algoritmos y formalización del derecho de revisión humana.
* **HOW (Cómo):**
  1. Levantar un inventario de todos los procesos donde el software tome decisiones automáticas que afecten al alumno (matrículas, becas, sanciones).
  2. Documentar la lógica y reglas de negocio de los algoritmos en fichas técnicas comprensibles.
  3. Habilitar en SISUNSA el botón: *"Solicitar revisión humana de esta decisión"*.
  4. Crear comités de apelación humana en la Dirección de Bienestar y DUFA.
* **WHO (Quién):** OTI (documentación de lógica de algoritmos), Asesoría Jurídica y Direcciones Académicas correspondientes.
* **WHAT (Qué entregables):**
  1. Catálogo Institucional de Sistemas de Decisión Automatizada.
  2. Protocolo de Garantía de Intervención Humana e Impugnación de Decisiones Algorítmicas.
  3. Fichas de Explicabilidad de Algoritmos para estudiantes.
* **WHERE (Dónde se ubica):** Reglamentos académicos de matrícula y becas, y en el sistema informático SISUNSA.

---

### 4. 🕵️ Perspectiva del Auditor (Ing. Rafael)
* **Observaciones:** Existen procesos donde el sistema informático rechaza beneficios estudiantiles o asigna prioridades de matrícula de forma 100% automatizada sin que los estudiantes conozcan la fórmula exacta ni tengan derecho a una reconsideración manual por un comité evaluador.
* **Recomendaciones:** Elaborar fichas de transparencia algorítmica y reglamentar formalmente el derecho a la revisión humana de decisiones automáticas.
* **Dictamen:** **NO IMPLEMENTADO ❌ | Nivel de Riesgo: MEDIO-ALTO.**

---

### 5. 🎤 Guiones de Exposición Oral

#### 🎙️ Guión Como Universidad (UNSA):
> *"Finalizamos con el control **A.1.3.11: Decisiones automatizadas y perfilamiento**.  
> En la UNSA usamos sistemas que toman decisiones automáticas: el orden de matrícula según notas o la asignación de cupos para el comedor universitario.  
> Este control establece que ningún estudiante puede quedar desamparado ante una decisión tomada únicamente por una computadora. La universidad debe ser transparente: explicar la fórmula matemática que usó el sistema y, lo más importante, garantizar que el alumno pueda pedir que un ser humano revise su caso si considera que el sistema cometió una injusticia.  
> Implementaremos fichas técnicas de los algoritmos y un mecanismo de apelación humana en SISUNSA."*

#### 🎙️ Guión Como Auditor (Ing. Rafael):
> *"Como auditor líder, dictamino este control como **NO IMPLEMENTADO con nivel de riesgo MEDIO-ALTO**.  
> Con el avance de la inteligencia artificial y la automatización universitaria, este control de la ISO 27701:2025 cobra una vigencia vital. La universidad no puede escudarse en 'así lo calculó el sistema' para denegar derechos a los estudiantes sin brindar explicabilidad ni derecho a revisión humana. Mi dictamen exige transparentar la lógica de los sistemas de selección y habilitar el canal de reconsideración humana en 60 días."*

---

---

# 📊 MATRIZ GLOBAL Y HOJA DE RUTA

### Matriz Consolidada de la Sección A.1.3 (Obligaciones hacia los Titulares)

| Control | Título Normativo | ¿Aplica en UNSA? | Estado de Madurez | Nivel de Riesgo | Prioridad |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **A.1.3.2** | Determining/fulfilling obligations | Sí | ⚠️ Parcialmente Implementado | **MEDIO** | Alta (P1) |
| **A.1.3.3** | Determining information for principals | Sí | ⚠️ Parcialmente Implementado | **MEDIO** | Media (P2) |
| **A.1.3.4** | Providing information to principals | Sí | ⚠️ Parcialmente Implementado | **MEDIO-ALTO** | Alta (P1) |
| **A.1.3.5** | Modify or withdraw consent | Sí | ❌ No Implementado | **ALTO** | Alta (P1) |
| **A.1.3.6** | Mechanism to object (Oposición) | Sí | ❌ No Implementado | **ALTO** | Alta (P1) |
| **A.1.3.7** | Access, correction or erasure (ARCO) | Sí | ⚠️ Parcialmente Implementado | **ALTO** | Urgente (P1) |
| **A.1.3.8** | Inform third parties of changes | Sí | ❌ No Implementado | **MEDIO** | Media (P2) |
| **A.1.3.9** | Providing copy of PII (Acceso/Portabilidad) | Sí | ⚠️ Parcialmente Implementado | **MEDIO** | Media (P2) |
| **A.1.3.10** | Handling requests (Procedimiento DSAR) | Sí | ❌ No Implementado | **ALTO** | Urgente (P1) |
| **A.1.3.11** | Automated decision making (Algoritmos) | Sí | ❌ No Implementado | **MEDIO-ALTO** | Media (P2) |

---

### 🤖 Conexión Estratégica con el Proyecto TIF-DSAR
Los controles de esta sección demuestran la justificación técnica y académica del **Trabajo de Investigación Formativa (TIF-DSAR)** que desarrolla el equipo:
* El **Agente de IA para DSAR** resuelve de forma automatizada los controles **A.1.3.6, A.1.3.7, A.1.3.9 y A.1.3.10**:
  1. Valida la identidad del titular solicitante.
  2. Clasifica automáticamente si el pedido es de acceso, rectificación, cancelación u oposición.
  3. Controla los plazos legales de 10 y 20 días hábiles.
  4. Redacta el borrador de resolución técnica para firma del responsable de la universidad.

---

```
____________________________________________________________________________
FIRMA Y RESPONSABILIDAD TÉCNICA DEL AUDITOR LÍDER:
Ing. Rafael — Especialista en Ciberseguridad y Auditoría de Sistemas TI (MSc.)
Lead Auditor ISO/IEC 27001 & ISO/IEC 27701 | CISA | CRISC
Universidad Nacional de San Agustín de Arequipa (UNSA)
```
