# Wireframes mínimos del MVP PANOS

## 1. Páginas y pantallas

### Home / Landing
- **Objetivo**: presentar PANOS, explicar el flujo asistido y captar leads para iniciar la entrevista.
- **Bloques de contenido**: hero con propuesta de valor, beneficios, testimonio breve, CTA principal, FAQs legales (T&Cs/Privacidad), footer con datos de contacto.
- **Acciones clave / CTAs**: "Iniciar entrevista", "Ver cómo funciona", enlace a T&Cs y Política de Privacidad.
- **Métricas a observar**: tasa de clic en CTA principal, scroll depth, rebote, aceptación T&Cs.
- **Placeholders permitidos**: imágenes ilustrativas, testimonios ficticios marcados como demo.

### Chat del agente (entrevista)
- **Objetivo**: conducir la entrevista guiada y recopilar datos para el brief.
- **Bloques de contenido**: panel de chat, timeline de pasos, input de usuario con sugerencias, aviso de privacidad.
- **Acciones clave / CTAs**: enviar respuesta, guardar y continuar luego, solicitar ayuda humana.
- **Métricas a observar**: mensajes por sesión, tasa de abandono por paso, confirmaciones de privacidad.
- **Placeholders permitidos**: avatar del agente, textos de ejemplo en burbujas.

### Panel lateral “Project Brief”
- **Objetivo**: mostrar progreso y resumen estructurado de la entrevista.
- **Bloques de contenido**: tabs por sección (Datos, Alcance, Riesgos, Legales), indicadores de completitud, botón "Descargar".
- **Acciones clave / CTAs**: expandir sección, editar respuesta, descargar resumen.
- **Métricas a observar**: secciones completadas, clic en descargar, edición de respuestas.
- **Placeholders permitidos**: valores de demo resaltados como "Lorem".

### Página “Mockups iniciales”
- **Objetivo**: presentar wireframes generados y recoger feedback rápido.
- **Bloques de contenido**: galería de mockups, notas del agente, formulario de comentarios, checklist de cambios.
- **Acciones clave / CTAs**: aprobar mockup, solicitar ajuste, descargar PDF.
- **Métricas a observar**: tasa de aprobación, comentarios enviados, descargas.
- **Placeholders permitidos**: imágenes wireframe low-fidelity, textos lorem etiquetados.

### Pago de seña (Checkout Pro / Link)
- **Objetivo**: redirigir a Mercado Pago y capturar la transacción de seña.
- **Bloques de contenido**: resumen del monto, beneficios de la seña, enlaces legales, botón para abrir link.
- **Acciones clave / CTAs**: "Pagar seña", "Ver condiciones de devolución", contacto soporte.
- **Métricas a observar**: clic en pagar, abandono, errores, conversiones confirmadas.
- **Placeholders permitidos**: logos de medios de pago genéricos, número de comprobante ficticio.

### Confirmación + Agenda
- **Objetivo**: confirmar pago exitoso y permitir agendar la primera reunión.
- **Bloques de contenido**: mensaje de éxito, comprobante, selector de franja horaria, CTA calendario, datos de contacto.
- **Acciones clave / CTAs**: elegir horario, descargar comprobante, agregar recordatorio.
- **Métricas a observar**: horarios seleccionados, descargas de comprobante, clic en recordatorios.
- **Placeholders permitidos**: número de comprobante mock, horarios de ejemplo.

### Dashboard interno PANOS (back-office)
- **Objetivo**: permitir al equipo PANOS ver leads, estado del brief y acciones pendientes.
- **Bloques de contenido**: widgets de conversiones, tabla de leads, filtros, panel de tareas.
- **Acciones clave / CTAs**: abrir brief, marcar tarea como realizada, iniciar contacto manual.
- **Métricas a observar**: leads procesados, tiempo hasta contacto, conversiones.
- **Placeholders permitidos**: datos dummy con etiqueta "Demo".

