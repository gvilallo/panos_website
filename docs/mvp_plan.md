# Plan MVP - 2 Semanas

## Objetivos
- Entregar flujo end-to-end: entrevista → mockups → seña → agenda.
- Validar propuesta de valor con prospectos reales del vertical inmobiliario.
- Preparar materiales y métricas para iterar hacia especificación técnica completa.

<<<<<<< ours
## Alcance (Historias Must)
- HU1 Captura inicial consentida.
- HU2 Entrevista adaptativa por vertical.
- HU3 Resumen dinámico del brief.
- HU4 Validación de presupuesto y tiempos.
- HU5 Generación automática de wireframes.
- HU7 Cálculo de inversión modular.
- HU8 Pago de seña seguro.
- HU9 Agenda automática de primera entrevista.
- HU10 Dashboard interno de leads (vista básica).
- HU11 Registro de consentimientos y revocación.
- HU12 Observabilidad del agente (MVP).

## Cronograma
### Semana 1
1. **Día 1-2**: Afinar textos legales, flujos de consentimiento (HU1, HU11).
2. **Día 2-3**: Implementar árbol de entrevista y resumen dinámico (HU2, HU3).
3. **Día 3-4**: Reglas de validación y alertas (HU4).
4. **Día 4-5**: Integración con generador de wireframes + plantillas (HU5).
5. **Día 5**: Sesión de revisión interna y pruebas con 2 usuarios piloto.

### Semana 2
1. **Día 6-7**: Motor de cálculos y propuesta modular (HU7).
2. **Día 7-8**: Checkout de seña y emisión de comprobante (HU8).
3. **Día 8-9**: Agenda automática e integraciones calendar/email/WhatsApp (HU9).
4. **Día 9-10**: Dashboard básico y observabilidad inicial (HU10, HU12).
5. **Día 10**: End-to-end testing, scripts de soporte, salida controlada a beta.
=======
## Alcance (Historias Must por Iteración)
### Iteración 1 – Semana 1
**HU1 - Captura inicial consentida**
- **Criterio Gherkin:**
  ```gherkin
  Dado que un prospecto accede a la landing
  Cuando acepta los Términos y Condiciones y la Política de Privacidad
  Entonces el sistema registra consentimiento con timestamp, IP, user-agent y canal
  Y habilita el inicio de la entrevista guiada
  ```
- **Definition of Done:** consentimientos versionados, textos legales aprobados por PANOS Legal, logs estructurados en datastore, pruebas de accesibilidad de formularios.
- **Dependencias:** textos legales vigentes, configuración de tracking (HU12).
- **Riesgos:** cambios regulatorios de última hora, rechazo del texto por legal.

**HU11 - Registro de consentimientos y revocación**
- **Criterio Gherkin:**
  ```gherkin
  Dado un prospecto con opt-in WhatsApp aceptado
  Cuando solicita revocar su consentimiento
  Entonces el sistema marca el opt-in como revocado con timestamp
  Y bloquea futuros envíos hasta nuevo opt-in válido
  ```
- **Definition of Done:** endpoints de registro y revocación probados, evidencia almacenada (ip, timestamp, texto), script manual de auditoría ejecutado.
- **Dependencias:** almacenamiento de consentimientos (HU1), políticas WhatsApp (docs/spec/whatsapp_politicas).
- **Riesgos:** inconsistencias entre base interna y Meta, pérdida de evidencia.

**HU2 - Entrevista adaptativa por vertical**
- **Criterio Gherkin:**
  ```gherkin
  Dado un prospecto inmobiliario en entrevista
  Cuando responde "manejo más de 100 propiedades"
  Entonces el agente despliega preguntas específicas sobre inventario masivo
  Y registra las respuestas en el brief estructurado
  ```
- **Definition of Done:** árbol de preguntas versionado, pruebas con datos dummy, fallback para preguntas no mapeadas, tracking de pasos completados.
- **Dependencias:** esquema de brief (docs/spec/brief_schema.md), contenido legal (HU1).
- **Riesgos:** cobertura incompleta de vertical, aumento de abandono si la entrevista se extiende demasiado.

