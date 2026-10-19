# Catálogo de controles y requisitos – ISO/IEC 27701:2025 (modo M1)

> **La numeración es referencial; verificar con el texto oficial de ISO/IEC 27701:2025.**
> Los IDs (CL-, RT-, EN-, SG-) son identificadores propios de este catálogo, no números de control de la norma. La columna "Tema" indica el grupo de controles de la norma; los resúmenes son redacción propia, no texto de la norma.

**Contexto:** ISO/IEC 27701:2025 (2.ª ed., publicada el 14/10/2025) es una norma independiente: ya no exige implementar ISO/IEC 27001. Tiene estructura de sistema de gestión (cláusulas 4 a 10) y un Anexo A con controles para responsables del tratamiento, controles para encargados y controles de seguridad seleccionados. La norma es voluntaria; la Ley 29733 y el D.S. 016-2024-JUS son obligatorios en Perú.

**Cómo filtrar por rol:** Responsable → secciones A, B y D. Encargado → secciones A, C y D. Ambos roles → todas.

**Abreviaturas de responsables típicos:** Dir. = Alta dirección; ODP = Oficial de datos personales; TI = Tecnologías de la información; SEG = Seguridad de la información; LEG = Legal; RRHH = Recursos humanos; CAL = Calidad/Auditoría interna; Áreas = dueños de procesos.

---

## Sección A. Requisitos de gestión (cláusulas 4 a 10)

| ID | Cláusula | Requisito (resumen propio) | Evidencia esperada | Responsable típico |
|---|---|---|---|---|
| CL-01 | 4 Contexto | Determinar cuestiones internas y externas y definir el alcance del PIMS (procesos, ubicaciones, sistemas, tratamientos). | Documento de alcance del PIMS con versión y aprobación; análisis de contexto (FODA/PESTEL) | Dir. / ODP |
| CL-02 | 4 Contexto | Identificar partes interesadas (titulares, autoridad, clientes, proveedores) y sus requisitos legales y contractuales de privacidad. | Matriz de partes interesadas; registro de requisitos legales (Ley 29733, D.S. 016-2024-JUS, contratos) | ODP / LEG |
| CL-03 | 4 Contexto | Definir y documentar el rol de la organización (responsable, encargado o ambos) para cada tratamiento. | Matriz de roles por tratamiento; contratos o instrucciones que lo respaldan | ODP / LEG |
| CL-04 | 5 Liderazgo | La alta dirección demuestra compromiso y aprueba una política de privacidad coherente con el alcance, con compromisos de cumplimiento y mejora. | Política de privacidad aprobada, fechada, versionada y difundida; acta de aprobación | Dir. |
| CL-05 | 5 Liderazgo | Asignar roles y autoridades de privacidad, incluido el oficial de datos personales (D.S. 016-2024-JUS). | Resolución o carta de designación del ODP; organigrama; manual de funciones | Dir. / RRHH |
| CL-06 | 6 Planificación | Evaluar riesgos para los titulares y para la organización con criterios definidos y repetibles. | Metodología de riesgos de privacidad; matriz de riesgos con fecha, dueños y valoración | ODP / SEG |
| CL-07 | 6 Planificación | Seleccionar tratamientos de riesgo, determinar controles necesarios y elaborar la declaración de aplicabilidad con justificación de exclusiones. | Plan de tratamiento de riesgos; declaración de aplicabilidad aprobada | ODP / Dir. |
| CL-08 | 6 Planificación | Establecer objetivos de privacidad medibles y planes para alcanzarlos. | Objetivos e indicadores con meta, responsable y plazo | Dir. / ODP |
| CL-09 | 7 Soporte | Asegurar competencia del personal con funciones de privacidad y capacitación del resto según su rol. | Plan anual de capacitación; listas de asistencia; evaluaciones; perfiles de puesto del ODP | RRHH / ODP |
| CL-10 | 7 Soporte | Controlar la información documentada (creación, versión, aprobación, acceso, retención). | Procedimiento de control documental; lista maestra de documentos; historial de versiones | CAL / ODP |
| CL-11 | 7 Soporte | Establecer comunicación interna y externa sobre privacidad y concienciar al personal. | Plan de comunicación; campañas de concienciación; canal de consultas y quejas | ODP |
| CL-12 | 8 Operación | Planificar y controlar los procesos operativos; mantener inventario o registro de tratamientos de datos personales. | Inventario/registro de tratamientos (finalidad, categorías, base legal, destinatarios, plazos); procedimientos operativos | ODP / Áreas |
| CL-13 | 8 Operación | Realizar evaluaciones de impacto en la privacidad (EIPD/DPIA) cuando el tratamiento implique riesgo elevado o cambios relevantes. | Procedimiento de EIPD; informes de EIPD con aprobación y medidas de mitigación | ODP / Áreas |
| CL-14 | 9 Evaluación | Hacer seguimiento, medición, análisis y evaluación del desempeño del PIMS. | Tablero de indicadores; informes periódicos; análisis de tendencias | ODP |
| CL-15 | 9 Evaluación | Realizar auditorías internas planificadas con auditores competentes e imparciales. | Programa de auditoría; plan e informes de auditoría interna; evidencia de competencia del auditor | CAL |
| CL-16 | 9 Evaluación | La alta dirección revisa el PIMS a intervalos planificados y decide mejoras. | Acta de revisión por la dirección con entradas (auditorías, incidentes, indicadores) y decisiones | Dir. |
| CL-17 | 10 Mejora | Tratar las no conformidades: corregir, analizar causa raíz y verificar eficacia de las acciones correctivas. | Registro de no conformidades y acciones correctivas con causa raíz, responsable, plazo y cierre verificado | CAL / ODP |
| CL-18 | 10 Mejora | Mejorar de forma continua la idoneidad y eficacia del PIMS. | Registro de mejoras implementadas; seguimiento de oportunidades de mejora | ODP / Dir. |

