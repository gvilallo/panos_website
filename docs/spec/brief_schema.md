# Esquema del Project Brief

## 1. Identificación del prospecto
- **Razón social / Nombre**
  - Tipo: texto (string)
  - Obligatorio: Requerido
  - Validaciones: mínimo 2 caracteres, sin caracteres especiales prohibidos; debe coincidir con documentación tributaria si aplica.
- **Contacto principal (nombre, email, WhatsApp)**
  - Tipo: objeto `{ nombre: string, email: string, whatsapp: string }`
  - Obligatorio: Requerido
  - Validaciones: nombre ≥ 2 caracteres; email con formato RFC 5322; WhatsApp en formato E.164 y validado contra lista de países soportados.
- **País / Provincia**
  - Tipo: enum (`AR`, `UY`, `CL`, ...); provincia según catálogo por país.
  - Obligatorio: Requerido
  - Validaciones: valores deben existir en catálogo activo; para Argentina provincia obligatoria.

## 2. Objetivos y alcance
- **Objetivo principal**
  - Tipo: texto
  - Obligatorio: Requerido
  - Validaciones: 20–500 caracteres; debe describir un resultado de negocio medible.
- **Alcance v1 (Must/Should/Could)**
  - Tipo: lista de objetos `{ prioridad: enum, descripción: string }`
  - Obligatorio: Requerido
  - Validaciones: al menos un Must y un Should; prioridades válidas `Must`, `Should`, `Could`.
- **KPIs de éxito**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: mínimo dos KPIs; cada KPI ≤ 120 caracteres y debe incluir métrica cuantificable.

## 3. Usuarios y casos de uso
- **Perfiles**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: mínimo dos perfiles; utilizar taxonomía estándar PANOS.
- **Principales tareas por perfil**
  - Tipo: lista de objetos `{ perfil: string, tareas: string[] }`
  - Obligatorio: Requerido
  - Validaciones: cada perfil listado debe tener al menos dos tareas; tareas ≤ 200 caracteres.

## 4. Datos e integraciones
- **Fuentes de datos existentes**
  - Tipo: lista de strings
  - Obligatorio: Opcional
  - Validaciones: si se especifican, indicar propietario y formato (CSV, API, etc.).
- **Integraciones requeridas**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: debe incluir categoría (pagos, mensajería, firma); validar disponibilidad regional (p. ej., Mercado Pago AR).
- **Disponibilidad de datos**
  - Tipo: objeto `{ disponible: bool, formato: enum, volumen_estimado: string }`
  - Obligatorio: Requerido
  - Validaciones: si `disponible = true`, el formato debe ser uno permitido; volumen expresado en cantidad mensual estimada.

## 5. Reglas de negocio (por vertical)
- **Inmobiliaria**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: cada regla debe indicar estado afectado y condición de activación; mínimo tres reglas (propiedades, contratos, cobranza).

## 6. Mockups solicitados
- **Páginas/pantallas**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: mínimo tres pantallas, incluyendo landing, panel y flujo crítico.
- **Notas de contenido y estilo**
  - Tipo: texto
  - Obligatorio: Opcional
  - Validaciones: ≤ 500 caracteres; evitar datos personales sensibles.

## 7. Cronograma y presupuesto
- **Plazo objetivo**
  - Tipo: fecha o semana ISO 8601
  - Obligatorio: Requerido
  - Validaciones: fecha ≥ fecha actual + 14 días; formato `YYYY-MM-DD` o `YYYY-Www`.
- **Rango de inversión**
  - Tipo: número (ARS o USD)
  - Obligatorio: Requerido
  - Validaciones: monto mínimo acorde a tarifas PANOS; indicar moneda.
- **Restricciones**
  - Tipo: texto
  - Obligatorio: Opcional
  - Validaciones: ≤ 300 caracteres; clasificar en operativas, legales o tecnológicas.

## 8. Riesgos y suposiciones
- **Supuestos clave**
  - Tipo: lista de strings
  - Obligatorio: Requerido
  - Validaciones: mínimo tres supuestos; cada uno con responsable de verificación.
- **Riesgos**
  - Tipo: tabla de objetos `{ riesgo: string, impacto: enum, probabilidad: enum, mitigación: string }`
  - Obligatorio: Requerido
  - Validaciones: impacto/probabilidad ∈ {Bajo, Medio, Alto}; mitigación ≤ 200 caracteres.