**HU3 - Resumen dinámico del brief**
- **Criterio Gherkin:**
  ```gherkin
  Dado que el prospecto completa un bloque de entrevista
  Cuando el agente resume la información
  Entonces el panel lateral "Project Brief" se actualiza en tiempo real
  Y resalta campos pendientes o inconsistentes
  ```
- **Definition of Done:** sincronización estado chat-panel validada, persistencia en base de datos con versionado, pruebas de reconexión.
- **Dependencias:** HU2 para insumos, modelo de datos (docs/spec/datos_modelo.md).
- **Riesgos:** condiciones de carrera al persistir, pérdida de datos si se interrumpe la sesión.

**HU4 - Validación de presupuesto y tiempos**
- **Criterio Gherkin:**
  ```gherkin
  Dado un brief con presupuesto menor al mínimo definido
  Cuando el agente evalúa la información
  Entonces muestra un mensaje de ajuste con rango sugerido
  Y marca la historia como bloqueada hasta confirmar ajuste
  ```
- **Definition of Done:** reglas de negocio parametrizadas, mensajes localizados, pruebas de límites, logs de validación con contexto.
- **Dependencias:** HU3 para datos agregados, catálogos de reglas (docs/spec/seguridad_cumplimiento.md).
- **Riesgos:** falsos positivos que frustren al usuario, reglas desactualizadas.

**HU5 - Generación automática de wireframes**
- **Criterio Gherkin:**
  ```gherkin
  Dado un brief con objetivos y usuarios definidos
  Cuando el agente solicita wireframes iniciales
  Entonces se generan enlaces a mockups de Home, Dashboard y flujo de contratos
  Y se guardan referencias en el brief
  ```
- **Definition of Done:** integración con herramienta de wireframes mockeada, placeholders identificados, control de tiempo de respuesta, logs de generación.
- **Dependencias:** HU3 para contenido, acceso a plantilla base de UI.
- **Riesgos:** tiempos de espera altos, inconsistencias entre brief y mockup.

**Hito Iteración 1:** Brief interactivo listo, consentimientos auditables y mockups iniciales demostrables.

### Iteración 2 – Semana 2
**HU7 - Cálculo de inversión modular**
- **Criterio Gherkin:**
  ```gherkin
  Dado un brief con módulos Must y Should definidos
  Cuando el agente calcula la inversión
  Entonces muestra un desglose por módulo con rango mínimo y máximo
  Y registra el cálculo en el dashboard interno
  ```
- **Definition of Done:** fórmulas validadas con finanzas PANOS, exportable PDF/JSON, pruebas con escenarios altos/bajos.
- **Dependencias:** HU4 (datos validados), HU3 (brief completo).
- **Riesgos:** desalineación con costos reales, errores de redondeo.

**HU8 - Pago de seña seguro**
- **Criterio Gherkin:**
  ```gherkin
  Dado que un prospecto acepta la propuesta
  Cuando el sistema genera un link de pago de seña con Mercado Pago
  Entonces el prospecto completa el pago exitosamente
  Y recibe comprobante automático en email y WhatsApp
  ```
- **Definition of Done:** integración Checkout Pro en sandbox, webhook simulado funcionando, comprobante con campos fiscales mínimos, logs auditables.
- **Dependencias:** HU7 (monto), docs/spec/pagos_flujo.md.
- **Riesgos:** rechazos por configuración de cuenta, demoras en notificaciones.

**HU9 - Agenda automática de primera entrevista**
- **Criterio Gherkin:**
  ```gherkin
  Dado que una seña está confirmada
  Cuando el prospecto selecciona un horario disponible
  Entonces el sistema agenda la reunión en el calendario PANOS
  Y envía confirmación por email y WhatsApp
  ```
- **Definition of Done:** slots sincronizados con calendario compartido, recordatorios programados, pruebas con huso horario AR.
- **Dependencias:** HU8 (estado pagado), integración calendario.
- **Riesgos:** doble reserva de slots, fallos en notificaciones.

**HU10 - Dashboard interno de leads (vista básica)**
- **Criterio Gherkin:**
  ```gherkin
  Dado un analista PANOS autenticado
  Cuando accede al dashboard de leads
  Entonces visualiza estado de entrevista, pago y agenda por prospecto
  Y puede filtrar por fecha y vertical
  ```
