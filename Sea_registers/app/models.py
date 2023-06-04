from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 12) 
    image = models.ImageField(upload_to = 'perfil_image',null = True,blank = True)
    def __str__(self):
        return  f'{self.name}' 

class School(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return f'Escuela: {self.name}'

class Commission(models.Model):
    name = models.CharField(max_length = 3)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    
    def get_school(self, school_template_id):
        school = School.objects.get(id = school_template_id)
        return f'{school}'
    
    def __str__(self):
        return f'{self.name}'
        
class Student(models.Model):
    name = models.CharField(max_length = 150)
    comission = models.ForeignKey(Commission, on_delete = models.CASCADE)
    