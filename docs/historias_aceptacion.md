# Historias de Usuario y Criterios de Aceptación

## Historias Must

### HU1 - Captura inicial consentida (Must, Quick Win)
- Como PyME quiero iniciar la entrevista con un consentimiento claro para que el agente use mis datos.
- Dependencias: ninguna.
- Criterios de aceptación (Gherkin):
  - ```
    Dado que un visitante accede a la landing
    Cuando acepta la política de privacidad y los T&Cs
    Entonces se habilita el inicio de la entrevista guiada
    Y se registra el timestamp y la versión de los documentos aceptados
    ```
- Definition of Done:
  - Textos legales aprobados por compliance.
  - Registro persistente y exportable.
  - Tests de flujo feliz y rechazo.

### HU2 - Entrevista adaptativa por vertical (Must)
- Como PyME quiero que las preguntas se adapten a mi industria para sentir relevancia.
- Dependencias: HU1.
- Criterios de aceptación:
  - ```
    Dado que el prospecto selecciona la vertical inmobiliaria
    Cuando responde la primera tanda de preguntas
    Entonces el agente presenta preguntas específicas de inventario y contratos
    Y omite preguntas no relevantes de otras verticales
    ```
- Definition of Done:
  - Árbol de decisión documentado.
  - Pruebas unitarias de branching.
  - Validación con socio PANOS.

### HU3 - Resumen dinámico del brief (Must, Quick Win)
- Como prospecto quiero ver un resumen vivo de mis respuestas para confirmar alineación.
- Dependencias: HU2.
- Criterios de aceptación:
  - ```
    Dado que el prospecto completó al menos el 50% de la entrevista
    Cuando solicita ver el resumen
    Entonces el sistema muestra objetivos, must/should y riesgos detectados
    Y destaca campos aún incompletos
    ```
- Definition of Done:
  - UI validada con usuarios internos.
  - Persistencia del resumen en back-office.
  - Métrica de visualización instrumentada.

### HU4 - Validación de presupuesto y tiempos (Must)
- Como socio PANOS quiero recibir alertas cuando el prospecto ingresa datos fuera de rango.
- Dependencias: HU2.
- Criterios de aceptación:
  - ```
    Dado que el prospecto indica un presupuesto menor al mínimo permitido
    Cuando finaliza la entrevista
    Entonces el agente muestra un mensaje de ajuste necesario
    Y notifica al back-office con el estado "Revisar"
    ```
- Definition of Done:
  - Reglas configurables.
  - Notificación probada en dashboard.
  - Casos límite documentados.

### HU5 - Generación automática de wireframes (Must)
- Como PyME quiero visualizar mockups iniciales para validar la solución.
- Dependencias: HU3.
- Criterios de aceptación:
  - ```
    Dado que el resumen contiene secciones definidas
    Cuando el prospecto solicita mockups
    Entonces el agente genera al menos tres vistas (home, dashboard, flujo clave)
    Y permite descargar o compartir un enlace
    ```
- Definition of Done:
  - Integración con herramienta de generación probada.
  - Plantillas base aprobadas por diseño.
  - Logs de generación almacenados.

### HU6 - Iteración rápida sobre mockups (Should)
- Como PyME quiero solicitar ajustes simples en la misma sesión.
- Dependencias: HU5.
- Criterios de aceptación:
  - ```
    Dado que un mockup fue generado
    Cuando el prospecto pide cambiar un texto o bloque
    Entonces el agente presenta una versión actualizada en menos de 60 segundos
    Y registra el historial de cambios
    ```
- Definition of Done:
  - Parámetros de ajuste definidos.
  - Límite de iteraciones configurado.
  - Evidencia de performance.

### HU7 - Cálculo de inversión modular (Must)
- Como PyME quiero un estimado con desglose para decidir la seña.
- Dependencias: HU4, HU5.
- Criterios de aceptación:
  - ```
    Dado que el prospecto completó la entrevista y validaciones
    Cuando el agente presenta la propuesta
    Entonces muestra rango de inversión por módulo y tiempos tentativos
    Y explica qué incluye la seña
    ```
- Definition of Done:
  - Fórmulas revisadas por finanzas.
  - UI con disclaimers legales.
  - Pruebas de cálculo con casos tipo.

### HU8 - Pago de seña seguro (Must)
- Como PyME quiero pagar la seña con opciones locales y recibir comprobante.
- Dependencias: HU7.
- Criterios de aceptación:
  - ```
    Escenario: Pago exitoso con Mercado Pago Checkout Pro
      Dado que el prospecto acepta el resumen y la propuesta
      Y el monto de la seña está parametrizado según el módulo seleccionado
      Cuando inicia el checkout y elige Mercado Pago
      Entonces se redirige al flujo de pago seguro
      Y al confirmar la operación el sistema registra el payment_id del proveedor
      Y actualiza el estado del lead a "Seña pagada"
    ```
  - ```
    Escenario: Envío de comprobante y correo de confirmación
      Dado que el pago de seña fue confirmado por el proveedor
      Cuando el webhook de confirmación es recibido
      Entonces el sistema genera el comprobante fiscal con el monto, fecha y CUIT
      Y envía el comprobante por email al prospecto
      Y deja disponible la descarga en el panel back-office
    ```
