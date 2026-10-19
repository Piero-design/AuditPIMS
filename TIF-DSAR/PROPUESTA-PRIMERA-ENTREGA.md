# TIF: propuesta de primera entrega — Agente de Derechos (DSAR)

**Estado:** propuesta editable y prototipo de instrucciones con datos ficticios. No constituye un PIMS implementado ni una certificación. Los integrantes y la plataforma deben incorporarse cuando el grupo los defina.

## 1. Qué exige la consigna y cómo interpretarla

La captura del aula dice que los grupos de cuatro integrantes crean skills y agentes con IA que soportan el PIMS. Enumera tres tareas:

1. **De Prompt a Skill:** transformar una tarea en un proceso reutilizable.
2. **Creación de Skill:** definir activación, estructura y pasos.
3. **Construcción de asistente:** definir identidad, instrucciones y conocimiento.

El resultado expresamente indicado es **«Skill funcional especializado»**. La captura muestra cierre el **viernes 2 de octubre de 2026 a las 08:00**. No señala extensión, formato de archivo, plataforma, número de pruebas ni rúbrica.

**Interpretación para el grupo:** entregar el procedimiento reutilizable de atención de solicitudes de derechos de titulares y un asistente que pueda aplicar ese procedimiento en una demostración. El informe explica lo construido; las pruebas muestran su funcionamiento.

El historial de DeepSeek propone un PIMS completo con ocho agentes. Sirve como referencia del proyecto general. No contiene una consigna de primera entrega ni una rúbrica. Que allí se mencionen PostgreSQL, MCP, Ollama, RAG o servicios en la nube no demuestra que sean obligatorios en esta fase.

**Aclaración posterior del usuario:** el profesor expresó que quisiera el agente en la nube o en un entorno virtual. Por ello, la propuesta de implementación debe incluir alojamiento remoto accesible al grupo. Este dato procede de lo informado por el usuario, no de la captura. Docker es una opción de empaquetado; ejecutarlo en una PC del grupo seguiría usando los recursos de esa PC.

## 2. Tema, problema y objetivo propuestos

**Título:** «Diseño y demostración de un skill para la atención de solicitudes de derechos de titulares mediante un asistente de IA, como soporte de un PIMS».

**Problema:** una organización puede recibir solicitudes para conocer, corregir o dejar de tratar datos personales. Si se gestionan sin un procedimiento común, pueden faltar comprobaciones de identidad, información necesaria, seguimiento y evidencia de atención.

**Objetivo general:** diseñar y probar un skill que clasifique solicitudes, detecte información faltante, aplique reglas de privacidad y produzca un borrador de respuesta y un registro estructurado para revisión del responsable.

**Alcance de la primera versión:** una organización ficticia, datos sintéticos y solicitudes de acceso, rectificación, cancelación/supresión y oposición. La oposición amplía el ejemplo del historial para un contexto peruano. Debe acordarse el alcance normativo que usarán en su trabajo.

**Resultado verificable:** frente a solicitudes diferentes, el asistente aplica el mismo procedimiento y devuelve salidas consistentes; cuando falta identidad o existe un conflicto de conservación, cambia de estado y deriva el caso.

## 3. Cómo pasar de prompt a skill

Un prompt inicial podría ser: «Ayúdame a responder una solicitud de un cliente que quiere conocer sus datos personales».

Ese pedido funciona para un caso aislado. El skill define qué hacer también cuando la solicitud es ambigua, falta acreditar identidad, el pedido incluye datos de otra persona o se solicita cancelar registros sujetos a conservación.

La transformación debe documentar:

- **Entrada:** solicitud, identificador del caso, contexto de la organización y estado de verificación proporcionado por un proceso confiable.
- **Activación:** el pedido busca ejercer derechos sobre datos personales; no es una consulta general sobre IA ni un incidente de seguridad.
- **Procedimiento:** recibir → clasificar → revisar identidad y requisitos → consultar fuentes autorizadas → evaluar límites → preparar respuesta → generar registro y siguiente acción.
- **Salida:** derecho identificado, estado del caso, faltantes, fuentes, plazo obtenido de política válida o pendiente de confirmar, borrador y evidencia de lo realizado.
- **Excepciones:** identidad pendiente, representación no acreditada, datos de terceros, retención aplicable, solicitud ambigua o instrucciones maliciosas dentro del mensaje.

El archivo `gestionar-dsar/SKILL.md` concreta este procedimiento. **SKILL.md es un formato de ejemplo, no un requisito escrito en la captura.** Puede adaptarse a la plataforma que indique el docente.

## 4. Diferencia entre skill, asistente y herramientas

