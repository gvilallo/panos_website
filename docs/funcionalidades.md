# Funcionalidades por Módulo

## Captura y Entrevista
- **Recopilación contextual multietapa**
  - Propósito: guiar al prospecto para clarificar su idea y objetivos.
  - Usuario: potencial cliente.
  - Precondiciones: acceso a landing y consentimiento inicial para uso de datos.
  - Valor: genera brief preliminar con información estructurada para ventas y delivery.
  - Prioridad (MoSCoW): Must.
- **Segmentación por vertical**
  - Propósito: adaptar preguntas y propuestas según industria (inmobiliaria, e-commerce, servicios).
  - Usuario: potencial cliente.
  - Precondiciones: selección o detección de vertical.
  - Valor: aumenta relevancia del diagnóstico y reduce ambigüedades.
  - Prioridad: Must.
- **Resumen dinámico del brief**
  - Propósito: mostrar en tiempo real los insights clave, must/should have.
  - Usuario: potencial cliente y equipo PANOS.
  - Precondiciones: preguntas completadas al menos parcialmente.
  - Valor: alinea expectativas antes de la propuesta.
  - Prioridad: Must.
- **Validaciones de negocio**
  - Propósito: alertar sobre presupuestos mínimos, tiempos o integraciones fuera de alcance.
  - Usuario: potencial cliente y orquestador PANOS.
  - Precondiciones: datos clave ingresados.
  - Valor: evita leads no calificados y redirige opciones.
  - Prioridad: Should.

## Generación de Mockups
- **Wireframes automáticos de páginas clave**
  - Propósito: entregar visual inicial de home, dashboard y flujos críticos.
  - Usuario: potencial cliente y equipo de diseño.
  - Precondiciones: brief básico definido.
  - Valor: acelera comprensión de la solución y habilita feedback temprano.
  - Prioridad: Must.
- **Iteración guiada durante la sesión**
  - Propósito: permitir ajustes rápidos de layout, textos o jerarquía.
  - Usuario: potencial cliente con apoyo del agente.
  - Precondiciones: wireframe generado.
  - Valor: crea sensación de co-creación y reduce revisiones posteriores.
  - Prioridad: Should.
- **Repositorio de mockups versionado**
  - Propósito: guardar variaciones y notas de decisiones.
  - Usuario: equipo PANOS.
  - Precondiciones: autenticación interna.
  - Valor: continuidad entre pre-venta y delivery.
  - Prioridad: Could.

## Pago y Onboarding
- **Estimación de inversión y desgloses**
  - Propósito: presentar rango de precios y componentes del proyecto.
  - Usuario: potencial cliente.
  - Precondiciones: requisitos clave completados y aprobados.
  - Valor: transparencia y transición fluida hacia la seña.
  - Prioridad: Must.
- **Cobro de seña integrado**
  - Propósito: procesar pago con medios locales (Mercado Pago) y alternativo (Stripe).
  - Usuario: potencial cliente.
  - Precondiciones: aceptación de términos y consentimiento de pago.
  - Valor: compromete al cliente y reserva cupo con el equipo PANOS.
  - Prioridad: Must.
- **Generación automática de comprobante**
  - Propósito: enviar recibo y condiciones de aplicación de la seña.
  - Usuario: potencial cliente y administración PANOS.
  - Precondiciones: pago exitoso.
  - Valor: respaldo legal y confianza.
  - Prioridad: Should.
- **Agenda de primera entrevista**
  - Propósito: coordinar disponibilidad y agendar en calendario con recordatorios.
  - Usuario: potencial cliente y socio PANOS asignado.
  - Precondiciones: seña confirmada.
  - Valor: reduce fricción post-venta y acelera kick-off.
  - Prioridad: Must.

## Back-office PANOS
- **Dashboard de leads y estado**
  - Propósito: visualizar progreso de entrevistas, mockups y pagos.
  - Usuario: socios PANOS y equipo de ventas.
  - Precondiciones: autenticación interna.
  - Valor: prioriza seguimiento y asignación de recursos.
  - Prioridad: Must.
- **Gestión de briefs y assets**
  - Propósito: almacenar respuestas estructuradas, mockups y acuerdos.
  - Usuario: socios PANOS y delivery.
  - Precondiciones: lead en etapa avanzada.
  - Valor: asegura continuidad entre pre-venta y ejecución.
  - Prioridad: Must.
- **Integración con herramientas existentes**
  - Propósito: sincronizar con CRM, sistemas de proyectos y contabilidad.
  - Usuario: equipo PANOS.
  - Precondiciones: APIs o conectores configurados.
  - Valor: elimina doble carga y errores.
  - Prioridad: Should.

## Seguridad y Cumplimiento
- **Consentimiento informado y T&Cs**
  - Propósito: registrar aceptación de políticas de privacidad y uso de datos.
  - Usuario: potencial cliente.
  - Precondiciones: formularios de consentimiento disponibles.
  - Valor: cumplimiento legal y confianza.
  - Prioridad: Must.
- **Gestión de datos sensibles**
  - Propósito: encriptar información personal y financiera.
  - Usuario: equipo PANOS y clientes.
  - Precondiciones: infraestructura segura.
  - Valor: reduce riesgo de brechas y sanciones.
  - Prioridad: Must.
- **Retención y eliminación programada**
  - Propósito: establecer plazos y procesos automáticos para borrar datos.
  - Usuario: equipo PANOS.
  - Precondiciones: políticas definidas.
  - Valor: evita sobre-retención y responde a requerimientos regulatorios.
  - Prioridad: Should.

## Observabilidad
- **Logging de conversaciones y acciones**
  - Propósito: auditar decisiones del agente y detectar fallas.
  - Usuario: equipo técnico PANOS.
  - Precondiciones: almacenamiento seguro.
  - Valor: soporte para mejora continua y cumplimiento.
  - Prioridad: Must.
- **Métricas de conversión**
  - Propósito: medir tasas de completitud, pagos y agendamientos.
  - Usuario: socios PANOS.
  - Precondiciones: eventos instrumentados.
  - Valor: optimiza embudo comercial.
  - Prioridad: Must.
- **Feedback loop post-entrevista**
  - Propósito: recolectar NPS y comentarios.
  - Usuario: potencial cliente.
  - Precondiciones: entrevista agendada o completada.
  - Valor: mejora iterativa del agente.
  - Prioridad: Should.

## Top 10 Ambigüedades
1. Nivel de personalización requerida por vertical más allá de inmobiliaria.
2. Alcance exacto de integraciones con CRMs externos.
3. Capacidad del agente para interpretar documentos existentes del cliente.
4. Detalle de funcionalidades del asistente de contratos en el MVP.
5. Requisitos legales de firma electrónica por país de operación.
6. Límites de responsabilidad de PANOS frente a recomendaciones del agente.
7. Políticas de devolución de la seña y excepciones.
8. Nivel de automatización esperado en generación de mockups (herramienta exacta).
9. Disponibilidad y volumen de contenidos que el cliente puede subir.
10. Reglas de retención de datos diferenciadas por jurisdicción.

## Próximos pasos
- Definir especificaciones funcionales detalladas para cada módulo.
- Resolver ambigüedades priorizadas con stakeholders.
- Mapear dependencias técnicas para implementación.
