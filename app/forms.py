from django import forms
from .models import *
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm


class TeacherForm(forms.Form):
    user = forms.ModelChoiceField(queryset = User.objects.all())
    name = forms.CharField(max_length = 50, required = False)
    phone = forms.CharField(max_length = 12)
    image = forms.ImageField()
    
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name']

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['name', 'school']

    def __init__(self, user, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        # Filtrar las escuelas según el usuario registrado
        self.fields['school'].queryset = School.objects.filter(user=user)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

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