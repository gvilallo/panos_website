# Requisitos No Funcionales del MVP PANOS

## 1. Disponibilidad y resiliencia
- **Objetivo MVP**: disponibilidad mensual ≥ 99.5% para el front conversacional y el orquestador de sesiones.
- **Topología**: despliegue inicial en una sola zona de disponibilidad (single AZ) con health checks; plan para evolucionar a multi-AZ antes de superar 500 sesiones activas simultáneas.
- **Reintentos**:
  - Pagos: backoff exponencial (3 intentos, 5s/15s/30s) ante fallas temporales de Mercado Pago y re-proceso de webhooks idempotentes.
  - WhatsApp: hasta 2 reintentos con backoff incremental (10s/60s) y escalado a email si se agota.
- **Modos degradados**:
  - Si WhatsApp está indisponible (>5 minutos), activar fallback de notificaciones vía email con el mismo contenido.
  - Si el generador de mockups falla, proveer resumen textual y notificar al equipo PANOS para follow-up manual.

## 2. Performance y latencia
- **Interacciones de chat/acciones del agente**: p50 < 1.5 s, p95 < 4 s desde solicitud hasta respuesta renderizada.
- **Generación y resumen del brief**: p95 < 8 s incluyendo llamadas al LLM y persistencia.
- **Procesamiento de webhooks de pago**: latencia promedio < 3 s desde recepción hasta confirmación al usuario.
- **Páginas SSR (Next.js)**: TTFB objetivo < 500 ms para usuarios en Argentina y < 800 ms para LatAm.
- **Carga concurrente**: soportar al menos 100 sesiones de chat concurrentes con degradación lineal controlada (<15% de incremento en p95).

## 3. Seguridad y cumplimiento
- **Gestión de secretos**: almacenar llaves API en Secret Manager o variables de entorno cifradas; rotación trimestral mínima.
- **Logging/audit**: registrar quién (usuario/ID sesión), qué acción ejecutó, cuándo (timestamp ISO 8601) y resultado (status) para pasos críticos (pagos, consentimientos, cambios de brief).
- **Consentimientos**: validar opt-in de WhatsApp antes de cada envío automatizado; bloquear envío si no hay evidencia registrada.
- **PCI**: acotar el alcance usando Mercado Pago Checkout Pro; nunca almacenar PAN/CSC ni datos sensibles de tarjetas.

## 4. Privacidad y retención
- **Retención por defecto**: 12 meses para briefs, consentimientos, registros de pago y logs asociados al MVP.
- **Excepciones**: evidencias de pago y contratos se retienen 24 meses; logs de depuración sensibles se purgan a los 90 días.
- **Derechos ARCO**: procesar solicitudes de acceso/borrado en ≤ 10 días hábiles; registrar responsable y fecha de cierre.
- **Pseudonimización**: usar identificadores internos al exportar datos a analítica; anonimizar campos personales (email, teléfono) con hashing irreversible cuando no se requiera contacto.

## 5. Observabilidad
- **Logs**: formato JSON estructurado con `request_id`, `user_id` y `session_id` para correlación; retención mínima 90 días.
- **Métricas**: instrumentar tasas de conversión de entrevista a pago, porcentaje de pagos aprobados, latencias p50/p95 de chat, cantidad de opt-ins/opt-outs y tasa de entrega de WhatsApp.
- **Alertas**: definir umbrales automáticos (ej. disponibilidad < 99%, tasa de pagos fallidos > 10%, latencia p95 > 6 s) con responsable on-call del equipo PANOS.
- **Tracing ligero**: habilitar tracing distribuido para llamadas críticas (LLM, pagos, WhatsApp) con muestreo al menos del 10%.

## 6. Accesibilidad e internacionalización
- **Cumplimiento mínimo**: WCAG 2.1 AA para contraste, foco visible, navegación con teclado y etiquetas semánticas en formularios.
- **Idiomas**: interfaz en español (es-AR) con preparación para i18n (en-US y pt-BR) mediante archivos de recursos; evitar hardcodear textos.
- **Compatibilidad**: asegurar experiencia usable en desktop y mobile (viewport ≥ 360px) con lectores de pantalla populares.

