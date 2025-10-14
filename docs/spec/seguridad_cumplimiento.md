# Seguridad y Cumplimiento

## Autenticación
- **Usuarios externos (prospectos)**: sesiones anónimas firmadas (JWT de corta duración) asociadas a `interviewId`. Renovación mediante refresh token atado al navegador y revocado al completar onboarding.
- **Socios PANOS y soporte**: autenticación federada (OAuth2/OIDC con Azure AD/Google Workspace). MFA obligatorio.
- **Servicios internos**: autenticación mutua mediante JWT firmados por autoridad interna o MTLS para webhooks críticos (Mercado Pago, WhatsApp).
- **Recuperación de sesión**: verificación vía email + token de un solo uso, con expiración 15 minutos.

## Autorización
- **Modelo RBAC** con scopes específicos: `prospect`, `partner_admin`, `support_agent`, `ops_payments`.
- **Políticas**:
  - Prospectos sólo pueden acceder a su entrevista/pago/agenda asociados.
  - `partner_admin` puede ver leads asignados a su región (Argentina inicialmente).
  - `ops_payments` con permisos para descargar comprobantes y ver conciliaciones.
- **Motor de políticas**: middleware que evalúa claims JWT y atributos de recurso; audit trail cuando se deniega acceso.

## Gestión de Secretos
- **Almacenamiento**: vault centralizado (HashiCorp Vault / AWS Secrets Manager) con rotación automática (30 días) para llaves LLM, Mercado Pago, WhatsApp, SMTP.
- **Distribución**: inyección en runtime vía sidecars o variables cifradas. Nunca en repositorios ni configuraciones planas.
- **Claves Mercado Pago**: diferenciar `public_key` (frontend) de `access_token` (backend). Guardar credenciales de producción y sandbox segregadas.
- **WhatsApp Cloud API**: rotar `system_user_access_token` cada 60 días según políticas Meta; proteger `phone_number_id` y `business_account_id`.

## Logs y Auditoría
- **Logs de aplicación**: JSON estructurado con nivel, servicio, requestId. Retención 12 meses en almacenamiento cifrado.
- **Audit trail**: captura cambios en datos sensibles (pagos, consentimientos, agenda). Eventos almacenados en esquema `audit.event_logs` (ver modelo de datos).
- **Acceso a logs**: restringido a equipo de seguridad/operaciones vía IAM; registros de acceso a la plataforma de monitoreo.
- **Protección**: anonimizar payloads (mascarar emails, teléfonos). Evitar almacenar tokens completos en logs.
- **Requerimientos legales AR**: conservar logs de acceso y administración por 2 años (Decreto 1558/2001 para proveedores de servicios).

## Privacidad y Retención
- **Ley 25.326**: obtener consentimiento explícito, permitir acceso, rectificación y supresión.
- **Política de privacidad**: especificar uso de LLMs (procesamiento transfronterizo), retención de datos y mecanismos de baja.
- **Gestión de derechos ARCO**: canal dedicado (email + formulario). SLA 5 días hábiles.
- **Retención por tipo de dato**: ver `docs/spec/datos_modelo.md`. Automatizar workflows de anonimización y purga.
- **Transferencias internacionales**: documentar proveedores (OpenAI/Figma/Datadog) y acuerdos de transferencia (cláusulas contractuales tipo).

## Opt-in WhatsApp
- **Requisitos Meta**: almacenar prueba de opt-in (fecha, canal, IP), permitir opt-out en cada mensaje.
- **Flujo**: checkboxes en la entrevista con copy que incluye finalidad y frecuencia. Registro en tabla `consents`.
- **Plantillas**: sólo mensajes aprobados por Meta; categoría `TRANSACTIONAL` para confirmaciones y recordatorios.
- **Límites**: monitorear niveles de envío (Tier 1 al inicio). Alertas cuando se acerque al límite.
- **Política anti-spam**: máximo 3 intentos de contacto si no hay respuesta, luego derivar a email.

## Cumplimiento Mercado Pago
- **Alta**: credenciales productivas sólo tras validar razón social PANOS y cuenta bancaria local.
- **Checkout Pro**: PANOS hospeda redirección; no almacena datos de tarjeta → fuera de PCI SAQ A.
- **Payment Links**: usados para escenarios fallback; vigilar expiración y reintentos manuales.
- **Comisiones**: documentar estructura (3,49% + IVA aproximado para tarjetas crédito nacionales) y reflejar en `payment_intents`.
- **Comprobantes**: generar comprobante fiscal propio (Factura B) y adjuntar recibo Mercado Pago. Retención 10 años.
- **Privacidad**: aclarar en T&Cs que datos de pago se procesan vía Mercado Pago; no retener PAN (solo tokens).

## Alcance PCI
- **Clasificación**: SAQ A (sin manejo directo de datos de tarjeta). Requerimientos mínimos:
  - Uso exclusivo de componentes alojados por Mercado Pago para captura.
  - Certificar que scripts de checkout no se alteran.
  - Políticas de seguridad documentadas y capacitación anual.

## Seguridad Operacional
- **Gestión de vulnerabilidades**: escaneos mensuales (SAST/DAST) y parches críticos <7 días.
- **Plan de respuesta a incidentes**: playbooks para fuga de datos, caída de integraciones, fraude en pagos.
- **Respaldo**: backups cifrados; pruebas de restauración trimestrales.
- **Continuidad**: runbooks para degradar a procesos manuales (pago offline, confirmación telefónica) si integraciones fallan.

## Próximos pasos
1. Redactar matriz de controles (NIST/ISO 27001) mapeada a requisitos legales argentinos.
2. Implementar prototipo de gestión de secretos y validar rotaciones automáticas.
3. Definir política de retención documentada y procedimientos de anonimización automatizados.