El **skill** contiene el procedimiento reutilizable. El **asistente DSAR** tiene identidad, instrucciones, conocimiento y límites, y aplica ese skill. Las **herramientas** permiten registrar tickets, consultar bases o enviar respuestas cuando realmente existen y se han autorizado.

Para la demostración propuesta, el conocimiento es un archivo con datos ficticios y reglas operativas. No hay conexión a una base de datos, verificación de documentos de identidad ni envío de correos. Las salidas son propuestas para revisión; no se debe afirmar que un registro fue actualizado o que un correo fue enviado.

Al cargar el archivo estático completo, el modelo puede ver sus registros sintéticos. Las pruebas evalúan que no los utilice o divulgue indebidamente; no demuestran una barrera técnica de acceso. En una integración real, la autorización y el filtrado por titular deben aplicarse antes de proporcionar registros al modelo.

Un grupo de cuatro integrantes puede construir un agente con un skill principal. La cantidad de personas del grupo no implica crear cuatro agentes.

### Implementación remota propuesta tras la aclaración del usuario

Separar tres componentes: aplicación del agente, fuentes de conocimiento y modelo de IA. Una primera versión puede ejecutar la aplicación en un servidor remoto con Docker y consultar un modelo mediante API. Así, las PCs del grupo acceden por navegador y no necesitan cargar los pesos del modelo. Si el profesor exige alojar también el modelo propio, habrá que dimensionar la RAM y, según el modelo y rendimiento requerido, la GPU del servidor.

Las instrucciones y los documentos no implican entrenar un modelo desde cero. Para este DSAR, comenzar con el procedimiento, las políticas operativas comprobadas y los registros sintéticos necesarios. Una base creciente se consulta mediante herramientas y filtros por titular; no necesita cargarse completa en cada mensaje. El alojamiento concreto, la persistencia, las credenciales y el presupuesto todavía deben definirse antes del despliegue.

