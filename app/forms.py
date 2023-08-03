from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class TeacherForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuario")
    name = forms.CharField(max_length=50, required=False, label="Nombre")
    phone = forms.CharField(max_length=12, label="Teléfono")
    image = forms.ImageField(label="Imagen")

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name']
        labels = {'name': 'Nombre'}

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['name', 'school']
        labels = {
            'name': 'Nombre',
            'school': 'Escuela'
        }

    def __init__(self, user, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        # Filtrar las escuelas según el usuario registrado
        self.fields['school'].queryset = School.objects.filter(user=user)
        self.fields['school'].label = 'Escuela'  # Opcional, puedes cambiar la etiqueta aquí si lo prefieres.

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
        labels = {'name': 'Nombre'}

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

        help_texts = {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

        help_texts = {k: '' for k in fields}
