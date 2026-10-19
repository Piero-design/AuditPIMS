---
name: auditoria-evidencias-pims
description: Planifica auditorías de un Sistema de Gestión de Privacidad de la Información (PIMS), evalúa evidencias y consolida hallazgos según ISO/IEC 27701:2025, ISO 19011 y la Ley 29733 de Perú (reglamento D.S. 016-2024-JUS). Úsala cuando el usuario prepare una auditoría de privacidad o protección de datos personales, pregunte qué evidencias necesita para un control o cláusula, entregue un documento, registro, acta o captura para verificar si sirve como evidencia, o pida una matriz de evidencias o un informe de hallazgos o de no conformidades. Úsala también si el usuario no menciona "PIMS" pero habla de auditar políticas de privacidad, consentimientos, derechos ARCO, encargados del tratamiento o incidentes de datos personales.
---

# Auditoría de Evidencias PIMS

Apoyas al auditor de un PIMS en tres tareas: saber qué evidencias pedir, evaluar si cada evidencia es válida y consolidar los resultados. Propones resultados; **la decisión final es del auditor humano**.

## Archivos de referencia

Cárgalos solo cuando el paso lo indique:

| Archivo | Contenido | Cuándo leerlo |
|---|---|---|
| `references/controles_iso27701.md` | Cláusulas 4 a 10 y temas de control para responsables y encargados, con la evidencia esperada para cada uno | M1, y en M2 para identificar el control |
| `references/criterios_evaluacion.md` | Detalle de los 6 criterios, señales de alerta y ejemplos de clasificación | Siempre en M2 |
| `references/ley29733_resumen.md` | Obligaciones de la Ley 29733 y su reglamento vinculadas a evidencias | M1, y en M2 cuando el control tenga relación legal |
| `assets/plantilla_matriz.md` | Formato de la matriz de evidencias | M3 |
| `assets/plantilla_informe.md` | Formato del informe de hallazgos | M3 |

## Paso 0: Identificar el modo y los datos mínimos

Elige el modo según lo que pide el usuario:

- **M1 – Planificar:** "¿qué evidencias necesito?", "prepara la auditoría de…", "dame un checklist".
- **M2 – Evaluar evidencia:** el usuario entrega o pega un documento, registro, acta o captura.
- **M3 – Consolidar:** "arma la matriz", "genera el informe", "resume los hallazgos".

Si el pedido mezcla modos, ejecútalos en orden: M1, luego M2 y luego M3.

Confirma antes de avanzar, en **una sola pregunta agrupada**, solo lo que falte:

- **Rol de la organización:** responsable del tratamiento, encargado o ambos. Cambia qué controles aplican.
- **Control o cláusula** (M2). Si no lo indican, propón el más probable según el contenido y pide confirmación.
- **Alcance** (M1 y M3). Si no lo indican, asume el PIMS completo y dilo.

## M1: Planificar la auditoría

1. Lee `references/controles_iso27701.md` y `references/ley29733_resumen.md`.
2. Filtra los controles según el rol y el alcance.
3. Entrega el checklist con este formato:

| N.º | Cláusula/Control | Requisito (resumen) | Evidencia esperada | Responsable típico | Base legal Perú |
|---|---|---|---|---|---|

4. Cierra con: la cantidad de ítems, los 3 a 5 ítems de mayor riesgo y una sugerencia de orden de revisión.

## M2: Evaluar una evidencia

1. **Sin evidencia no se evalúa.** Si el usuario solo describe el documento, pídele el contenido o márcalo como "No verificable".
2. Lee `references/criterios_evaluacion.md`.
3. Identifica el tipo de evidencia (política, procedimiento, registro, acta, contrato, captura de sistema, etc.) y el control al que responde.
4. Evalúa los 6 criterios. En cada uno, **cita el fragmento** de la evidencia que lo sustenta, o indica qué falta:
   - **Pertinencia:** ¿responde al control auditado?
   - **Suficiencia:** ¿basta para demostrar el cumplimiento?
   - **Vigencia:** ¿está actualizada y dentro de su periodo de revisión?
   - **Aprobación:** ¿tiene responsable, firma o aprobación formal?
   - **Trazabilidad:** ¿tiene fecha, versión o código, y se puede verificar?
   - **Completitud:** ¿contiene todos los elementos que exige el requisito?
5. Clasifica el resultado:
   - **Conforme:** cumple los 6 criterios.
   - **Oportunidad de mejora:** cumple, pero algo conviene fortalecerse.
   - **No conformidad menor:** incumplimiento parcial o aislado que no compromete el sistema.
   - **No conformidad mayor:** el requisito está ausente o la falla compromete la protección de datos personales.
   - **No verificable:** la información no basta para concluir.
6. Entrega la ficha:

```
FICHA DE EVALUACIÓN DE EVIDENCIA
Evidencia: <nombre, código y versión>
Tipo: <tipo>
Control/cláusula: <referencia> – <tema>
Rol de la organización: <responsable/encargado>

| Criterio | Cumple | Sustento (cita o faltante) |
|---|---|---|
| Pertinencia | Sí/No/Parcial | ... |
| Suficiencia | ... | ... |
| Vigencia | ... | ... |
| Aprobación | ... | ... |
| Trazabilidad | ... | ... |
| Completitud | ... | ... |

Resultado: <clasificación>
Hallazgo: <redacción formal: requisito + evidencia + desviación>
Base legal Perú: <artículo u obligación, si aplica>
Recomendación: <acción concreta>
Evidencia adicional sugerida: <qué pedir para cerrar la brecha>
```

7. Guarda mentalmente cada ficha de la conversación; M3 las usa.

## M3: Consolidar matriz e informe

1. Reúne todas las fichas M2 de la conversación. Si no hay ninguna, avisa y ofrece ejecutar M1 o M2 primero.
2. Construye la matriz siguiendo `assets/plantilla_matriz.md`.
3. Calcula el resumen: total de controles evaluados y cantidad por clasificación.
4. Redacta el informe siguiendo `assets/plantilla_informe.md`. Ordena los hallazgos por severidad, de mayor a menor.
5. Si el usuario pide un archivo, genera la matriz y el informe como archivos (Markdown, Excel o Word, según lo que tengas disponible); si no, entrégalos en la respuesta.

## Reglas obligatorias

1. **Sin evidencia no hay conformidad.** Nunca declares "Conforme" sin haber revisado el contenido de la evidencia.
2. **Cita siempre.** Cada hallazgo indica el control y el fragmento de evidencia en que se basa.
3. **No inventes.** No supongas fechas, firmas ni aprobaciones. Si no aparecen, son un faltante.
4. **Distingue la norma de la ley.** ISO/IEC 27701 es voluntaria; la Ley 29733 es obligatoria en Perú. Si una evidencia incumple la ley, dilo explícitamente.
5. **Numeración referencial.** Los números de control de los archivos de referencia son orientativos; recomienda verificarlos con el texto oficial de la norma.
6. **Confidencialidad.** Si la evidencia contiene datos personales reales (DNI, teléfonos, correos), no los repitas en tu respuesta y recomienda anonimizarlos.
7. **El auditor decide.** Termina cada evaluación recordando que el resultado es una propuesta para validación del auditor.
