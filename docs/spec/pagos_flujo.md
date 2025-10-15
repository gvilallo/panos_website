# Flujo de Pago de Seña (MVP Argentina)

## 1. Máquina de Estados Textual
- **INICIADO → LINK_GENERADO**
  - **Disparador**: Orquestador tras confirmar alcance y monto de seña.
  - **Entrada**: brief validado, monto de seña, medio preferido, consentimiento a T&Cs/Privacidad.
  - **Salida**: solicitud de creación de link en Mercado Pago (Checkout Pro / Link de Pago).
  - **Eventos & Telemetría**: `payment_flow.start`, `brief_id`, `prospect_id`, timestamp.
- **LINK_GENERADO → REDIRECCION_MP**
  - **Disparador**: Servicio de Pagos recibe preferencia aprobada por Mercado Pago.
  - **Entrada**: `init_point`, `external_reference`, `notification_url`.
  - **Salida**: URL firmada enviada al Front, registro de auditoría con IP, user_agent.
  - **Eventos & Telemetría**: `payment_link.created`, `external_reference`, tiempo de respuesta API.
- **REDIRECCION_MP → PAGADO_OK**
  - **Disparador**: Webhook/IPN con estado `approved` o callback de éxito.
  - **Entrada**: payload Mercado Pago (`payment_id`, `status`, `transaction_amount`, `payer_email`).
  - **Salida**: actualización de orden de seña a `paid`, publicación de evento interno.
  - **Eventos & Telemetría**: `payment.approved`, latencia, hash de payload verificado.
- **PAGADO_OK → COMPROBANTE_EMITIDO**
  - **Disparador**: Servicio de Pagos confirma idempotencia y conciliación mínima.
  - **Entrada**: datos del pago, plantilla de comprobante, datos fiscales PANOS.
  - **Salida**: comprobante PDF/HTML generado, enviado por email y almacenado en repositorio seguro.
  - **Eventos & Telemetría**: `receipt.generated`, `storage_location`, checksum archivo.
- **COMPROBANTE_EMITIDO → AGENDA_DISPONIBLE**
  - **Disparador**: Orquestador detecta comprobante disponible.
  - **Entrada**: `payment_id`, `receipt_url`, preferencias de agenda, opt-in WhatsApp.
  - **Salida**: slots de agenda habilitados, mensajes de confirmación disparados.
  - **Eventos & Telemetría**: `agenda.slot_offered`, métricas de conversión pago→agenda.
- **REDIRECCION_MP → PAGO_FALLIDO**
  - **Disparador**: Webhook con estado `rejected`/`cancelled`.
  - **Entrada**: payload con causa de rechazo, códigos de error.
  - **Salida**: notificación al prospecto, CTA a reintentar, alerta a soporte si recurrente.
  - **Eventos & Telemetría**: `payment.rejected`, motivo, contador de reintentos.
- **REDIRECCION_MP → ABANDONO**
  - **Disparador**: timeout front (sin retorno en X minutos) o webhook `pending` sin actualización.
  - **Entrada**: `external_reference`, timestamp último evento.
  - **Salida**: recordatorio automatizado, registro en back-office para seguimiento.
  - **Eventos & Telemetría**: `payment.abandoned`, duración, canal del recordatorio.
- **LINK_GENERADO → EXPIRADO**
  - **Disparador**: expiración del link según configuración Mercado Pago.
  - **Entrada**: marca de expiración, configuración TTL.
  - **Salida**: invalidación del link, generación opcional de nuevo link.
  - **Eventos & Telemetría**: `payment.expired`, TTL, número de regeneraciones.
- **PAGO_FALLIDO/ABANDONO/EXPIRADO → REINTENTO**
  - **Disparador**: usuario solicita nuevo intento desde front o soporte.
  - **Entrada**: motivo, datos actualizados si aplica (monto, contacto).
  - **Salida**: nueva transición a `LINK_GENERADO` con control de duplicados.
  - **Eventos & Telemetría**: `payment.retry_requested`, `retry_count`, resultado final.

## 2. Requisitos Funcionales (MVP Argentina)
- **Medio de Pago**: Mercado Pago Checkout Pro / Link de Pago para minimizar alcance PCI.
- **Campos mínimos al crear link**: `transaction_amount` (monto seña), `description` (referencia proyecto + "seña"), `external_reference` (UUID del brief), `notification_url` (webhook PANOS).
- **Persistencia de resultados**: guardar `payment_id`, `status`, `status_detail`, `payer_email`, `transaction_amount`, `currency_id`, `payment_method_id`, `operation_type`, `processed_at`.
- **Comprobante automático**:
  - Formato PDF o HTML protegido.
  - Contenido: datos prospecto, monto y moneda, fecha/hora, `payment_id`, condición tributaria PANOS, política de devoluciones, contacto soporte.
  - Distribución: email + descarga en back-office.

## 3. Alternativa Exportable
- **Stripe Checkout** (referencia para LATAM ampliado):
  - **Parámetros equivalentes**: `amount`, `currency`, `mode=payment`, `success_url`, `cancel_url`, `client_reference_id`, `metadata` (brief_id), `payment_intent_data[description]`.
  - **Datos a persistir**: `checkout_session_id`, `payment_intent`, `payment_status`, `customer_email`, `amount_total`, `charge_id`, timestamps.
  - **Consideraciones**: requiere manejo de claves secretas, Webhook con firma (`Stripe-Signature`).

