import pandas as pd
import numpy as np
class Register:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        register = self.session.get("register")
        if not register:
            self.session["register"] = pd.DataFrame()
            self.register = self.session["register"]
        else:
            self.register = register
        
        self.available_days = 0
        self.month = ''
        self.mean_assistence = 0
        self.total_available_days = 0
    
    def set_students(self,students):
        names = [student.name for student in students]
        quantity_students = len(names)
        assistences = np.zeros(quantity_students)
        inassistences = np.zeros(quantity_students)
        dict_students = {
            'Alumno': names,
            'Asistencia total': assistences,
            'Inasistencia total': inassistences
        }
        self.register = pd.DataFrame(dict_students)
        self.total_available_days = quantity_students * self.available_days
        self.save_register()
        
    def save_register(self):
        self.session["register"] = self.register
        self.session.modified = True
        
    def add_all_students(self):
        self.register['Asistencia total'] = self.register['Asistencia total'].add(1)
        self.save_register()
    
    def sub_all_students(self):
        self.register['Asistencia total'] = self.register['Asistencia total'] - 1
        self.save_register()
        
    def sub_student(self,student):
        self.register.loc[self.register['Alumno'] == student, 'Asistencia total'] -= 1
        self.save_register()
        
    def add_student(self,student):
        self.register.loc[self.register['Alumno'] == student, 'Asistencia total'] += 1
        self.save_register()


        

    