# Academia EduOdoo - Gestión Educativa en Odoo

Este módulo de Odoo ha sido diseñado para gestionar de manera integral una academia de idiomas o centro de estudios, permitiendo el control de cursos, sesiones de clase, profesorado, alumnado y facturación.

## Descripción del Proyecto
Academia EduOdoo transforma la gestión académica tradicional en una experiencia digital fluida. El sistema permite planificar horarios, controlar el aforo de las aulas, gestionar la disponibilidad de los docentes y realizar el seguimiento del ciclo de vida de las matrículas de los alumnos.

---

## Desarrollo del Proyecto por Semanas

### Semana 1: Cimientos y Estructura de Datos (26 - 30 Enero)
En la primera fase, definimos la arquitectura del sistema y las relaciones entre los modelos fundamentales:
- **Cursos**: Definición de títulos, niveles (A1-C2) y precios.
- **Sesiones**: Programación de fechas, duraciones y asignación de aulas.
- **Participantes**: Registro de Alumnos y Profesores.
- **Relaciones ORM**: Implementación de relaciones `Many2one` (Sesión -> Curso), `Many2many` (Alumnos <-> Cursos) y `One2many`.

### Semana 2: Lógica de Negocio y Validaciones (2 - 6 Febrero)
Potenciamos el sistema con inteligencia distribuida mediante campos computados y restricciones:
- **Campos Computados (@api.depends)**:
    - Cálculo automático de **Asientos Ocupados**.
    - Cálculo del **Porcentaje de Ocupación** con visualización dinámica en barra de progreso.
- **Validaciones Críticas (@api.constrains)**:
    - **Disponibilidad Docente**: Impide que un profesor sea asignado a dos sesiones que se solapen en el tiempo.
    - **Control de Aforo**: Bloquea la inscripción de más alumnos de los permitidos por el número de asientos de la sesión.
- **Flujo de Matrículas**: Implementación de estados para las inscripciones (`Borrador` -> `Confirmada` -> `Pagada`).

### Semana 3: Experiencia de Usuario - UX/UI (9 - 13 Febrero)
Llevamos la interfaz al siguiente nivel con visualizaciones avanzadas:
- **Vista de Calendario**: Visualización cronológica de sesiones, agrupadas por profesor para optimizar la planificación.
- **Vista Kanban**: Gestión visual por tarjetas agrupadas por curso, incluyendo barras de progreso y selectores de color funcionales.
- **Estilos Dinámicos**: La vista de lista cambia automáticamente el color de la fila (Rojo/Amarillo) según el nivel de ocupación de la sesión.

---

## Restricciones y Reglas de Negocio
El sistema garantiza la integridad de los datos mediante las siguientes reglas:
1.  **No se permiten solapamientos**: Un profesor no puede impartir dos clases al mismo tiempo (se valida mediante `fecha_inicio` y `duracion_horas`).
2.  **Límite de estudiantes**: El número de alumnos en una sesión nunca puede superar el campo `num_asientos`.
3.  **Flujo Dirigido**: Las matrículas siguen un camino lógico de estados, permitiendo la gestión administrativa desde la creación hasta el cobro.

---

## Requisitos e Instalación
1.  Odoo 17.0 o superior.
2.  Dependencias: `base`, `contacts`, `mail`.
3.  **Instalación**: Copiar la carpeta `proyecto_edu_odoo` al directorio de `addons`, actualizar la lista de aplicaciones e instalar "Academia EduOdoo".

---
*Desarrollado como parte del proyecto de Sistemas de Gestión - Jacobo DAM*