- **Definition of Done:** roles y permisos aplicados, filtros funcionales, métricas clave visibles, pruebas de rendimiento con dataset simulado.
- **Dependencias:** HU3 (datos de brief), HU8/HU9 (estados), HU12 (logs/metrics).
- **Riesgos:** exposición de datos sensibles, inconsistencias en sincronización.

**HU12 - Observabilidad del agente (MVP)**
- **Criterio Gherkin:**
  ```gherkin
  Dado que ocurren eventos clave (consentimiento, pago, agenda)
  Cuando se consulta el panel de observabilidad
  Entonces se visualizan métricas y logs correlacionados por request_id
  Y existen alertas básicas ante fallos de pago o WhatsApp
  ```
- **Definition of Done:** dashboards mínimos configurados, alertas Slack/email activas, retención de logs 30 días, runbook actualizado.
- **Dependencias:** integraciones previas (HU8, HU9, HU10), docs/spec/nfr_mvp.md.
- **Riesgos:** falta de cobertura en alertas, ruido por falsos positivos.

**Hito Iteración 2:** Flujo pago → agenda → dashboard operativo probado y demo listo para salida controlada.

## Cronograma Iterativo y Hitos
- **Semana 1 (Iteración 1):**
  - Día 1-2: HU1, HU11 – Consentimientos y registro legal.
  - Día 2-3: HU2 – Entrevista adaptativa.
  - Día 3-4: HU3 – Resumen dinámico.
  - Día 4: HU4 – Validaciones de negocio.
  - Día 5: HU5 – Wireframes + revisión. _Hito: Brief interactivo y mockups listos._
- **Semana 2 (Iteración 2):**
  - Día 6: HU7 – Cálculo modular.
  - Día 7-8: HU8 – Pago de seña.
  - Día 8-9: HU9 – Agenda automática.
  - Día 9: HU10 – Dashboard leads.
  - Día 10: HU12 – Observabilidad + pruebas E2E. _Hito final: Demo E2E con pago y agenda, lista para prospectos piloto._
>>>>>>> theirs

## Flujo End-to-End
1. Usuario ingresa, acepta consentimientos y comienza entrevista.
2. Agente guía preguntas adaptadas, registra respuestas y genera resumen vivo.
3. Se ejecutan validaciones de presupuesto/tiempo y se sugieren ajustes.
4. Con el brief consolidado, se generan wireframes de home, dashboard y flujo de contratos.
5. Agente calcula inversión modular y presenta política de seña.
6. Usuario procede al checkout, paga la seña y recibe comprobante automático.
7. Sistema ofrece agenda; usuario elige slot, se envían confirmaciones y recordatorios.
8. Back-office recibe lead con estado, consentimientos y métricas en dashboard.

## Mockups mínimos requeridos
- Home pública de la inmobiliaria con búsqueda destacada.
- Dashboard administrativo con KPIs (unidades disponibles, reservas, vencimientos).
- Flujo de contrato paso a paso (wizard básico).
- Centro de notificaciones integradas (WhatsApp/email).

## Guion de demo
1. Presentación breve del caso inmobiliario y objetivo de la demo.
2. Navegación por landing y explicación de consentimientos.
3. Ejecución de entrevista mostrando adaptaciones de preguntas.
4. Visualización del resumen dinámico y validaciones.
5. Generación de mockups y ejemplo de ajuste rápido.
6. Presentación de cálculo de inversión y explicación de seña.
7. Simulación de pago exitoso y recepción de comprobante.
8. Selección de slot en agenda y notificaciones emitidas.
9. Recorrido por dashboard interno y métricas clave.
10. Cierre con próximos pasos y roadmap.

## Métricas de éxito
- ≥70% de prospectos completan la entrevista.
- ≥40% de entrevistas completadas terminan en pago de seña.
- Tiempo promedio desde inicio hasta agendamiento ≤ 25 minutos.
- Satisfacción post-demo ≥ 8/10.
- Tiempo de generación de mockups ≤ 90 segundos.
- Cero incidentes críticos en pagos o consentimientos durante beta.

## Próximos pasos
- Definir owners por entregable y checklists de QA detallados.
- Preparar documentación técnica preliminar (diagramas, APIs) para la especificación.
- Planificar iteración posterior con historias Should prioritarias.
