# Matriz de Pruebas Funcionales y de Controles

## Introducción
La siguiente matriz consolida los casos críticos del MVP PANOS (Argentina) cruzando cada flujo funcional con los objetivos de negocio, los datos requeridos, los resultados esperados y la evidencia que debe capturarse para auditoría y mejora continua. Incluye escenarios de error y referencia explícita a los requisitos no funcionales (NFR) definidos en `docs/spec/nfr_mvp.md`.

## Flujo: Entrevista Guiada
| Objetivo | Pasos | Datos | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Validar flujo feliz de entrevista desde landing hasta brief preliminar | 1. Ingresar a landing.<br>2. Autenticarse/identificarse.<br>3. Completar preguntas dinámicas.<br>4. Confirmar resumen y consentimientos. | Prospecto inmobiliaria ("Estudio Andina"), presupuesto ARS 3.5M, integraciones Mercado Pago/WhatsApp, opt-in otorgado. | Se generan respuestas persistidas, brief preliminar con campos Req completos, consentimientos registrados (timestamp, IP). | Captura de pantalla del resumen, log `interview_completed` con request_id, export JSON del brief. |
| Verificar validaciones de negocio mínimas | 1. Repetir flujo feliz.<br>2. Ingresar presupuesto menor al mínimo.<br>3. Dejar sin seleccionar integraciones obligatorias. | Presupuesto ARS 200k, sin opt-in. | Sistema bloquea avance, muestra errores contextuales, no persiste brief incompleto. | Screenshot de mensajes de error, log `validation_error` con campo y regla, registro de auditoría sin brief creado. |
| Simular interrupción y reanudación | 1. Completar 50% de preguntas.<br>2. Cerrar sesión.<br>3. Reingresar y continuar. | Misma PyME, navegador Chrome, cookies habilitadas. | Estado se reanuda desde última pregunta, sin pérdida de datos, timestamps consistentes. | Log `session_resume`, captura UI con paso retomado, diff de respuestas antes/después. |

## Flujo: Generación de Mockups Iniciales
| Objetivo | Pasos | Datos | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Confirmar generación automática post-entrevista | 1. Finalizar entrevista feliz.<br>2. Solicitar mockups desde chat.<br>3. Verificar panel lateral y página dedicada. | Brief completado, vertical inmobiliaria, layout sugerido (home, dashboard, panel propiedades). | Mockups wireframe se generan en < 2 min, preview accesible, enlaces descargables, registro en base de datos. | Captura de mockups, log `mockup_generated` con duración, almacenamiento de URL en base. |
| Manejo de cambios rápidos | 1. Solicitar ajuste (ej. agregar filtro barrios).<br>2. Confirmar nueva versión. | Requerimiento textual en chat. | Nueva iteración con versión incrementada, historial visible, tiempos dentro de NFR p95<8s. | Log de `mockup_revision`, comparación de versiones, timestamp. |
| Error en proveedor de mockups | 1. Forzar fallo (simular 500).<br>2. Observar fallback. | Payload mínimo, flag error. | Usuario recibe mensaje con retry/soporte, sistema encola reintento (máx 3) con backoff, alerta en observabilidad. | Log `mockup_error`, alerta registrada, captura del mensaje de fallback. |

## Flujo: Pago de Seña (Mercado Pago Checkout Pro / Link)
| Objetivo | Pasos | Datos | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Cobro exitoso y comprobante | 1. Desde brief aprobado, generar link de pago.<br>2. Redirigir a Checkout Pro sandbox.<br>3. Completar pago aprobado.<br>4. Volver a PANOS y descargar comprobante. | Monto ARS 150.000, descripción "Seña MVP PANOS", email test@cliente.com, documento ficticio válido. | Estado pasa a `PAGADO_OK`, se registra payment_id, status approved, comprobante PDF con datos obligatorios, agenda habilitada. | Log `payment_success`, webhook registrado (<3s), copia comprobante, captura de agenda disponible. |
| Pago rechazado | 1. Repetir flujo pero con tarjeta simulada rechazada.<br>2. Observar mensajes y opciones. | Tarjeta sandbox `rejected_call_for_authorize`. | Estado `PAGO_FALLIDO`, usuario informado, CTA reintentar o cambiar medio, no se genera comprobante. | Log `payment_failed` con código, screenshot mensaje, registro de intento. |
| Abandono del pago | 1. Generar link.<br>2. Cerrar ventana antes de pagar.<br>3. Esperar expiración. | Link válido 30 min. | Estado `ABANDONO` tras timeout, notificación email/WhatsApp pendiente, reintento opcional. | Log `payment_abandoned`, timestamp expiración, evidencia de notificación enviada. |
| Webhook no recibido | 1. Completar pago exitoso.<br>2. Bloquear recepción webhook (simulado).<br>3. Consultar estado vía API fallback. | Payment_id sandbox. | Sistema detecta ausencia de webhook en 2 min, ejecuta `status_polling`, actualiza registro. | Log `webhook_timeout`, registro del polling, anotación en auditoría. |