## 7. Escalabilidad y límites
- **Colas y orquestación**: máximo 50 jobs/minuto en la cola de tareas; monitorear y escalar al llegar a 70% de uso sostenido.
- **Rate limiting**: 30 solicitudes/minuto por usuario autenticado, 10 solicitudes/minuto para visitantes, con mensajes de error claros.
- **Límites externos**: monitorear cuotas de WhatsApp (mensajes/24h) y Mercado Pago (llamadas/min) para planificar upgrades.
- **Plan de escalado**: si las métricas superan 200 sesiones/día o 100 pagos/día, preparar despliegue multi-AZ y caché para respuestas frecuentes.

## 8. Backup y recuperación
- **Backups**: realizar backups completos diarios de Postgres con retención de 7 días en caliente y 30 días en almacenamiento frío cifrado.
- **Restauración**: ejecutar prueba de restauración mensual documentada; objetivo RPO ≤ 24 h, RTO ≤ 4 h para la base principal.
- **Versionado**: mantener historial de esquemas (migraciones) y validar compatibilidad durante recuperaciones.

## 9. Operación (SRE light)
- **Runbooks**: documentar procedimientos para caída de pagos, indisponibilidad de WhatsApp, rollback de despliegues y pérdida de datos.
- **Mantenimientos**: comunicar ventanas planificadas con 48 h de anticipación; limitar a domingos 22:00–02:00 ART.
- **Deploys**: cadencia mínima semanal; estrategia rolling simple con posibilidad de rollback automatizado en <15 minutos.

## 10. Definition of Done (NFR)
- Métricas y alertas configuradas en panel de monitoreo (ej. Grafana/Datadog) con responsables asignados.
- Pruebas de carga livianas ejecutadas y documentadas alcanzando objetivos p95 (<4 s para chat).
- Prueba de restauración de backup ejecutada y registrada.
- Revisión de cumplimiento (privacidad, T&Cs, opt-in WhatsApp) completada con checklist firmada.

## Tabla: Métricas y Umbrales del MVP

| Nombre | Objetivo | Umbral alerta | Medición | Frecuencia | Dueño |
| --- | --- | --- | --- | --- | --- |
| Disponibilidad Front | ≥ 99.5% mensual | < 99% | Ping synthetic monitor | 5 min | Líder SRE |
| Latencia p95 Chat | < 4 s | ≥ 6 s | APM/Tracing | 5 min | Tech Lead Backend |
| Pagos aprobados | ≥ 90% | < 80% | Webhooks Mercado Pago | Diario | Product Ops |
| Webhooks procesados <3 s | ≥ 95% | < 85% | Métrica de procesamiento | 15 min | Backend |
| Opt-ins válidos | 100% antes de enviar | < 95% | Auditoría automatizada | Diario | Compliance |
| Errores WhatsApp | < 5% | ≥ 10% | Logs estructurados | 10 min | Integraciones |
| Backups exitosos | 100% | < 100% | Reporte backup | Diario | DBA |
| SLA ARCO | ≤ 10 días hábiles | > 10 días | Registro de solicitudes | Semanal | Legal |
| Accesibilidad issues críticos | 0 | ≥ 1 | Auditoría manual | Lanzamiento + trimestral | UX |
| Retención de logs | ≥ 90 días | < 90 días | Revisión automatizada | Mensual | SRE |

## Próximos pasos hacia Prototipado
1. Validar herramientas de monitoreo (stack elegido) y configurar panel inicial.
2. Definir scripts automatizados de prueba de carga ligera y documentar baseline.
3. Completar runbooks y asignar responsables on-call.
4. Integrar los NFR en el backlog del MVP con historias técnicas vinculadas.
