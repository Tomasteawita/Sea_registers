class Register:
    """
    Clase que representa el registro de asistencias de los estudiantes.

    Attributes:
        request (HttpRequest): Objeto HttpRequest para acceder a la sesión.
        session (SessionStore): Almacén de sesión para guardar el registro.
        register (dict): Diccionario que contiene el registro de asistencias.
        available_days (int): Número de días disponibles para registrar asistencias.
        month (str): Mes actual del registro.
        mean_assistence (int): Promedio de asistencias por estudiante.
        total_available_days (int): Total de días disponibles para asistencia.

    Methods:
        set_students(students): Establece los estudiantes y crea el registro.
        save_register(): Guarda el registro en la sesión.
        add_all_students(): Añade una asistencia a todos los estudiantes.
        sub_all_students(): Resta una asistencia a todos los estudiantes.
        sub_student(student): Resta una asistencia a un estudiante específico.
        add_student(student): Añade una asistencia a un estudiante específico.
    """

    def __init__(self, request):
        """
        Inicializa una instancia de la clase Register.

        Args:
            request (HttpRequest): Objeto HttpRequest para acceder a la sesión.
        """
        self.request = request
        self.session = request.session
        register = self.session.get("register")
        current_comission = self.session.get("current_comission")
        
        if not register:
            self.session["register"] = {}
            self.register = self.session["register"]
            
        else:
            self.register = register
        
        if not current_comission:
            self.session["current_comission"] = None
            self.current_comission = self.session["current_comission"]
        
        else:
            self.current_comission = current_comission

        self.available_days = 0
        self.month = ''
        self.mean_assistence = 0
        self.total_available_days = 0

    def set_students(self, students):
        """
        Establece los estudiantes y crea el registro de asistencias.

        Args:
            students (QuerySet): Conjunto de estudiantes.

        """
        self.register = {}
        for student in students:
            self.register[str(student.id)] = {
                "name": student.name,
                "assistance": 0,
                "inassistance": 0
            }
            
        self.save_register()

    def set_current_comission(self, comission):
        """
        Actualiza las variables del objeto con la información actualizada sobre la comisión.
        
        Args:
            comission (int): id de la comision.
        """
        self.session["current_comission"] = comission
        self.current_comission = self.session["current_comission"]
        self.session.modified = True

    def save_register(self):
        """
        Guarda el registro en la sesión.
        """
        self.session["register"] = self.register
        self.session.modified = True

    def add_all_students(self):
        """
        Añade una asistencia a todos los estudiantes.
        """
        for student in self.register['Alumno']:
            self.register['Asistencia total'][student] += 1
        self.save_register()

    def sub_all_students(self):
        """
        Resta una asistencia a todos los estudiantes.
        """
        for student in self.register['Alumno']:
            self.register['Asistencia total'][student] -= 1
        self.save_register()

    def sub_student(self, student):
        """
        Resta una asistencia a un estudiante específico.

        Args:
            student (str): Nombre del estudiante.
        """
        index = self.register['Alumno'].index(student)
        self.register['Asistencia total'][index] -= 1
        self.save_register()

    def add_student(self, student):
        """
        Añade una asistencia a un estudiante específico.

        Args:
            student (str): Nombre del estudiante.
        """
        index = self.register['Alumno'].index(student)
        self.register['Asistencia total'][index] += 1
        self.save_register()
