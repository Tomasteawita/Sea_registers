# Sea Registers - calculadora de registros
---
El proposito de este repositorio es desarrollar una aplicación web para automatizar los calculos de asistencias que tiene que realizar las maestras de nivel primario en periodos mensuales

## Funciones y características
La app contiene:
* Usuarios.
* Registros por usuario.
* Entidades: estudiante, comision.

La app permite hacer un CRUD completo para los usuarios registrados en la aplicación para:
* Crear, borrar, eliminar y modificar las entidades "estudiante" y "comision".
* Registrar asistencia para cada alumno.
* Hacer los calculos de:
    * Asistencia media
    * Asistencia total
    * Inasistencia media
    * Inasistencia total

Los datos se almacenan localmente usando SQLite3 como base de datos.

## Propuesta de valor
### Situación
Existen tareas mensuales para las maestras que les quitan tiempo para centrarse en su actividad principal, la cual es planificar para dar clases y dar clases a sus alumnos, hoy en día existen tareas mensuales, trimestrales y anuales que le quitan mucho tiempo a las maestras, el cual podria utilizar para desarrollar actividades para sus alumnos o simplementa para descansar y tener más energía para sus fines fundamentales. Entre esas tareas se encuentan:
* La redacción de boletines trimestrales con notas de alumnos.
* El desarrollo del "Registro de alumnos" en el cual desarrollan cuentas matematicas.
* Planificación de contenido y actividades pedagogicas.
* otras.

### Propuesta
Se plantea desarrollar una aplicación para automatizar dichos procesos para ahorrar y utilizar en actividades más fundamentales de las maestras y profesores uno de los recursos más fundamentales que tienen las personas, el tiempo.

## Requerimentos
* Python 3.11.4
* Node 18.16.1
* SASS 3.6.5
* Boostrap 5.3.0

## Framework y Bibliotecas
* Django==4.2.1
* Pillow==9.5.0

## Instalación y ejecución del proyecto
El proyecto aprobecha la posibilidad de la creacion de entornos virtuales de Python
```bash
python -m venv venv
```
Luego activaremos dicho entorno:
* En Windows:
```bash
.\venv\Scripts\activate
```

* macOS y Linux:
```bash
source venv/bin/activate
```

* Una vez dentro, instalar las dependencias requeridas con el comando pip install requirements.
```bash
pip install -r requirements.txt
```

* Nos movemos al direcotorio del proyecto y lo ejecutamos
```bash
cd Sea_registers
python manage.py runserver
```


Ejemplos de uso: Proporciona ejemplos de cómo utilizar tu proyecto en la práctica. Esto puede incluir fragmentos de código, comandos de línea de comandos o capturas de pantalla que ilustren su funcionamiento. Cuantos más ejemplos des, mejor comprensión tendrán los usuarios sobre cómo pueden aprovechar tu proyecto.

Documentación adicional: Si tu proyecto tiene una documentación más extensa, como una wiki o un sitio web, asegúrate de incluir enlaces a esa documentación en el README.md. Esto permitirá a los usuarios acceder a información más detallada si así lo desean.

Contribuciones: Si deseas que otros contribuyan a tu proyecto, proporciona pautas claras sobre cómo pueden hacerlo. Puedes explicar cómo presentar problemas (issues), solicitar características (feature requests) o enviar solicitudes de extracción (pull requests). También es útil mencionar cualquier convención de nomenclatura o estilo de codificación que prefieras.

Licencia: Es importante indicar claramente la licencia bajo la cual se distribuye tu proyecto. Esto establece los términos y condiciones para el uso del código y protege tus derechos como autor.

Contacto: Proporciona tus datos de contacto, como tu dirección de correo electrónico o perfil de redes sociales, para que las personas puedan comunicarse contigo si tienen preguntas, comentarios o problemas relacionados con tu proyecto.

Recuerda que estos son solo puntos de partida y puedes personalizar tu README.md según las necesidades específicas de tu proyecto. La idea principal es brindar información clara y concisa para que otros puedan entender rápidamente lo que haces y cómo pueden utilizar o contribuir a tu proyecto.