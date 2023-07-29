# Sea Registers - Calculadora de registros
---
El propósito de este repositorio es desarrollar una aplicación web que automatice los cálculos de asistencia que deben realizar las maestras de nivel primario en periodos mensuales.

## Funciones y características

La aplicación incluye:

* Usuarios.
* Registros por usuario.
* Entidades: estudiante, comisión.

La aplicación permite realizar un CRUD completo para los usuarios registrados en la aplicación, lo cual incluye:

* Crear, borrar, actualizar y modificar las entidades "estudiante", "comisión" y "escuela".
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

## Frameworks y bibliotecas

* Django==4.2.1
* Pillow==9.5.0
* psycopg2-binary==2.9.6

## Imagenes de Docker
* node:alpine
* python:3.9-alpine
* postgres:15-alpine

## Instalación y ejecución del proyecto

Para ejecutar el proyecto debemos tener Docker instalado.

1. Nos posicionamos en el directorio raiz del proyecto y creamos la carpeta postgres_data:
```bash
mkdir postgres_data
```

2. Luego de crear la carpeta que usaremos como volumen de PostgreSQL, corremos nuestros contenedores:
```bash
docker-compose up --build
```
3. Una vez creado el entorno de trabajo, accedemos al contenedor del servicio Django en modo interactivo:

```bash
docker exec -it bofi sh
```

4. Dentro del contenedor, ejecutamos las migraciones:
```shell
python manage.py makemigrations
python manage.py migrate
```

5. Creo un usuario administrador; ejecuto el comando, luego completo los campos solicitados:
```shell
python manage.py createsuperuser
```

6. Finalmente podremos correr el proyecto con:
```shell
python manage.py runserver 0.0.0.0:8000
```
En nuestro navegador accedemos a la direccion: 127.0.0.1:8000 para acceder al index o bien podemos ingresar directamente desde http://localhost:8000