- Definition of Done:
  - Integraciones sandbox certificadas.
  - Logs de transacción y auditoría almacenados de forma segura con retención definida.
  - Reconciliación contable definida.
  - Pruebas de integración simuladas con Mercado Pago y Stripe documentadas.

### HU9 - Agenda automática de primera entrevista (Must, Quick Win)
- Como PyME quiero agendar la reunión inicial inmediatamente después del pago.
- Dependencias: HU8.
- Criterios de aceptación:
  - ```
    Dado que el pago fue confirmado
    Cuando el prospecto elige un horario
    Entonces el sistema bloquea el slot en el calendario PANOS
    Y envía recordatorios por email y WhatsApp
    ```
- Definition of Done:
  - Sincronización bidireccional con calendario.
  - Plantillas de recordatorio aprobadas.
  - Logs de envío verificables.

### HU10 - Dashboard interno de leads (Must)
- Como socio PANOS quiero visualizar el estado de cada lead para priorizar acciones.
- Dependencias: HU3, HU4, HU8, HU9.
- Criterios de aceptación:
  - ```
    Dado que existen leads en distintas etapas
    Cuando un socio accede al dashboard
    Entonces ve status (Entrevista, Mockups, Propuesta, Pago, Agenda)
    Y puede filtrar por prioridad y vertical
    ```
- Definition of Done:
  - Roles y permisos implementados.
  - Datos actualizados en tiempo casi real.
  - Documentación de uso entregada al equipo.

### HU11 - Registro de consentimientos y revocación (Must)
- Como especialista de soporte quiero consultar y gestionar consentimientos otorgados.
- Dependencias: HU1.
- Criterios de aceptación:
  - ```
    Dado que un prospecto solicita revocar el consentimiento de mensajes
    Cuando soporte accede al registro
    Entonces puede marcar la revocación
    Y el sistema detiene envíos posteriores automáticamente
    ```
- Definition of Done:
  - Auditoría trazable.
  - Procesos de baja replicados en WhatsApp y email.
  - Documentación legal validada.

### HU12 - Observabilidad del agente (Must)
- Como equipo técnico quiero monitorear logs y métricas para mejorar el agente.
- Dependencias: HU2, HU5, HU8.
- Criterios de aceptación:
  - ```
    Dado que una sesión de entrevista se completa
    Cuando se revisa el panel de observabilidad
    Entonces se visualizan métricas de pasos, conversiones y tiempos
    Y se puede exportar un reporte mensual
    ```
- Definition of Done:
  - Instrumentación con alertas críticas.
  - Reportes automatizados.
  - Capacitación interna realizada.

## Historias Should

### HU13 - Iteración guiada con sugerencias del agente (Should)
- Como PyME quiero recibir propuestas de mejora automáticas basadas en mis respuestas.
- Dependencias: HU3, HU5.
- Criterios de aceptación:
  - ```
    Dado que el prospecto revisa el resumen
    Cuando solicita sugerencias
    Entonces el agente propone mejoras priorizadas
    Y permite aceptarlas o descartarlas con un clic
    ```
- Definition of Done:
  - Biblioteca de sugerencias por vertical.
  - Métrica de aceptación implementada.
  - Revisión editorial completada.

### HU14 - Biblioteca de plantillas de contratos (Should)
- Como socio PANOS quiero seleccionar plantillas validadas para la propuesta final.
- Dependencias: HU7.
- Criterios de aceptación:
  - ```
    Dado que se prepara el paquete de onboarding
    Cuando el socio elige una plantilla
    Entonces el sistema ofrece las variantes legales disponibles
    Y adjunta la seleccionada al resumen ejecutivo
    ```
- Definition of Done:
  - Plantillas revisadas por legal.
  - Versionado documentado.
  - Control de acceso implementado.

### HU15 - Feedback post-entrevista automatizado (Should, Quick Win)
- Como PyME quiero calificar la experiencia para mejorar el servicio.
- Dependencias: HU9.
- Criterios de aceptación:
  - ```
    Dado que la primera entrevista fue agendada
    Cuando pasan 24 horas
    Entonces el sistema envía encuesta NPS
    Y almacena la respuesta vinculada al lead
    ```
- Definition of Done:
  - Plantillas aprobadas por marketing.
  - Automatización con tasa de envío monitoreada.
  - Reporte semanal configurado.

## Próximos pasos
- Priorizar historias Must para la planificación técnica detallada.
- Desglosar criterios en tareas técnicas y de diseño.
- Preparar matrices de dependencia para la especificación técnica.