## Flujo: Agenda y Confirmación
| Objetivo | Pasos | Datos | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Agendar reunión tras pago | 1. Luego de pago aprobado, seleccionar franja en calendario integrado.<br>2. Confirmar. | Franja martes 10:00 ART, Google Calendar sandbox. | Evento creado, invitaciones email/WhatsApp enviadas, estado `AGENDA_DISPONIBLE`. | Log `meeting_scheduled`, screenshot confirmación, registro ICS. |
| Reagendar / cancelar | 1. Abrir dashboard.<br>2. Cambiar franja.<br>3. Confirmar cancelación previa. | Nueva franja jueves 15:00. | Evento previo cancelado (status cancelled), nuevo evento creado, notificaciones reemitidas. | Log `meeting_rescheduled`, ICS cancelado, confirmación al usuario. |
| Error en calendar API | 1. Simular 500 al crear evento.<br>2. Reintentar. | Payload válido. | Sistema guarda encola reintento (máx 3), avisa soporte y mantiene estado previo hasta confirmación. | Log `calendar_error`, alerta soporte, nota en back-office. |

## Flujo: Mensajería WhatsApp (Meta Cloud API)
| Objetivo | Pasos | Datos | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Envío de plantilla post-pago | 1. Tras pago OK, disparar plantilla `confirmacion_sena`. | Número E.164 con opt-in registrado, template ID. | Mensaje enviado dentro ventana, status delivered/read (si aplica). | Log `whatsapp_template_sent` con message_id, captura del mensaje, registro consent_version. |
| Opt-in ausente | 1. Intentar enviar mensaje sin opt-in previo. | Número sin registro `opt_in`. | Sistema bloquea envío, registra error y notifica necesidad de consentimiento. | Log `whatsapp_optin_missing`, screenshot mensaje UI, ticket follow-up. |
| Manejo de opt-out | 1. Usuario responde "STOP" (simulado). | Template marketing previo. | Opt-out registrado, se bloquean futuros envíos no transaccionales, confirmación enviada. | Log `whatsapp_optout`, actualización base, evidencia de mensaje confirmatorio. |
| Error plantilla rechazada | 1. Forzar respuesta `template_rejected`. | Template modificada sin aprobación. | Sistema captura error, alerta a operaciones, fallback email enviado. | Log `whatsapp_error`, alerta en observabilidad, copia email fallback. |

## Criterios de Aceptación vs NFR
| Flujo | NFR asociado | Criterio de aceptación | Evidencia requerida |
| --- | --- | --- | --- |
| Entrevista | Performance p95<4s, Privacidad (retención 12m) | Tiempo de respuesta agregado <4s, campos sensibles enmascarados en logs, retención configurada. | Reporte de latencias, screenshot configuración retención, auditoría de logs. |
| Mockups | Performance p95<8s, Disponibilidad 99.5% | Generación en <8s y sin errores durante ventana de prueba, fallback notifica soporte <2 min. | Métricas en dashboard, log de incidentes. |
| Pago | Seguridad PCI alcance mínimo, Webhooks <3s, Disponibilidad | No almacenar PAN/CSC, webhook procesado <3s, fallback de polling probado. | Evidencia de configuración PCI, log webhook timestamps, resultado prueba manual. |
| Agenda | Resiliencia (backoff), Observabilidad | Reintentos configurados (3), alertas activas si falla API, métricas de scheduling. | Configuración de backoff, alerta enviada, gráfico métricas. |
| WhatsApp | Consentimiento verificado, Latencia <4s | Envíos solo con opt-in, logs con consent_version, latencia promedio <4s. | Registro opt-in, logs estructurados, reporte latencia. |

## Próximos Pasos
- Integrar esta matriz al plan de pruebas (`docs/spec/pruebas_plan.md`) y automatizar la recolección de evidencias en el dashboard QA.
- Preparar scripts de simulación para Mercado Pago y Meta Cloud API que permitan ejecutar los casos de error sin afectar reputación.
- Alinear al equipo de SRE/Soporte con la política de almacenamiento de evidencias y tiempos de respuesta definidos en los NFR.
