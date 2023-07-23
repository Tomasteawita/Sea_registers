class Register:
    """
    Clase que representa el registro de asistencias de los estudiantes.

    Attributes:
        request (HttpRequest): Objeto HttpRequest para acceder a la sesión.
        session (SessionStore): Almacén de sesión para guardar el registro.
        register (dict): Diccionario que contiene el registro de asistencias.
        available_days (int): Número de días disponibles para registrar asistencias.
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
        self.initialize_register()

    def save_register(self):
        """
        Guarda el registro en la sesión.
        """
        self.session["register"] = self.register
        self.session.modified = True

    def initialize_register(self):
        register = self.session.get("register")
        current_comission = self.session.get("current_comission")
        available_days = self.session.get("available_days")
        
        if not register:
            self.session["register"] = {}
        
        self.register = self.session["register"]
            
        if not current_comission:
            self.session["current_comission"] = None
        
        self.current_comission = self.session["current_comission"]

        if not available_days:
            self.session["available_days"] = 0
        
        self.available_days = self.session["available_days"]
        
    def set_available_days(self ,days):
        """
        Actualiza las variables del objeto con la información actualizada sobre los días habiles.
        
        Args:
            days (int): cantidad de días habiles.
        """
        self.session["available_days"] = days
        self.available_days = self.session["available_days"]
        self.session.modified = True
    
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
                "assistance": self.available_days,
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

    def get_students(self):
        return self.register
    
    def get_available_days(self):
        return self.available_days

    def add_all_students(self):
        """
        Añade una asistencia a todos los estudiantes.
        """
        for key in self.register:
            self.register[key]['assistance'] += 1
            self.register[key]['inassistance'] -= 1
        self.save_register()

    def add_student(self, student_id):
        """
        Añade una asistencia a un estudiante específico.

        Args:
            student_id (str): id del alumno.
        """
        self.register[student_id]['assistance'] += 1
        self.register[student_id]['inassistance'] -= 1
        self.save_register()
    def sub_all_students(self):
        """
        Resta una asistencia a todos los estudiantes.
        """
        for key in self.register:
            self.register[key]['assistance'] -= 1
            self.register[key]['inassistance'] += 1
        self.save_register()

    def sub_student(self, student_id):
        """
        Resta una asistencia a un estudiante específico.

        Args:
            student_id (str): id del alumno.
        """
        self.register[student_id]['assistance'] -= 1
        self.register[student_id]['inassistance'] += 1
        self.save_register()