---

## Sección B. Controles para el RESPONSABLE del tratamiento

| ID | Tema | Control (resumen) | Evidencia esperada | Base legal Perú |
|---|---|---|---|---|
| RT-01 | Condiciones para la recolección y el tratamiento | Identificar y documentar la base legal y la finalidad de cada tratamiento, y limitar el tratamiento a esa finalidad. | Registro de tratamientos con base legal y finalidad; matriz de finalidades | Ley 29733, principios (arts. 4 a 11) |
| RT-02 | Condiciones para la recolección y el tratamiento | Obtener y registrar el consentimiento libre, previo, expreso, informado e inequívoco cuando sea la base legal, incluido el reforzado cuando corresponda. | Registro de consentimientos (quién, cuándo, finalidad, versión del texto, canal); formularios; capturas del flujo de recolección | Ley 29733, arts. 5 y 13–14; consentimiento reforzado (D.S. 016-2024-JUS) |
| RT-03 | Condiciones para la recolección y el tratamiento | Mecanismo para retirar el consentimiento con la misma facilidad con que se otorgó, y registro del retiro. | Procedimiento de revocación; registro de revocaciones y su efecto en los sistemas | Ley 29733, arts. 5 y 13–14 |
| RT-04 | Condiciones para la recolección y el tratamiento | Tratar datos sensibles y biométricos con base legal reforzada y medidas adicionales. | Inventario de datos sensibles/biométricos; consentimientos específicos; medidas de seguridad reforzadas (D.S. 016-2024-JUS) | Ley 29733, arts. 5 y 13–14; biométricos como sensibles (D.S. 016-2024-JUS) |
| RT-05 | Condiciones para la recolección y el tratamiento | Inscribir y mantener actualizados los bancos de datos personales ante la autoridad. | Constancias de inscripción y actualizaciones en el Registro Nacional de Protección de Datos Personales | Ley 29733, art. 34 |
| RT-06 | Obligaciones con los titulares | Informar a los titulares sobre el tratamiento (aviso de privacidad) de forma clara y accesible en el momento de la recolección. | Aviso/política de privacidad publicada y versionada; capturas de web, formularios y carteles | Ley 29733, art. 18 |
| RT-07 | Obligaciones con los titulares | Atender solicitudes de derechos ARCO (acceso, rectificación, cancelación/supresión, oposición y demás) con canal, responsable y plazos. | Procedimiento de atención de derechos; registro de solicitudes con fechas de recepción y respuesta; muestras de respuestas | Ley 29733, arts. 18 a 27; verificar plazo vigente en el reglamento (D.S. 016-2024-JUS) |
| RT-08 | Obligaciones con los titulares | Verificar la identidad del solicitante y entregar la respuesta en forma comprensible y gratuita en lo que corresponda. | Protocolo de verificación de identidad; modelos de respuesta; registro de rechazos motivados | Ley 29733, arts. 18 a 27 |
| RT-09 | Obligaciones con los titulares | Comunicar la rectificación o supresión a terceros a quienes se hayan transferido los datos, cuando proceda. | Registro de comunicaciones a destinatarios; evidencia de ejecución | Ley 29733, arts. 18 a 27 |
| RT-10 | Obligaciones con los titulares | Gestionar quejas y atender requerimientos de la Autoridad Nacional de Protección de Datos Personales. | Registro de quejas; respuestas a requerimientos; seguimiento | Ley 29733, título VII (infracciones y sanciones) |
| RT-11 | Privacidad desde el diseño y por defecto | Aplicar minimización: recolectar solo los datos necesarios, adecuados y pertinentes. | Revisión de formularios y campos; análisis de necesidad por finalidad | Ley 29733, principios (arts. 4 a 11) |
| RT-12 | Privacidad desde el diseño y por defecto | Definir y aplicar plazos de retención y eliminación o anonimización al vencer la finalidad. | Política de retención; calendario de conservación; registros de eliminación o anonimización | Ley 29733, principios (arts. 4 a 11) |
| RT-13 | Privacidad desde el diseño y por defecto | Incorporar requisitos de privacidad en el diseño de sistemas y procesos nuevos y configurar valores por defecto protectores. | Lista de verificación de privacidad en proyectos; EIPD previas al lanzamiento; configuraciones por defecto | Ley 29733, principios (arts. 4 a 11); D.S. 016-2024-JUS |
| RT-14 | Privacidad desde el diseño y por defecto | Garantizar exactitud y calidad de los datos durante su ciclo de vida. | Procedimiento de actualización y depuración; controles de calidad de datos | Ley 29733, principios (arts. 4 a 11) |
| RT-15 | Compartición, transferencia y divulgación | Formalizar con contrato las relaciones con encargados del tratamiento, con instrucciones, seguridad y condiciones de subcontratación. | Contratos o adendas con encargados; inventario de encargados; evaluaciones previas de proveedores | Ley 29733, art. 28; D.S. 016-2024-JUS (encargados) |
| RT-16 | Compartición, transferencia y divulgación | Documentar y justificar los flujos transfronterizos, verificando nivel adecuado de protección o garantías. | Inventario de transferencias internacionales; cláusulas contractuales o garantías; comunicación a la autoridad cuando corresponda | Ley 29733, art. 15 |
| RT-17 | Compartición, transferencia y divulgación | Registrar las transferencias y divulgaciones a terceros (destinatario, datos, finalidad, fecha, base legal). | Registro de divulgaciones/transferencias; solicitudes de autoridades y respuestas | Ley 29733, arts. 15 y 28 |
| RT-18 | Compartición, transferencia y divulgación | Mantener el registro de actividades de tratamiento actualizado y alineado con las transferencias reales. | Registro de actividades con fecha de última revisión; conciliación con proveedores | Ley 29733, art. 28; D.S. 016-2024-JUS |
| RT-19 | Compartición, transferencia y divulgación | Informar a los titulares sobre los destinatarios y las transferencias. | Aviso de privacidad con destinatarios o categorías; consentimiento específico si aplica | Ley 29733, art. 18 |

