# Opciones Técnicas Evaluadas

## Front-end (Experiencia Conversacional)
| Criterio | Next.js / React | Vite / React |
| --- | --- | --- |
| Renderizado | SSR/ISR nativo, SEO sólido | CSR rápido; SSR requiere configuración extra |
| Integraciones | Ecosistema maduro (Auth, CMS) | Configuración ligera; requiere selección manual |
| Performance | Optimizaciones de imágenes y routing híbrido | Build muy veloz, hot reload instantáneo |
| Escalabilidad | Soporta rutas app router, edge functions | Necesita orquestar SSR con Node/Express |
| Curva de aprendizaje | Familiar para equipos con React + fullstack | Simple para front puro, menos convenciones |
| Adecuación PANOS | Ideal para landing + app conversacional con SEO | Viable para prototipos rápidos, menos robusto para SSR |

## Backend / Agente Orquestador
| Criterio | FastAPI | NestJS |
| --- | --- | --- |
| Paradigma | Python async, minimalista | Node.js, modular y opinionado |
| Integración LLM | Ecosistema Python rico (langchain, openai) | SDK JS amplio, pero menos maduro en ML |
| Performance | Excelente para IO bound con uvicorn | Muy bueno con TypeScript y clustering |
| Productividad | Rápido para prototipos, tipado opcional | Arquitectura estructurada con inyección de dependencias |
| Observabilidad | Depende de extensiones | Integración nativa con interceptors y guards |
| Adecuación PANOS | Facilita experimentación con agentes y notebooks | Ventaja si equipo es TS; más set-up inicial |

## Vector DB / RAG
| Criterio | Postgres + pgvector | Qdrant |
| --- | --- | --- |
| Complejidad operativa | Unifica datos relacionales y vectores | Servicio especializado separado |
| Performance | Suficiente para dataset mediano; tuning necesario | Optimizado para búsquedas vectoriales |
| Escalabilidad | Escala verticalmente; sharding complejo | Sharding y replicación integrados |
| Costos | Aprovecha infra existente | Puede requerir hosting dedicado |
| Adecuación PANOS | Simplifica stack inicial y reportes | Ideal si se esperan embeddings voluminosos |

## Orquestación de prompts y funciones
- **LangChain**: ecosistema amplio, conectores listos, soporta memory y chains complejas. Riesgo de sobre-ingeniería.
- **LlamaIndex**: enfoque en gestión de documentos y agents modular, buena integración con RAG.
- **Propietario ligero (custom state machine)**: control granular, menor dependencia externa, requiere más esfuerzo inicial.

## Pagos
| Criterio | Mercado Pago (AR) | Stripe |
| --- | --- | --- |
| Cobertura | Amplio uso en Argentina, soporta cuotas, transferencias y Pago Fácil/Rapipago | Soporta múltiples países LATAM, experiencia homogénea |
| Cumplimiento | Requisitos locales (CUIT, facturación AFIP, comprobantes electrónicos) | PCI completo, documentación extensa |
| Experiencia usuario | Checkout Pro reconocido y confiable, links de pago reutilizables | UX pulido, pago en un clic para tarjetas |
| Integración | Checkout Pro (hosted) reduce alcance PCI; Payments API requiere tokenización y servidor seguro | SDK completo, requiere adaptación fiscal local |
| Conciliación | Reportes nativos, liquidaciones en pesos, comisiones 3-6% según plan | Reportes multimoneda; liquidación en USD/moneda local |
| Adecuación PANOS | Clave para adopción local y conciliación | Alternativa para clientes internacionales |

### Detalle Mercado Pago (Argentina)
- **Modalidades**: Checkout Pro (hosted) con flujo rápido y mínima integración técnica; Payments API para cobro in-app manteniendo control del UX; links de pago para ventas asistidas.
- **Comisiones**: 3,19% a 5,99% + IVA según plan y plazo de acreditación; costos adicionales por cuotas financiadas y uso de links sin tienda.
- **Comprobantes**: integración con `payment notifications` y `payments/charges` para emitir comprobantes tipo "Recibo de señas" y exportar datos a facturación AFIP.
- **Privacidad y retención**: PANOS no almacena datos de tarjeta (queda en Mercado Pago); retención de datos transaccionales mínima necesaria (importe, payer_id, email) por 10 años según AFIP; anonimizar data al generar dashboards.

## Mensajería
| Criterio | WhatsApp Cloud API | Twilio |
| --- | --- | --- |
| Costos | Cobro por conversación, precios oficiales Meta | Intermediario con costos adicionales |
| Control | Configuración directa en Meta Business Manager | Consola unificada para múltiples canales |
| Implementación | Requiere verificación negocio y plantillas aprobadas | SDK uniforme, fallback SMS/email |
| Adecuación PANOS | Menos intermediarios, control directo de plantillas | Útil si se desea multicanal rápido |

### Detalle WhatsApp Business (Meta Cloud API)
- **Alta**: verificación de empresa en Meta Business Manager, número dedicado y asociación con proveedor de soluciones o uso directo de Cloud API.
- **Mensajes templated**: plantillas aprobadas previamente por Meta; categorías (utility, marketing) con costos diferentes. Requiere parámetros dinámicos validados.
- **Límites**: niveles de envío según calidad y volumen; inicio con 250 conversaciones/24h y escalado automático. Necesario mantener CSAT alto para evitar bloqueos.
- **Opt-in y anti-spam**: capturar consentimiento explícito (webform, checkbox) y almacenar timestamp/IP; mecanismos de opt-out inmediatos.
- **Privacidad y retención**: mensajes alojados en servidores de Meta; PANOS debe limitar logs a metadatos necesarios (estado, timestamps) y purgar contenido sensible tras 30 días salvo obligación contractual.

## Recomendación para MVP en Argentina
- **Front-end**: Next.js/React para combinar landing, chat y dashboard con SSR e internacionalización futura.
- **Backend/Agente**: FastAPI por rapidez para prototipos LLM y disponibilidad de librerías Python.
- **Vector DB**: Postgres con pgvector para simplificar operaciones iniciales y reportes integrados.
- **Orquestación**: LangChain para MVP, complementado con state machine propia para hitos críticos (pago, agenda).
- **Pagos**: Mercado Pago como método principal; Stripe habilitado para leads internacionales.
- **Mensajería**: WhatsApp Cloud API con plantillas aprobadas y fallback email gestionado desde el backend.

## Próximos pasos
- Validar capacidades del equipo para cada stack y cerrar decisiones tecnológicas.
- Diseñar arquitectura de referencia detallada (diagramas, flujos) para la especificación técnica.
- Estimar esfuerzos de integración y costos operativos asociados.
