# Políticas y lineamientos de WhatsApp Business (Meta Cloud API) para el MVP

## 1. Requisitos de cumplimiento
- **Opt-in explícito**
  - *Canales válidos*: formularios web (checkbox no preseleccionado), confirmación por email, QR con URL dedicada, mensajes entrantes desde el número oficial.
  - *Texto de consentimiento sugerido*: "Autorizo a PANOS a contactarme vía WhatsApp sobre el avance de mi proyecto y recordatorios operativos".
  - *Evidencia obligatoria*: `timestamp`, `ip`, `user_agent`, `canal` (web, email, presencial), `version_texto`, `prospect_id` o `lead_id`.
- **Ventanas y límites**
  - *Sesión de servicio de 24h*: respuesta dentro de 24 horas desde el último mensaje del usuario. Después de ese plazo se requieren plantillas aprobadas.
  - *Mensajes template*: marketing solo con categoría Marketing, recordatorios y pagos como Utility/Transactional. Monitorear tasas de entrega, bloqueos y calificación de calidad.
  - *Reputación*: respetar límites de volumen inicial (1k conversaciones/24h) y escalar conforme la cuenta mantenga buena calidad.
- **Alta y verificación**
  - Registrar cuenta de WhatsApp Business Manager y completar verificación de empresa en Meta.
  - Verificar el número telefónico con capacidad de recepción de llamadas o SMS.
  - Clasificar plantillas por categoría (TRANSACTIONAL, MARKETING) y mantener versión aprobada.

## 2. Plantillas iniciales (HSM)
| ID sugerido | Categoría | Idioma | Texto con variables | Ejemplo instanciado |
| --- | --- | --- | --- | --- |
| `pago_sena_confirmacion_v1` | TRANSACTIONAL | es_AR | "Hola {{1}}, confirmamos la recepción de tu seña de {{2}} para el proyecto {{3}}. Adjuntamos el comprobante y próximos pasos." | "Hola Carla, confirmamos la recepción de tu seña de ARS 150.000 para el proyecto Panel Propiedades. Adjuntamos el comprobante y próximos pasos." |
| `entrevista_recordatorio_24h_v1` | TRANSACTIONAL | es_AR | "Hola {{1}}, te recordamos la entrevista con PANOS el {{2}} a las {{3}}. Responde este mensaje si necesitás reprogramar." | "Hola Carla, te recordamos la entrevista con PANOS el 14/05/2024 a las 10:00. Responde este mensaje si necesitás reprogramar." |
| `entrevista_recordatorio_2h_v1` | TRANSACTIONAL | es_AR | "{{1}}, faltan {{2}} horas para tu entrevista con PANOS. Unite usando el link {{3}}." | "Carla, faltan 2 horas para tu entrevista con PANOS. Unite usando el link https://panos.link/meet" |
| `brief_bienvenida_v1` | TRANSACTIONAL | es_AR | "Gracias {{1}} por completar el brief. En breve recibirás los mockups iniciales y la propuesta. ¿Querés dejarnos un comentario adicional?" | "Gracias Carla por completar el brief. En breve recibirás los mockups iniciales y la propuesta. ¿Querés dejarnos un comentario adicional?" |

## 3. Registro de consentimientos
- **Campos mínimos**: `consent_type`, `text_version`, `channel`, `timestamp`, `ip`, `user_agent`, `source_page`, `evidence_id` (opcional) y relación con el contacto.
- **Flujo de opt-out (STOP)**: palabra clave "STOP" o "BAJA" desactiva envíos. Registrar `timestamp`, `canal`, `motivo`. Actualizar flag `whatsapp_opt_in=false` y reportar a Meta via API de suscripciones. Confirmar opt-out al usuario.

## 4. Reglas de envío
- **Sesión vs plantilla**: dentro de la ventana de 24h se pueden enviar mensajes libres; fuera de ventana solo plantillas aprobadas.
- **Reintentos y errores**: máximo 3 intentos con backoff exponencial. Para `INVALID_NUMBER`, marcar contacto para verificación manual. Si `Outside 24h window`, reenviar usando plantilla o avisar vía email. Documentar rechazo de plantilla y reenviar una vez solucionado.
- **Anti-spam**: limitar a 4 mensajes no solicitados por semana por contacto, priorizar contenido útil y permitir opt-out en cada interacción.

## 5. Observabilidad
- **Logs mínimos**: `message_id`, `to`, `template_id` (si aplica), `status` (queued, sent, delivered, read), `error_code`, `latency_ms`, `timestamp`, `webhook_id`.
- **Métricas clave**: tasa de entrega, lectura (si disponible), respuesta, bloqueos, opt-outs y ratio de plantillas aprobadas vs rechazadas.

## 6. Riesgos y mitigaciones
- **Rechazo de plantillas**: Mitigar con revisión legal y de marca antes de enviar a Meta, versionado controlado.
- **Pérdida de reputación**: Monitorear métricas y reducir volumen si la calificación baja; ejecutar campañas de re-engagement solo con opt-in renovado.
- **Opt-in insuficiente**: Validar canales de captura y reforzar copys en web y seguimiento manual.
- **Bloqueo temporal**: Configurar alertas cuando status cambia; preparar canal alternativo (email/sms) para notificaciones críticas.

## 7. Checklist Definition of Done (MVP)
- Opt-in registrado y persistido antes del primer mensaje por contacto.
- Al menos 3 plantillas aprobadas y listas en ambiente de producción.
- Manejo de opt-out funcionando y sincronizado con Meta.
- Logging y métricas básicos operativos con alertas para errores críticos.

## Próximos pasos hacia Prototipado
1. Implementar almacenamiento de consentimientos con auditoría.
2. Desarrollar módulo de envío de plantillas y manejo de estados.
3. Configurar tablero de métricas y alertas para reputación y fallos.
4. Validar copys con el equipo legal y marca antes de la solicitud en Meta.
