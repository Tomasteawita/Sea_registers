# Sea Registers - Calculadora de registros
---
El propósito de este repositorio es desarrollar una aplicación web que automatice los cálculos de asistencia que deben realizar las maestras de nivel primario en periodos mensuales.

## Funciones y características

La aplicación incluye:

* Usuarios.
* Registros por usuario.
* Entidades: estudiante, comisión.

La aplicación permite realizar un CRUD completo para los usuarios registrados en la aplicación, lo cual incluye:

* Crear, borrar, actualizar y modificar las entidades "estudiante" y "comisión".
* Registrar la asistencia de cada alumno.
* Realizar los siguientes cálculos:
    * Asistencia media.
    * Asistencia total.
    * Inasistencia media.
    * Inasistencia total.

Los datos se almacenan localmente utilizando SQLite3 como base de datos.

## Propuesta de valor

### Situación

Las maestras de nivel primario tienen que realizar tareas mensuales que les quitan tiempo que podrían dedicar a su actividad principal: planificar y dar clases a sus alumnos. Actualmente, estas tareas mensuales, trimestrales y anuales consumen mucho tiempo de las maestras, el cual podrían utilizar para desarrollar actividades para sus alumnos o simplemente descansar y tener más energía para sus tareas fundamentales. Algunas de estas tareas incluyen:

* Redacción de boletines trimestrales con notas de los alumnos.
* Desarrollo del "Registro de alumnos", que implica realizar cálculos matemáticos.
* Planificación de contenido y actividades pedagógicas.
* Otras tareas.

### Propuesta

Se propone desarrollar una aplicación que automatice estos procesos, permitiendo a las maestras y profesores ahorrar tiempo y utilizarlo en actividades más fundamentales. Uno de los recursos más valiosos que las personas tienen es el tiempo.

## Requisitos

* Python 3.11.4
* Node 18.16.1
* SASS 3.6.5
* Bootstrap 5.3.0

## Frameworks y bibliotecas

* Django==4.2.1
* Pillow==9.5.0

## Instalación y ejecución del proyecto

El proyecto aprovecha la posibilidad de crear entornos virtuales de Python.

```bash
python -m venv venv
```

Luego, activaremos el entorno:

* En Windows:

```bash
.\venv\Scripts\activate
```

* macOS y Linux:

```bash
source venv/bin/activate
```

Una vez dentro, instala las dependencias requeridas utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

Luego, navega al directorio del proyecto y ejecútalo:

```bash
cd Sea_registers
python manage.py runserver
```