---

## Sección C. Controles para el ENCARGADO del tratamiento

| ID | Tema | Control (resumen) | Evidencia esperada | Base legal Perú |
|---|---|---|---|---|
| EN-01 | Contrato con el cliente | Contar con contrato escrito con cada responsable que defina objeto, duración, tipos de datos, instrucciones y medidas de seguridad. | Contratos o acuerdos de encargo firmados; anexos de tratamiento | Ley 29733, art. 28; D.S. 016-2024-JUS (encargados) |
| EN-02 | Instrucciones documentadas | Tratar los datos solo según instrucciones documentadas del responsable y avisar si una instrucción infringe la ley. | Instrucciones por escrito; registro de tratamientos del encargado; procedimiento de gestión de instrucciones | Ley 29733, principios (arts. 4 a 11) y art. 28 |
| EN-03 | Apoyo en derechos ARCO | Apoyar al responsable en la atención de solicitudes de titulares, derivándolas sin demora. | Procedimiento de derivación; registro de solicitudes recibidas y reenviadas con fechas | Ley 29733, arts. 18 a 27 |
| EN-04 | Subencargados | Contratar subencargados solo con autorización del responsable y trasladarles las mismas obligaciones. | Autorizaciones del responsable; contratos con subencargados; lista actualizada | D.S. 016-2024-JUS (encargados) |
| EN-05 | Transferencias | Realizar transferencias internacionales solo según instrucción y con garantías. | Inventario de transferencias del encargado; autorizaciones; garantías contractuales | Ley 29733, art. 15 |
| EN-06 | Término del servicio | Devolver o eliminar los datos al terminar el servicio y certificar la eliminación. | Procedimiento de cierre; certificados de eliminación o actas de devolución | Ley 29733, principios (arts. 4 a 11); D.S. 016-2024-JUS |
| EN-07 | Incidentes | Notificar al responsable los incidentes de seguridad sin demora, con plazos compatibles con la obligación de 48 horas del responsable. | Procedimiento de notificación; registro de incidentes y notificaciones con hora de detección y aviso | Notificación a la autoridad en 48 horas (D.S. 016-2024-JUS) |
| EN-08 | Confidencialidad | Asegurar que el personal autorizado a tratar datos esté sujeto a deber de confidencialidad. | Acuerdos de confidencialidad firmados; cláusulas laborales | Ley 29733, art. 17 |