## 9. Legales y consentimiento
- **Aceptación de T&Cs y Política de Privacidad**
  - Tipo: booleano
  - Obligatorio: Requerido
  - Validaciones: debe registrarse timestamp y versión de documentos.
- **Opt-in WhatsApp (fecha, fuente, evidencia)**
  - Tipo: objeto `{ fecha: date, fuente: enum, evidencia: string }`
  - Obligatorio: Requerido
  - Validaciones: fecha en formato ISO; fuente ∈ {Form web, Email, Evento, Otro}; evidencia URL o referencia almacenada en drive seguro.
- **Retención de datos (meses)**
  - Tipo: número entero
  - Obligatorio: Requerido
  - Validaciones: rango permitido 6–36 meses; aplicar políticas LGPD/ARPD si corresponde.

## 10. Seña y próxima acción
- **Monto de seña**
  - Tipo: número (ARS)
  - Obligatorio: Requerido
  - Validaciones: monto ≥ mínimo definido por PANOS; hasta dos decimales.
- **Medio de pago (Checkout Pro / Link)**
  - Tipo: enum
  - Obligatorio: Requerido
  - Validaciones: valores permitidos `Checkout Pro`, `Link de pago`; si `Link de pago`, validar generación previa al envío.
- **Preferencia de agenda (franja horaria)**
  - Tipo: texto
  - Obligatorio: Requerido
  - Validaciones: debe mapear a slots disponibles (mañana, tarde, after-hours) y especificar zona horaria.

## Tabla resumen de validaciones

| Campo | Regla de validación | Mensaje de error |
| --- | --- | --- |
| Razón social / Nombre | ≥ 2 caracteres y caracteres permitidos | "Ingrese un nombre válido (mínimo 2 caracteres)." |
| Contacto principal.email | Formato RFC 5322 | "Correo inválido. Revise el formato nombre@dominio." |
| Contacto principal.whatsapp | Formato E.164 y país soportado | "Número de WhatsApp no válido o no soportado." |
| País / Provincia | Debe existir en catálogo activo | "Seleccione un país y provincia válidos." |
| Objetivo principal | 20–500 caracteres | "Describa el objetivo en 20 a 500 caracteres." |
| Alcance v1 | ≥1 Must y ≥1 Should | "Defina al menos un Must y un Should." |
| KPIs de éxito | ≥2 métricas cuantificables | "Agregue al menos dos KPIs medibles." |
| Perfiles | ≥2 perfiles de taxonomía PANOS | "Incluya al menos dos perfiles reconocidos." |
| Tareas por perfil | ≥2 tareas por perfil | "Cada perfil debe tener dos tareas mínimas." |
| Integraciones requeridas | Categoría y disponibilidad regional | "Indique integraciones válidas para su país." |
| Disponibilidad de datos | Formatos permitidos y volumen | "Complete formato y volumen estimado." |
| Reglas de negocio | ≥3 reglas con estado y condición | "Defina reglas clave para la operación." |
| Páginas/pantallas | ≥3 entradas | "Seleccione al menos tres pantallas para mockups." |
| Plazo objetivo | Fecha futura ≥ 14 días | "El plazo debe ser al menos dentro de 14 días." |
| Rango de inversión | ≥ mínimo PANOS | "El monto debe superar el mínimo requerido." |
| Supuestos clave | ≥3 supuestos | "Liste al menos tres supuestos." |
| Riesgos | Impacto/probabilidad válidos | "Seleccione impacto y probabilidad válidos." |
| Aceptación T&Cs | Booleano true con timestamp | "Debe aceptar Términos y Privacidad." |
| Opt-in WhatsApp | Fecha ISO y fuente válida | "Registre fecha, fuente y evidencia del opt-in." |
| Retención de datos | Entre 6 y 36 meses | "Defina una retención entre 6 y 36 meses." |
| Monto de seña | ≥ mínimo PANOS | "La seña debe alcanzar el mínimo establecido." |
| Medio de pago | Enum permitido | "Seleccione un medio de pago válido." |
| Preferencia de agenda | Slot válido y zona horaria | "Seleccione una franja disponible." |

## Definition of Ready del brief
- Todas las secciones 1–10 completadas y validadas sin errores.
- KPIs, alcance y reglas de negocio revisadas por un consultor PANOS.
- Integraciones requeridas confirmadas con disponibilidad regional.
- Opt-in de WhatsApp respaldado con evidencia almacenada.
- Plazo objetivo y rango de inversión alineados con el equipo comercial.
- Riesgos con responsables asignados y mitigaciones preliminares.

