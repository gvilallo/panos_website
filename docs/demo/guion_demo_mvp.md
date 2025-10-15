# Guion de Demo MVP PANOS

## Storyline (7–10 minutos)
| Minuto aprox. | Escena | Objetivo | Datos de ejemplo (Inmobiliaria "Lomas Verdes") | Narrativa clave |
| --- | --- | --- | --- | --- |
| 0:00 – 1:00 | **Landing** | Presentar propuesta de valor y CTA principal. | Hero con CTA "Iniciar diagnóstico". Testimonio breve de cliente. | "En menos de 10 minutos dejamos lista la primera entrevista y un brief accionable." |
| 1:00 – 3:30 | **Chat del agente** | Capturar requerimientos del prospecto mediante preguntas dinámicas. | Respuestas: segmento residencias premium, 120 propiedades activas, CRM propio. | Mostrar cómo el agente adapta preguntas según respuestas. Enfatizar confirmación de T&Cs y privacidad antes de continuar. |
| 3:30 – 4:30 | **Resumen del brief en vivo** | Visualizar consolidado en panel lateral. | Must: inventario + panel cobranza; Should: firma electrónica; Could: app móvil. | "El panel prioriza lo imprescindible y marca oportunidades para siguientes etapas." |
| 4:30 – 6:00 | **Mockups iniciales** | Enseñar wireframes generados al vuelo. | Home con buscador, dashboard con KPIs, flujo de contrato en 3 pasos. | "Mientras charlamos, PANOS produce mockups editables para alinear expectativas." |
| 6:00 – 7:30 | **Pago de seña** | Mostrar creación del link de Mercado Pago y confirmación del pago de ARS 150.000. | Monto seña: ARS 150.000, external_reference: LV-2024-09, payer_email: carolina@lomasverdes.com. | "En un clic aseguramos la agenda; la seña se descuenta del proyecto final." |
| 7:30 – 8:30 | **Comprobante y agenda** | Entregar comprobante y seleccionar franja horaria. | Comprobante PDF descargable, agenda jueves 16:00 ART con team PANOS. | "Todo queda registrado, con recordatorios por email y WhatsApp (opt-in previo)." |
| 8:30 – 9:30 | **Dashboard interno** | Mostrar vista del equipo PANOS con logs y próximos pasos. | Lead #LV-2024-09, estado: "Seña confirmada", tareas: preparar workshop. | "El equipo recibe un brief completo y trazabilidad de consentimientos y pagos." |
| 9:30 – 10:00 | **Cierre y próximos pasos** | Resaltar métricas obtenidas y llamadas a la acción. | KPIs mostrados en dashboard, agenda confirmada, opt-ins registrados. | "Listos para la primera reunión; seguimos con prototipado y estimación detallada." |

## Momentos "Wow"
1. **Brief en vivo**: panel lateral se actualiza con Must/Should/Could y KPIs tras cada respuesta.
2. **Mockup instantáneo**: wireframe del dashboard inmobiliario generado en segundos con CTA para iterar.
3. **Pago con comprobante automático**: después de Mercado Pago, se genera recibo con datos fiscales y se habilita agenda.

## Datos de ejemplo coherentes
- Prospecto: *Lomas Verdes Propiedades S.R.L.*
- Contacto: *Carolina Méndez*, carolina@lomasverdes.com, +54 9 11 3456-7890.
- Objetivo principal: "Centralizar inventario y automatizar cobranza".
- KPIs: +20% leads calificados, <24h en emitir contratos, 0 pagos vencidos sin notificación.
- Mockups solicitados: Home pública, Dashboard admin, Flujo de contrato.
- Seña: ARS 150.000 (Checkout Pro), referencia externa LV-2024-09.
- Agenda preferida: jueves 16:00 ART, canal Google Meet.

## Métricas a capturar durante la demo
- Tiempo total de entrevista (inicio/fin) y número de preguntas respondidas.
- Tasa de completitud del brief (campos obligatorios vs. completados).
- Estado del pago (tiempo desde link generado a `PAGADO_OK`).
- Tiempo de emisión del comprobante y envío de notificación.
- Confirmación de agenda (latencia desde pago hasta slot reservado).
- Opt-ins válidos (registro timestamp + canal) y confirmación de plantillas WhatsApp enviadas.

## Checklist previa a la demo
- [ ] Plantillas de WhatsApp (confirmación de seña, recordatorios) aprobadas y cargadas en ambiente de pruebas.
- [ ] Link de pago de prueba en Mercado Pago (modo sandbox) con monto actualizado y `notification_url` apuntando a staging.
- [ ] Logs y dashboards visibles (telemetría de entrevista, pagos, consentimientos) con filtros para el lead LV-2024-09.
- [ ] Mockups base precargados y personalizables para inmobiliaria.
- [ ] Agenda de calendario conectada (slot de ejemplo disponible y permisos verificados).
- [ ] Mensajes legales (T&Cs, privacidad, opt-in) revisados y consistentes con la demo.
- [ ] Equipo alineado con guion y roles de narrador/operador definidos.

## Notas para la narración
- Reforzar que la seña se descuenta del proyecto final y es reembolsable bajo ciertas condiciones.
- Mencionar que los datos sensibles se almacenan en forma segura y con retención de 12 meses.
- Destacar fallback por email si WhatsApp no estuviese disponible.

## Próximos pasos hacia Prototipado
1. Probar secuencia completa en entorno sandbox con telemetría real.
2. Ajustar tiempos de respuesta del agente para cumplir NFR (p95 <4s).
3. Iterar con feedback interno y preparar versión en inglés para expansión regional.