## 4. Política de Devoluciones de la Seña
- **Casos**: cancelación por parte de PANOS, cambio de alcance que imposibilita el proyecto, incumplimiento de plazos por PANOS.
- **Plazos**: respuesta inicial ≤ 48h, ejecución de devolución ≤ 10 días hábiles.
- **Canal**: solicitud vía email soporte@panos o formulario back-office; trazabilidad en ticketing.
- **Validaciones**: verificación de identidad (email registrado, IP histórica), confirmación de monto y `payment_id`, aprobación interna (socio PANOS).
- **Auditoría**: registrar `refund_id`, `approved_by`, timestamp, motivo categorizado, comunicación enviada.

## 5. Seguridad y Cumplimiento
- **Protección de datos**: no almacenar PANs ni CSC; solo tokens/IDs provistos por Mercado Pago.
- **Webhooks**: validar `X-Hub-Signature` o token secreto; rechazar payloads no firmados.
- **Logs obligatorios**: IP, user_agent, `external_reference`, `payment_id`, estado, monto, moneda, timestamp, `notification_url`, resultado de validación.
- **PCI**: mantener alcance SAQ-A (solo redirección). Documentar evidencias y pruebas anuales.
- **Privacidad**: enlaces visibles a T&Cs y Política de Privacidad en cada pantalla relacionada al pago; almacenar consentimiento y opt-in relacionados.

## 6. Pruebas Manuales (Sin Integración Real)
| Caso | Pasos | Datos de ejemplo | Resultado esperado | Evidencia |
| --- | --- | --- | --- | --- |
| Pago OK | Generar link sandbox → simular aprobación vía webhook mock | `transaction_amount=50000`, `status=approved` | Estado pasa a `PAGADO_OK`, comprobante generado, agenda habilitada | Screenshot confirmación + `log_id` de webhook |
| Pago rechazado | Trigger webhook con `status=rejected` | `status_detail=cc_rejected_insufficient_data` | Estado `PAGO_FALLIDO`, mensaje de reintento, alerta soporte | Log estructurado con causa + captura UI |
| Abandono | No recibir webhook en 15 min → job marca abandono | - | Estado `ABANDONO`, envío de recordatorio | Registro cron job + historial mensajes |
| Expirado | Configurar TTL corto → esperar expiración | `expiration_date=+30min` | Estado `EXPIRADO`, CTA generar nuevo link | Captura UI + log expiración |
| Reintento | Tras fallo, pulsar "Reintentar pago" → crear nuevo link | `retry_count=1` | Retorno a `LINK_GENERADO`, seguimiento de duplicados | Log de retry + confirmación link |

## 7. Matriz Estados ↔ UI/UX
| Estado | Mensaje en pantalla | CTA principal | Mensajes secundarios |
| --- | --- | --- | --- |
| INICIADO | "Estamos generando tu enlace de seña" | Ninguna (spinner) | Recordatorio de monto y T&Cs |
| LINK_GENERADO | "Tu enlace de pago está listo" | "Pagar ahora" (abre Mercado Pago) | Link a Política de Privacidad |
| REDIRECCION_MP | "Redirigiendo a Mercado Pago" | "Reintentar" (si falla) | Contacto soporte |
| PAGADO_OK | "Pago aprobado" | "Descargar comprobante" | Mensaje sobre agenda próxima |
| COMPROBANTE_EMITIDO | "Comprobante enviado" | "Elegir horario" | Link para reenviar comprobante |
| AGENDA_DISPONIBLE | "Seleccioná tu franja" | "Agendar" | Información de contacto PANOS |
| PAGO_FALLIDO | "No pudimos procesar tu pago" | "Reintentar" | Canal soporte, sugerencias de medios |
| ABANDONO | "¿Seguís ahí?" | "Volver al pago" | Recordatorio de vigencia |
| EXPIRADO | "El enlace de pago expiró" | "Generar nuevo enlace" | Información de soporte |
| REINTENTO | "Creando un nuevo enlace" | "Pagar ahora" | Historial de intentos |

## 8. Checklist Definition of Done del Flujo
1. Campos obligatorios (`transaction_amount`, `description`, `external_reference`, `notification_url`) validados y auditados.
2. Evidencia de consentimiento (T&Cs, Privacidad, opt-in WhatsApp) asociada al `external_reference`.
3. Webhook Mercado Pago simulado y verificación de firma documentada.
4. Comprobante generado, almacenado y accesible desde front/back-office.
5. Agenda habilitada automáticamente tras `PAGADO_OK`, con notificación enviada (email + WhatsApp si opt-in).
6. Logs estructurados enviados a observabilidad con correlación `payment_flow_id`.
7. Procedimiento de reintento y manejo de expiración probado y documentado.

## Próximos Pasos
1. Prototipar mock server de Mercado Pago para pruebas de contrato.
2. Integrar generación real de comprobante con plantilla aprobada legalmente.
3. Automatizar pruebas de regresión del flujo de pago dentro del pipeline CI.
