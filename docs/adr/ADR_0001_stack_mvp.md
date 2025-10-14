# ADR 0001: Stack tecnológico del MVP PANOS

- **Fecha**: 2024-04-07
- **Estado**: Propuesto

## Contexto
PANOS debe lanzar un MVP operativo en Argentina que permita a un prospecto pasar de una entrevista guiada por IA a la reserva pagada y la agenda de la primera reunión con el equipo. El stack debe equilibrar velocidad de entrega en dos semanas, cumplimiento local (AFIP, Ley 25.326, opt-in WhatsApp), integraciones nativas con Mercado Pago y WhatsApp Cloud API, y la capacidad de iterar sobre flujos conversacionales y mockups sin fricción.

## Opciones evaluadas
- **Front-end**
  - *Next.js (App Router) + React*: SSR/ISR nativo, buenas prácticas de routing, soporte integrado para APIs ligeras y edge functions.
  - *Vite + React*: build rápido, simplicidad, requiere configurar routing, SSR y despliegue manual.
- **Backend/Agente**
  - *FastAPI (Python)*: performance aceptable, typing, ecosistema de librerías LLM (LangChain, Pydantic), compatibilidad con pipelines de datos.
  - *NestJS (Node.js)*: estructura opinionada, TypeScript end-to-end, buenas prácticas integradas.
- **Base de datos / Vector Store**
  - *Postgres 15 + pgvector*: datos transaccionales y embeddings en una sola instancia administrada.
  - *Qdrant gestionado*: vector store dedicado, requiere sincronización adicional con la base relacional.
- **Orquestación de prompts/funciones**
  - *Funciones serverless ligeras + colas simples (Celery/RQ)*.
  - *Frameworks especializados (Temporal, Prefect)*.
- **Pagos Argentina**
  - *Mercado Pago Checkout Pro / Links de pago*: redirección con UI de MP, menor alcance PCI.
  - *Mercado Pago Payments API*: integración directa, UX embebida, mayor responsabilidad de cumplimiento.
  - *Stripe Checkout*: alternativa internacional para clientes fuera de AR.
- **Mensajería WhatsApp**
  - *Meta WhatsApp Cloud API*: acceso directo, plantillas oficiales, control de opt-in y límites.
  - *Twilio WhatsApp*: capa intermedia, costos adicionales, dependencia de disponibilidad de números locales.

## Decisión
Adoptar la combinación: **Next.js (App Router) + React** en el front, **FastAPI** como backend/orquestador del agente, **Postgres 15 con extensión pgvector** como store unificado, **server functions + cola ligera (Celery sobre Redis administrado)** para orquestación, **Mercado Pago Checkout Pro con fallback a links de pago y plan de extensión a Payments API**, **Stripe Checkout** solo para escenarios exportables, y **Meta WhatsApp Cloud API** como canal primario de mensajería.

## Justificación
- **Time-to-market**: Next.js y FastAPI permiten prototipos rápidos con soporte sólido para SSR y APIs REST, lo que reduce fricción en el handoff de entrevistas a mockups y back-office.
- **Ecosistema LLM**: Python concentra librerías maduras para orquestar prompts, embeddings y manejo de memoria conversacional; pgvector evita duplicidad de almacenes.
- **Cumplimiento argentino**: Checkout Pro minimiza alcance PCI y ofrece comprobantes válidos para AFIP. La Cloud API de Meta habilita trazabilidad, opt-in explícito y control de plantillas requerido por la política anti-spam.
- **Operación liviana**: colas simples cubren necesidades de orquestación sin introducir frameworks pesados; se pueden operar en el mismo hosting (Render/Fly/Heroku) y escalar progresivamente.
- **Escalabilidad futura**: mantener Stripe y Qdrant como opciones secundarias facilita expansión regional sin rehacer integraciones clave.

## Consecuencias
- **Positivas**
  - Un único lenguaje (TypeScript en front, Python en back) balanceado con un motor de datos centralizado simplifica la curva del equipo.
  - Menor superficie de auditoría PCI al delegar cobros a Checkout Pro.
  - Control directo de métricas y logs gracias a Postgres + pgvector y colas propias.
- **Negativas / Deuda técnica**
  - Dependencia de servicios de Meta para mensajería y de Mercado Pago para cobros; se requiere plan de contingencia ante caídas.
  - Celery sobre Redis agrega componente adicional a administrar; futuro escalado podría requerir migración a orquestadores más robustos.
  - pgvector puede no escalar óptimamente si el corpus crece mucho; podría demandar migración a Qdrant.

## Alternativas descartadas
- **Vite + React**: descartado por carecer de SSR y routing nativo, lo que dificulta SEO inicial y genera overhead para proteger rutas del back-office.
- **NestJS**: ofrecería TypeScript end-to-end pero limitaría acceso directo a tooling Python para agentes y embeddings, clave en esta etapa.
- **Temporal/Prefect**: exceso de complejidad para un MVP de dos semanas; se pospone hasta que se evidencie necesidad de workflows complejos.
- **Mercado Pago Payments API como primera opción**: implica alojar tarjetas y mayor alcance PCI; se adopta solo cuando se requiera UX embebida.
- **Twilio WhatsApp**: costos y dependencia adicional, además de provisión limitada de números para Argentina.

## Impacto en el MVP
- Habilita en dos semanas: flujo conversacional completo (Next.js + FastAPI), generación de resúmenes y mockups iniciales usando librerías Python, cobro de seña mediante Checkout Pro con comprobante automático, registro de interacciones y consentimientos en Postgres, disparo de plantillas WhatsApp aprobadas, y tablero interno básico apoyado en SSR.
- Define base reutilizable para los siguientes ADRs y la fase de especificación técnica detallada.

---

### Próximos ADRs propuestos
- **ADR 0002** – Pagos (profundizar en modalidades Mercado Pago, conciliación, fallback Stripe).
- **ADR 0003** – WhatsApp (gestión de plantillas, opt-in, límites y monitoreo de reputación).
- **ADR 0004** – Vector DB / RAG (evolución desde pgvector hacia servicios dedicados y gobernanza de embeddings).
- **ADR 0005** – Hosting e infraestructura (proveedor, redes, CI/CD, observabilidad).