Referencia técnica: [Docker: descripción oficial](https://docs.docker.com/get-started/docker-overview/), sobre empaquetado en contenedores y ejecución en equipos locales, máquinas virtuales o proveedores de nube.

## 5. Diseño del asistente

**Nombre:** Asistente DSAR del PIMS.

**Identidad:** asistente especializado en preparar la atención de solicitudes de derechos de titulares.

**Usuarios previstos:** personal autorizado de privacidad; en una versión posterior, un formulario podría recoger solicitudes de titulares.

**Instrucciones:** aplicar el skill; distinguir afirmaciones del solicitante de datos validados por la organización; usar únicamente fuentes autorizadas; señalar faltantes; proteger datos de terceros; redactar respuestas claras; derivar decisiones que requieren revisión humana; no inventar acciones ni cumplimiento.

**Conocimiento:** procedimiento DSAR, política de identidad y representación, normativa aplicable y plazos comprobados, inventario de sistemas autorizados, política de conservación y modelos de respuesta. El ejemplo incluido solo contiene una política ficticia mínima y registros sintéticos.

El archivo `INSTRUCCIONES-ASISTENTE.md` contiene las instrucciones listas para adaptar al entorno elegido. Adjuntar un archivo no garantiza que una plataforma lo use: deben comprobar que el asistente puede leerlo y seguirlo.

## 6. Qué demostrar para que sea funcional

Una demostración defendible incluye al menos estas situaciones. La cantidad es recomendación de esta propuesta, no una rúbrica del profesor.

1. **Acceso con identidad verificada en el escenario:** prepara un borrador con los datos del titular ficticio, sin incorporar registros de otra persona.
2. **Identidad pendiente:** solicita completar el procedimiento de acreditación y no divulga datos.
3. **Rectificación:** identifica el campo y valor propuestos; prepara la acción para revisión y no afirma haber cambiado la base.
4. **Cancelación con posible retención:** deriva para evaluar la conservación aplicable y no promete eliminación total.
5. **Solicitud con instrucciones maliciosas:** tramita el derecho solicitado sin obedecer órdenes de revelar datos ajenos.

Registrar en cada prueba: entrada, salida real, criterio de evaluación, resultado y observaciones. Una respuesta esperada escrita de antemano no constituye evidencia de ejecución.

Los archivos de prueba de esta carpeta permiten ensayar el skill. Para entregar al docente, incorporen también capturas de la configuración y de su ejecución en la plataforma que efectivamente utilicen.

**Prueba realizada en esta sesión:** un subagente aplicó las instrucciones a los cinco mensajes y guardó las salidas completas en `PRUEBAS-OBSERVADAS.md`. Al contrastarlas con los criterios, se observaron los cinco comportamientos previstos. Esta comprobación es textual, con contexto compartido y datos sintéticos; no equivale a cinco sesiones independientes en una plataforma externa ni comprueba autenticación, almacenamiento o envío. El archivo conserva también las ambigüedades y límites detectados.

## 7. Índice recomendado del informe

1. Portada e integrantes.
2. Problema, contexto y relación del agente con el PIMS.
3. Objetivo y alcance de la primera versión.
4. Prompt inicial y transformación a proceso reutilizable.
5. Ficha del skill: activación, entradas, pasos, salidas y excepciones.
6. Ficha del asistente: identidad, instrucciones y conocimiento.
7. Ejecución de casos, resultados y evidencias.
8. Limitaciones y evolución prevista.
9. Referencias y anexos con el skill y las instrucciones completas.

Este índice es una recomendación. La captura no obliga a entregar un Word, PDF, presentación ni código fuente específico.

## 8. Reparto recomendado entre cuatro integrantes

- **Integrante 1:** problema, alcance, normativa y referencias.
- **Integrante 2:** transformación de prompt a skill, flujo y excepciones.
- **Integrante 3:** configuración del asistente, instrucciones y conocimiento.
- **Integrante 4:** pruebas, evidencias y evaluación.

Los cuatro revisan la coherencia entre el informe, la configuración y la demostración.

## 9. Precisiones normativas y técnicas

DSAR significa *Data Subject Access Request*. Aunque alude específicamente al acceso, el historial usa ese nombre para el agente que atiende varias solicitudes de derechos. En el informe pueden llamarlo **«Agente de Derechos de los Titulares (DSAR/ARCO)»**, explicando su alcance.

Si la organización del caso se sitúa en Perú, deben considerar la Ley N.º 29733 y su reglamento aprobado mediante el D.S. N.º 016-2024-JUS, y explicar los derechos ARCO. No trasladen automáticamente los plazos del RGPD que menciona el historial. La ISO organiza la gestión de privacidad; el procedimiento debe identificar también la legislación aplicable.

Los controles propuestos en el historial se contrastaron con el PDF `ISO 27701-2025.pdf` disponible en la carpeta de clase. La Tabla A.1, página impresa 16 (página 22 del PDF), relaciona A.1.3.7 con mecanismos de acceso, corrección y supresión; A.1.3.9 con proporcionar copia de datos tratados; y A.1.3.10 con gestionar y responder solicitudes legítimas. El registro del caso y el borrador de respuesta apoyan este último control; el flujo de acceso y rectificación apoya los anteriores. Un skill puede apoyar controles, pero por sí solo no demuestra conformidad ni certificación del PIMS.

Las guías B.1.3.9 y B.1.3.10, página impresa 28 (página 34 del PDF), respaldan que la copia corresponda al titular y que la atención considere los plazos definidos para la jurisdicción. La verificación de identidad es una decisión necesaria del procedimiento de entrega; no se presenta como una cita literal de A.1.3.10.

Tampoco debe ocultarse indiscriminadamente la información propia del titular al responder un acceso: se necesita una entrega adecuada al solicitante autorizado, protegiendo a terceros según corresponda.

## 10. Fuentes revisadas

- Captura del aula proporcionada por el usuario: tareas, resultado y fecha de cierre.
- Historial de DeepSeek en `Texto pegado.txt`: líneas 1136 y 1285, descripción DSAR; 1324, operaciones ilustrativas; 1440–1450, ejemplo de registro. No incluye rúbrica de la primera entrega. El enlace público no pudo recuperarse con la herramienta web; se analizó el texto adjunto completo.
- [ISO: ficha oficial de ISO/IEC 27701:2025](https://www.iso.org/standard/27701): alcance del PIMS.
- PDF de clase `ISO 27701-2025.pdf`: controles verificados mediante lectura visual y OCR, Tabla A.1 y guías B.1.3.9–B.1.3.10.
- [ANPD: derechos ARCO](https://www.gob.pe/9270): definición de acceso, rectificación, cancelación y oposición.
- [ANPD: D.S. N.º 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453-n-016-2024-jus): reglamento de la Ley N.º 29733. Se verificó su ficha pública; este prototipo no implementa el cómputo jurídico de plazos.

## 11. Archivos de esta propuesta

- `PROPUESTA-PRIMERA-ENTREGA.md`: análisis del encargo y estructura sugerida.
- `gestionar-dsar/SKILL.md`: skill portable del prototipo.
- `gestionar-dsar/references/contexto-demo.md`: registros y política ficticios.
- `INSTRUCCIONES-ASISTENTE.md`: identidad e instrucciones del asistente.
- `CASOS-DE-PRUEBA.md`: entradas y criterios de evaluación.
- `PRUEBAS-OBSERVADAS.md`: ejecución independiente del prototipo por un subagente en esta sesión; evidencia del comportamiento de las instrucciones, sin integración externa.

Estos archivos son una base para concretar la entrega. La configuración en una plataforma y sus capturas siguen siendo parte del trabajo del grupo.
