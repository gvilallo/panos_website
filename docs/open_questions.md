# Preguntas abiertas y ambigüedades clave

| Pregunta | Impacto | Prioridad | Dueño | Fecha objetivo | Notas |
| --- | --- | --- | --- | --- | --- |
| ¿Qué tipo de comprobante fiscal (Factura B/C) debemos emitir para la seña según categoría impositiva del cliente en Argentina? | Legal/fiscal, riesgo de sanciones AFIP | Alta | Finanzas + Estudio Contable | 2024-04-10 | Bloquea MVP: Sí. Define integración AFIP y contenido del comprobante automático. |
| ¿Debemos emitir el comprobante electrónicamente en tiempo real vía AFIP o puede diferirse mediante ERP/manual? | Cumplimiento y experiencia del cliente | Alta | Finanzas + Operaciones | 2024-04-10 | Bloquea MVP: Sí. Impacta en diseño del flujo de comprobantes del módulo Pago/Onboarding. |
| ¿Cuál es la política de devolución/cancelación aplicable a la seña según Defensa del Consumidor (plazos, condiciones, medios)? | Legal/comercial | Media | Legal + Ventas | 2024-04-12 | Bloquea MVP: No, pero condiciona T&Cs y mensajes de confirmación. |
| ¿Qué datos tributarios (CUIT/CUIL, domicilio) son obligatorios antes del cobro de la seña? | Cumplimiento KYC | Alta | Legal + Producto | 2024-04-09 | Bloquea MVP: Sí. Determina formularios de captura y validaciones. |
| ¿Cómo se realizará la conciliación bancaria de Mercado Pago (reportes, periodicidad, integración con contabilidad)? | Operaciones financieras | Media | Finanzas + Back-office | 2024-04-15 | Bloquea MVP: No, pero afecta procesos diarios y backlog de automatización. |
| ¿Qué procedimiento de opt-in doble debemos implementar para WhatsApp Cloud API y dónde se almacena la prueba? | Privacidad y mensajería | Alta | Legal + Producto Conversacional | 2024-04-08 | Bloquea MVP: Sí. Sin opt-in válido Meta puede bloquear mensajes proactivos. |
| ¿Cuáles son los límites y plantillas aprobadas para mensajes proactivos de WhatsApp en Argentina? | Operación de mensajería | Media | Marketing + Producto Conversacional | 2024-04-11 | Bloquea MVP: No, pero condiciona recordatorios y escalado. |
| ¿Qué política de retención y eliminación aplicaremos para datos personales y comprobantes (Ley 25.326 vs. AFIP)? | Privacidad y gobernanza de datos | Alta | Legal + Seguridad | 2024-04-12 | Bloquea MVP: Sí. Impacta diseño de base de datos y jobs de limpieza. |
| ¿Dónde residirán los datos (proveedor cloud) y se requieren cláusulas específicas para transferencias internacionales? | Legal y hosting | Media | Seguridad + Infraestructura | 2024-04-16 | Bloquea MVP: No, pero debe resolverse antes del ADR de hosting. |
| ¿Qué expectativas tienen los clientes argentinos respecto a medios alternativos de pago (transferencia, billeteras locales) y cómo se comunica el alcance del MVP? | Comercial/UX | Media | Ventas + Producto | 2024-04-12 | Bloquea MVP: No, pero evita churn post-entrevista. |
| ¿Qué proveedor gestionará la infraestructura (Render, Fly.io, Vercel) y cómo aseguramos cumplimiento local de datos/latencia? | Operación técnica | Alta | Ingeniería | 2024-04-09 | Bloquea MVP: Sí. Requisito del ADR_0005_hosting y despliegue continuo. |
| ¿Cómo monitorearemos la disponibilidad de Checkout Pro y definiremos plan de contingencia ante caídas de Mercado Pago? | Continuidad operativa | Media | Ingeniería + Finanzas | 2024-04-13 | Bloquea MVP: No, pero debe documentarse en ADR_0002_pagos. |

## Próximos pasos
- Asignar responsables para resolver cada pregunta y registrar decisiones en los ADRs correspondientes.
- Actualizar backlog del MVP con tareas derivadas de cada respuesta y ajustar dependencias Must/Should.
- Preparar insumos para la fase de Prototipado una vez cerradas las dependencias críticas del MVP.