## Ejemplo rellenado (vertical: inmobiliaria)
- **Razón social / Nombre:** Inmobiliaria Horizonte SRL
- **Contacto principal:** `{ nombre: "Mariana López", email: "mariana.lopez@horizonte.com", whatsapp: "+5491160012233" }`
- **País / Provincia:** `AR / Buenos Aires`
- **Objetivo principal:** "Lanzar una plataforma que centralice el inventario de propiedades y automatice la gestión de reservas con seguimiento por WhatsApp."
- **Alcance v1:**
  - `Must`: "Dashboard de propiedades con estado de publicación"
  - `Must`: "Automatización de recordatorios de cobranza vía WhatsApp"
  - `Should`: "Asistente de contratos con plantillas editables"
  - `Could`: "Portal de propietarios para cargar documentación"
- **KPIs de éxito:** `Tiempo promedio de reserva < 48h`, `Tasa de conversión de leads a visitas 20%`, `Cobranza puntual 90%`
- **Perfiles:** `Administrador`, `Agente de ventas`, `Propietario`
- **Principales tareas por perfil:**
  - Administrador: `{ tareas: ["Configurar estados de propiedad", "Publicar nuevas unidades"] }`
  - Agente de ventas: `{ tareas: ["Registrar visitas", "Enviar propuestas", "Disparar recordatorios de pagos"] }`
  - Propietario: `{ tareas: ["Revisar contratos", "Actualizar disponibilidad"] }`
- **Fuentes de datos existentes:** `CRM actual (Zoho)`, `Planilla inventario semanal (Google Sheets)`
- **Integraciones requeridas:** `Mercado Pago Checkout Pro`, `WhatsApp Cloud API`, `Firma electrónica (Autentic.ar)`
- **Disponibilidad de datos:** `{ disponible: true, formato: "API", volumen_estimado: "150 propiedades activas, 50 reservas mensuales" }`
- **Reglas de negocio (inmobiliaria):**
  - "Estados de propiedad: Disponible, Reservada, Alquilada; cambio solo permitido por administrador."
  - "Publicación requiere fotos mínimas y precio actualizado."
  - "Contrato digital exige validación de documentación del propietario."
  - "Cobranza: recordatorio automático a las 24h y 72h antes de vencimiento."
- **Páginas/pantallas:** `Landing comercial`, `Panel administrador`, `Detalle de propiedad`, `Flujo de pago de seña`, `Centro de notificaciones`
- **Notas de contenido y estilo:** "Estilo moderno, colores azul y blanco, destacar testimonios de inquilinos."
- **Plazo objetivo:** `2024-07-15`
- **Rango de inversión:** `ARS 3.500.000`
- **Restricciones:** "Integración debe operar con AFIP para comprobantes."
- **Supuestos clave:** `Inventario centralizado se actualiza diariamente`, `Equipo interno capacitado en carga de datos`, `Usuarios aceptan notificaciones digitales`
- **Riesgos:**
  - `{ riesgo: "Demoras en aprobación de WhatsApp Business", impacto: Alto, probabilidad: Media, mitigación: "Iniciar solicitud con 3 semanas de anticipación." }`
  - `{ riesgo: "Integración CRM limitada", impacto: Medio, probabilidad: Media, mitigación: "Plan B exportación CSV semanal." }`
  - `{ riesgo: "Cambios en política de Mercado Pago", impacto: Medio, probabilidad: Baja, mitigación: "Revisión semanal de actualizaciones." }`
- **Aceptación de T&Cs y Política de Privacidad:** `true (2024-05-03, versión 1.2)`
- **Opt-in WhatsApp:** `{ fecha: "2024-05-02", fuente: "Form web", evidencia: "https://drive.google.com/..." }`
- **Retención de datos (meses):** `24`
- **Monto de seña:** `ARS 150.000`
- **Medio de pago:** `Checkout Pro`
- **Preferencia de agenda:** "Franja tarde (15:00–18:00) GMT-3"

## Próximos pasos hacia Prototipado
- Implementar formulario validado en el front conversacional con retroalimentación en tiempo real.
- Definir mapeo de brief a plantillas de propuesta automática.
- Configurar almacenamiento seguro y versionado del brief en la base de datos.
