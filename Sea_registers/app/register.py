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
        if not register:
            self.session["register"] = {}
            self.register = self.session["register"]
        else:
            self.register = register

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
        names = [student.name for student in students]
        quantity_students = len(names)
        assistences = [0] * quantity_students
        inassistences = [0] * quantity_students
        dict_students = {
            'Alumno': names,
            'Asistencia total': assistences,
            'Inasistencia total': inassistences
        }
        self.register = dict_students
        self.total_available_days = quantity_students * self.available_days
        self.save_register()

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