---

## Sección D. Controles de seguridad relevantes para la privacidad

| ID | Tema | Control (resumen) | Evidencia esperada | Base legal Perú |
|---|---|---|---|---|
| SG-01 | Control de acceso | Conceder acceso a datos personales por necesidad (mínimo privilegio) y revisar los accesos periódicamente. | Matriz de roles y accesos; revisiones periódicas de accesos; altas/bajas con aprobación | Ley 29733, arts. 16 y 17 |
| SG-02 | Cifrado | Proteger datos personales en tránsito y en reposo con cifrado según su sensibilidad. | Política de criptografía; configuración de cifrado; certificados vigentes; capturas del sistema | Ley 29733, art. 16 |
| SG-03 | Registros y monitoreo | Registrar y proteger los accesos y operaciones sobre datos personales y revisarlos. | Logs de acceso con retención definida; informes de revisión; protección contra alteración | Ley 29733, art. 16 |
| SG-04 | Gestión de incidentes | Detectar, clasificar, contener y comunicar incidentes de seguridad con datos personales, incluida la notificación a la autoridad en 48 horas. | Procedimiento de incidentes; registro de incidentes; simulacros; notificaciones a la autoridad y a titulares | Ley 29733, art. 16; notificación en 48 horas (D.S. 016-2024-JUS) |
| SG-05 | Copias de respaldo | Realizar y probar copias de respaldo protegidas, con retención coherente con la política de datos. | Política y calendario de respaldos; registros de ejecución; pruebas de restauración | Ley 29733, art. 16 |
| SG-06 | Capacitación y concienciación | Capacitar al personal en seguridad y privacidad con evaluación de efectividad. | Registros de capacitación; resultados de campañas de phishing o evaluaciones | Ley 29733, art. 16; CL-09 |
| SG-07 | Gestión de proveedores | Evaluar y supervisar la seguridad de proveedores que acceden a datos personales. | Evaluaciones de proveedores; acuerdos de nivel de servicio y seguridad; informes de auditoría de terceros | Ley 29733, arts. 16 y 28 |

---

## Sección E. Ítems de mayor riesgo

Suelen generar no conformidades mayores porque su ausencia compromete directamente a los titulares o expone a sanciones.

| N.º | ID | Ítem | Por qué es de alto riesgo |
|---|---|---|---|
| 1 | RT-02 / RT-03 | Registro de consentimientos (y revocación) | Sin registro no se puede demostrar la base legal; el reglamento refuerza el consentimiento. |
| 2 | RT-05 | Inscripción y actualización de bancos de datos en el Registro Nacional | Es obligación legal verificable por la autoridad; su omisión es infracción. |
| 3 | SG-04 / EN-07 | Gestión de incidentes y notificación en 48 horas | Plazo estricto (D.S. 016-2024-JUS); sin procedimiento ni registro la organización no puede cumplirlo. |
| 4 | RT-15 / EN-01 | Contratos con encargados y subencargados | Sin contrato hay tratamiento sin garantías y se rompe la cadena de responsabilidad. |
| 5 | RT-07 | Atención de derechos ARCO | Incumplir o responder fuera de plazo es causa frecuente de reclamos y sanciones; verificar plazo vigente en el reglamento. |

**Otros a vigilar:** CL-05 (oficial de datos personales no designado), RT-16 (transferencias internacionales sin garantías), RT-04 (datos biométricos o sensibles sin consentimiento reforzado) y CL-13 (ausencia de EIPD en tratamientos de riesgo elevado).

**Orden de revisión sugerido:** (1) CL-01 a CL-05 (alcance, rol, política, ODP); (2) CL-12 y RT-01 (inventario y base legal); (3) los ítems de la sección E; (4) resto de controles de la sección B/C; (5) sección D; (6) CL-14 a CL-18 (desempeño y mejora).