### Estado / Historial (logs básicos)
- **Objetivo**: ofrecer visibilidad de eventos clave (pagos, mensajes, cambios de brief).
- **Bloques de contenido**: línea de tiempo, filtros por evento, detalles expandibles, exportar CSV.
- **Acciones clave / CTAs**: filtrar por tipo, descargar reporte, marcar como revisado.
- **Métricas a observar**: consultas por período, exportaciones, eventos con error.
- **Placeholders permitidos**: eventos de muestra con tags "Mock".

## 2. Componentes reutilizables (UI kit mínimo)
- **Header / Brand**: logo PANOS, navegación principal, link a soporte.
- **Card**: contenedor con título, descripción y CTA secundario.
- **Lista con íconos**: bullets con íconos para destacar beneficios o pasos.
- **Tabs**: navegación por secciones (ej. panel brief).
- **Stepper**: indicar progreso de entrevista y pagos.
- **Toasts / Alerts**: notificaciones de éxito, error o info con autocierre y accesibles.
- **Modal de confirmación**: confirmar acciones críticas (pago, envío de datos).
- **Tabla simple**: listados de leads, eventos y tareas con sorting básico.
- **Pagination**: control para navegar listados extensos.

## 3. Notas de accesibilidad
- Garantizar contraste AA mínimo (WCAG 2.1) en texto y elementos interactivos.
- Proveer estado de foco visible para inputs, botones y enlaces.
- Permitir navegación completa con teclado (tab order lógico, skip links).
- Incluir labels y descripciones para formularios, iconografía con texto alternativo.

## 4. Copys guía (microcopy)
- **Inicio**: "Descubrí cómo PANOS transforma tu idea en proyecto listo para arrancar." CTA: "Iniciar entrevista".
- **Entrevista**: "Contanos sobre tu negocio para armar el brief inicial." Ayuda contextual: "Podés guardar y continuar más tarde."
- **Pago**: "Reservá tu lugar con una seña 100% aplicable al proyecto final." Mensaje legal: "Al continuar aceptás T&Cs y Política de Privacidad."
- **Confirmación**: "¡Listo! Recibimos tu seña. Revisá tu comprobante y agendá la primera reunión."
- **Agenda**: "Elegí la franja horaria que mejor se adapte a tu disponibilidad." Mensaje de soporte: "¿Necesitás ayuda? Escribinos a soporte@panos.com."

## 5. Definition of Ready (DoR) de los wireframes
- Cada pantalla documenta objetivo y usuarios principales.
- CTAs principales y secundarios definidos con estados (enabled/disabled).
- Datos de ejemplo coherentes con el caso inmobiliaria y etiquetados como demo.
- Placeholders identificados y anotados para reemplazo en prototipo.
- Métricas a medir listadas con origen de logging o analytics.
- Referencias a copys guía y componentes reutilizables asignados.

## 6. Anexo: mapa de navegación
- **Home / Landing** → iniciar entrevista / ver cómo funciona → **Chat del agente**.
- Chat actualiza **Panel lateral “Project Brief”** en paralelo.
- Tras completar entrevista → **Página “Mockups iniciales”** → feedback → CTA "Avanzar a seña".
- "Avanzar a seña" → **Pago de seña** (Checkout Pro / Link) → redirección éxito.
- Éxito → **Confirmación + Agenda** → selección de turno → integración calendario.
- Equipo PANOS accede a **Dashboard interno** → desde allí consulta **Estado / Historial**.
- Navegación secundaria desde dashboard hacia mockups y brief descargable.

## Próximos pasos hacia prototipado
- Priorizar fidelidad (low vs mid) por pantalla y definir herramientas (Figma, FigJam).
- Crear componentes en librería compartida y asegurar consistencia visual.
- Validar copys con equipo legal/marketing antes de diseño hi-fi.
- Preparar escenarios de prueba para accesibilidad básica (teclado, lector pantalla).
