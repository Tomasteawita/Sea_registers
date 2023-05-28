import pandas as pd
import numpy as np
class Register:
    def __init__(self,students):
        
        names = [student.name for student in students]
        quantity_students = len(names)
        assistences = list(np.zeros(quantity_students))
        inassistences = list(np.zeros(quantity_students))
        dict_students = {
            'Alumno': names,
            'Asistencia total': assistences,
            'Inasistencia total': inassistences
        }
        self.register = pd.DataFrame(dict_students)
        self.available_days = 0
        self.month = ''
        self.mean_assistence = 0
        self.total_available_days = quantity_students * self.available_days
        
    
    def add_all_students(self):
        self.register['Asistencia total'] = self.register['Asistencia total'].add(1)
    
    def sub_all_students(self):
        self.register['Asistencia total'] = self.register['Asistencia total'] - 1
    
    def sub_student(self,student):
        self.register.loc[self.register['Alumno'] == student, 'Asistencia total'] -= 1
    
    def add_student(self,student):
        self.register.loc[self.register['Alumno'] == student, 'Asistencia total'] += 1
        


        

    