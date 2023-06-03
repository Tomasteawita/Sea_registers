from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50) 
    image = models.ImageField(upload_to = 'perfil_image',null = True,blank = True)
    def __str__(self) -> str:
        return  f'{super().__str__()}' 

class School(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self) -> str:
        return super().__str__()

class Commission(models.Model):
    name = models.CharField(max_length = 3)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length = 150)
    comission = models.ForeignKey(Commission, on_delete = models.CASCADE)
    