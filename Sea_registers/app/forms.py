from django import forms
from .models import *
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm


class TeacherForm(forms.Form):
    user = forms.ModelChoiceField(queryset = User.objects.all())
    name = forms.CharField(max_length = 50, required = False)
    phone = forms.CharField(max_length = 12)
    image = forms.ImageField()
    
class SchoolForm(forms.Form):
    name = forms.CharField(max_length = 150)

class CommissionForm(forms.Form):
    name = forms.CharField(max_length= 3)
    school = forms.ModelChoiceField(queryset = School.objects.all())
    teacher = forms.ModelChoiceField(queryset = Teacher.objects.all())

class StudentForm(forms.Form):
    name = forms.CharField(max_length= 150)
    comission = forms.ModelChoiceField(queryset = Commission.objects.all())

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}