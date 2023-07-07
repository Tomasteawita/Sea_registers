from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import *
from .models import *
from .register import Register
from django.views.generic import ListView, View
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, FormView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Calculator(ListView, View):
    """
    Vista que muestra la calculadora de asistencias para una comisión específica.
    """
    template_name = 'calculator/calculator.html'
    model = Student
    def get_queryset(self):
        """
        Obtiene la lista de estudiantes de la comisión especificada.

        Returns:
            QuerySet: Lista de estudiantes filtrados por comisión.
        """
        id_comission = self.kwargs['comission_id']
        student_list = Student.objects.filter(comission_id = id_comission)
        return student_list

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto.

        Returns:
            dict:{
                'paginator': None, 
                'page_obj': None, 
                'is_paginated': False, 
                'object_list': list, 
                'view': <app.views.Calculator object at 0x000001D9F9D9E850>
            }
        """
        context = {}
        register = Register(self.request)

        if register.current_comission != self.kwargs['comission_id']:
            students = self.get_queryset()
            register.set_students(students)
            register.set_current_comission(self.kwargs['comission_id'])

        context["register"] = register
        print(context)
        
        return context


class Index(ListView, View):
    """
    Vista de la página de inicio.
    """
    template_name = 'index.html'

    def get_queryset(self):
        """
        Obtiene las comisiones asociadas al usuario actual.

        Returns:
            dict: Diccionario con las comisiones filtradas por usuario.
        """
        commission = Commission.objects.filter(user_id=self.request.user.id)
        queryset = {
            'commission': commission
        }
        return queryset


class SingUp(CreateView):
    """
    Vista para registrar un nuevo usuario.
    """
    form_class = SingUpForm
    success_url = '/'
    template_name = 'login/singup.html'


class AdminLoginView(LoginView):
    """
    Vista para el inicio de sesión del administrador.
    """
    template_name = 'login/login.html'


class AdminLogoutView(LogoutView):
    """
    Vista para cerrar sesión del administrador.
    """
    template_name = 'login/logout.html'


@login_required
def sub_assistence(request, student_id):
    """
    Registra una asistencia negativa para el estudiante especificado.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.
        student_id (int): ID del estudiante.

    Returns:
        HttpResponseRedirect: Redirige a la página de la calculadora.
    """
    register = Register(request)
    register.sub_student(student_id)
    return redirect("Calculator", register.current_comission)

def add_assistence(request, student_id):
    """
    Registra una asistencia positiva para el estudiante especificado.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.
        student_id (int): ID del estudiante.

    Returns:
        HttpResponseRedirect: Redirige a la página de la calculadora.
    """
    register = Register(request)
    register.add_student(student_id)
    return redirect("Calculator", register.current_comission)

def add_all_students(request):
    """
    Registra asistencia positiva para todos los estudiantes.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponseRedirect: Redirige a la página de la calculadora.
    """
    register = Register(request)
    register.add_all_students()
    return redirect("Calculator", register.current_comission)

def sub_all_students(request):
    """
    Registra asistencia negativa para todos los estudiantes.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponseRedirect: Redirige a la página de la calculadora.
    """
    register = Register(request)
    register.sub_all_students()
    return redirect("Calculator", register.current_comission)
