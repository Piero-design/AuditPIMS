# Resumen de la Ley 29733 y su reglamento (D.S. 016-2024-JUS)

> Resumen propio con fines de apoyo a la auditoría; no sustituye el texto legal. Para el reglamento no se citan números de artículo: se describe la obligación por tema y se marca "(D.S. 016-2024-JUS)". Donde el plazo no está confirmado, verificar plazo vigente en el reglamento. Los IDs de controles corresponden a `controles_iso27701.md` (numeración referencial).

## Marco

- **Ley 29733**, Ley de Protección de Datos Personales (Perú).
- **D.S. 016-2024-JUS**, nuevo reglamento, vigente desde el 30/03/2025; derogó el D.S. 003-2013-JUS.
- Novedades del reglamento: notificación de incidentes de seguridad a la Autoridad Nacional de Protección de Datos Personales en 48 horas; oficial de datos personales; consentimiento reforzado; datos biométricos como sensibles; alcance extraterritorial.

**Nota:** ISO/IEC 27701:2025 es voluntaria (certificable); la Ley 29733 y su reglamento son obligatorios en Perú. Cumplir la norma ISO ayuda a demostrar cumplimiento, pero no lo garantiza ni lo reemplaza. Si una evidencia incumple la ley, el hallazgo debe decirlo expresamente.

## Principios (arts. 4 a 11)

| Principio | Idea central |
|---|---|
| Legalidad | Tratamiento conforme a la ley; prohibida la recolección por medios fraudulentos o desleales. |
| Consentimiento | El tratamiento requiere consentimiento libre, previo, expreso e informado (salvo excepciones legales). |
| Finalidad | Los datos se recolectan para finalidades determinadas, explícitas y lícitas, y no se usan para otras incompatibles. |
| Proporcionalidad | El tratamiento debe ser adecuado, relevante y no excesivo respecto de la finalidad. |
| Calidad | Datos veraces, exactos, actualizados y conservados solo el tiempo necesario. |
| Seguridad | Medidas técnicas, organizativas y legales para proteger los datos. |
| Disposición de recurso | El titular debe contar con vías administrativas y judiciales para reclamar. |
| Nivel de protección adecuado | En transferencias fuera del país se garantiza un nivel de protección suficiente. |

## Tabla de obligaciones

| N.º | Obligación | Fuente | Evidencia que la demuestra | Controles ISO relacionados |
|---|---|---|---|---|
| 1 | Aplicar los principios de legalidad, finalidad y proporcionalidad en cada tratamiento | Ley 29733, arts. 4 a 11 | Registro de tratamientos con finalidad y base legal; análisis de necesidad de datos | CL-12, RT-01, RT-11 |
| 2 | Obtener consentimiento libre, previo, expreso e informado, y poder demostrarlo | Ley 29733, arts. 5 y 13–14; consentimiento reforzado (D.S. 016-2024-JUS) | Registro de consentimientos; formularios; texto versionado | RT-02, RT-03 |
| 3 | Informar al titular sobre el tratamiento (aviso de privacidad) | Ley 29733, art. 18 | Aviso publicado y versionado; capturas de formularios | RT-06, RT-19 |
| 4 | Inscribir los bancos de datos en el Registro Nacional de Protección de Datos Personales y mantenerlos actualizados | Ley 29733, art. 34 | Constancias de inscripción y de actualizaciones | RT-05, RT-18 |
| 5 | Atender los derechos del titular (acceso, actualización, inclusión, rectificación, supresión, oposición y otros) | Ley 29733, arts. 18 a 27; verificar plazo vigente en el reglamento | Procedimiento; registro de solicitudes con fechas; respuestas | RT-07, RT-08, RT-09, EN-03 |
| 6 | Adoptar medidas de seguridad técnicas, organizativas y legales | Ley 29733, art. 16 | Política de seguridad; control de accesos; cifrado; logs; respaldos | SG-01 a SG-07, CL-06, CL-07 |
| 7 | Guardar confidencialidad del personal que accede a los datos | Ley 29733, art. 17 | Acuerdos de confidencialidad; cláusulas laborales | EN-08, SG-01 |
| 8 | Cumplir las condiciones para el flujo transfronterizo de datos | Ley 29733, art. 15 | Inventario de transferencias; garantías contractuales; comunicación a la autoridad cuando corresponda | RT-16, EN-05 |
| 9 | Cumplir las obligaciones del titular del banco de datos personales (en el rol de responsable) | Ley 29733, art. 28 | Registro de actividades; políticas; contratos con terceros | RT-15, RT-17, RT-18 |
| 10 | Regular por contrato las relaciones con encargados del tratamiento | Ley 29733, art. 28; D.S. 016-2024-JUS (encargados) | Contratos con instrucciones, seguridad, subencargados y devolución | RT-15, EN-01, EN-02, EN-04, EN-06 |
| 11 | Designar un oficial de datos personales (según los supuestos del reglamento) | D.S. 016-2024-JUS | Designación formal; funciones; independencia; comunicación a la autoridad si aplica (verificar) | CL-05 |
| 12 | Notificar a la autoridad los incidentes de seguridad en 48 horas, y a los titulares cuando corresponda | D.S. 016-2024-JUS | Procedimiento de incidentes; registro con hora de detección y notificación; constancias | SG-04, EN-07 |
| 13 | Tratar datos sensibles (incluidos biométricos) con consentimiento reforzado y medidas adicionales | Ley 29733, arts. 5 y 13–14; D.S. 016-2024-JUS | Inventario de datos sensibles; consentimientos específicos; medidas reforzadas | RT-04 |
| 14 | Realizar evaluaciones de impacto o análisis de riesgos para tratamientos de riesgo elevado, según el reglamento | D.S. 016-2024-JUS (verificar supuestos exactos) | EIPD aprobadas; metodología de riesgos | CL-06, CL-13 |
| 15 | Aplicar la ley a tratamientos con alcance extraterritorial según los supuestos del reglamento | D.S. 016-2024-JUS | Análisis de aplicabilidad; designación de representante si corresponde (verificar) | CL-02, CL-03 |
| 16 | Conservar los datos solo por el tiempo necesario y suprimirlos al cumplirse la finalidad | Ley 29733, principios (arts. 4 a 11) | Política de retención; registros de eliminación | RT-12, EN-06 |
| 17 | Responder ante la autoridad por infracciones y atender sus requerimientos | Ley 29733, título VII (infracciones y sanciones) | Registro de requerimientos y respuestas; expedientes | RT-10 |

## Uso en la auditoría

- En M1, usa la tabla para añadir la columna "Base legal Perú" del checklist.
- En M2, si el control tiene relación legal, indica la obligación en el campo "Base legal Perú" de la ficha y deja claro cuando el incumplimiento es de la ley (obligatoria) y no solo de la norma (voluntaria).
- No cites artículos del reglamento; usa "(D.S. 016-2024-JUS)" y el tema. Si el usuario necesita el artículo exacto, recomienda verificarlo en el texto oficial publicado en El Peruano.
