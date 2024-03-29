from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .register import Register
from django.db.models import Prefetch
from django.views.generic import ListView, View
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

class CalculatorView(ListView, View, LoginRequiredMixin):
    """
    Vista que muestra la calculadora de asistencias para una comisión específica.
    """
    template_name = 'calculator/calculator.html'
    model = Student
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        register = Register(request)
        students = register.get_students()
        results_data = {}
        available_days = register.get_available_days()
        
        total_assistance = sum(student['assistance'] for student in students.values())
        total_inassistance = sum(student['inassistance'] for student in students.values())
        total_available_days = available_days * len(students)
        
        assistance_percentage = (total_assistance * 100) / (total_assistance + total_inassistance)
        inassistance_percentage = (total_inassistance * 100) / (total_assistance + total_inassistance)
        
        results_data["total_assistance"] = total_assistance
        results_data["total_inassistance"] = total_inassistance
        results_data["assistance_percentage"] = assistance_percentage
        results_data["inassistance_percentage"] = inassistance_percentage
        results_data["media_assistance"] = total_available_days / total_assistance
        
        return render(request, self.template_name, {'results_data': results_data})

class ConfigView(View, LoginRequiredMixin):
    template_name = 'calculator/config.html'

    def get_queryset(self, commission_id):
        """
        Obtiene la lista de estudiantes de la comisión especificada.

        Returns:
            QuerySet: Lista de estudiantes filtrados por comisión.
        """
        id_comission = commission_id
        student_list = Student.objects.filter(comission_id = id_comission)
        return student_list
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs): 
        register = Register(request)
        register.set_available_days(int(request.POST.get('days')))
        students = self.get_queryset(self.kwargs['comission_id'])
        register.set_students(students)
        register.set_current_comission(self.kwargs['comission_id'])
        
        url = reverse('Calculator', kwargs = {
            'comission_id' : self.kwargs['comission_id'] 
            })

        return redirect(url)

class IndexView(ListView):
    template_name = 'index.html'
    model = Commission

    def get_queryset(self):
        return Commission.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SchoolCreateView(CreateView, LoginRequiredMixin):
    model = School
    form_class = SchoolForm
    template_name = 'school/create_school.html'
    
    def get_success_url(self):
        return reverse_lazy('Index')
    
    def form_valid(self, form):
        school = form.save(commit=False)
        school.user_id = self.kwargs['pk']
        school.save()
        
        return super().form_valid(form)

class ComissionCreateView(CreateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionForm
    template_name = 'comission/create_comission.html'

    def get_success_url(self):
        return reverse_lazy('Index')

    def get_form_kwargs(self):
        kwargs = super(ComissionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        commission = form.save(commit=False)
        commission.user_id = self.kwargs['pk']
        commission.save()

        return super().form_valid(form)

class ComissionDeleteView(DeleteView, LoginRequiredMixin):
    model = Commission
    template_name = 'comission/delete_comission.html'
    success_url = '/'
    
class StudentCreateView(CreateView, LoginRequiredMixin):
    model = Student
    form_class = StudentForm  
    template_name = 'students/create_student.html'
    
    def get_success_url(self):
        return reverse_lazy('StudentCreate', kwargs={'comission_id': self.kwargs['comission_id']})
    
    def form_valid(self, form):
        student = form.save(commit=False)
        student.comission_id = self.kwargs['comission_id']
        student.save()
        
        return super().form_valid(form)

class StudentDeleteView(DeleteView, LoginRequiredMixin):
    model = Student
    template_name = 'students/delete_student.html'

    def get_success_url(self):
        comission_id = self.get_object().comission_id
        return reverse_lazy('Student', kwargs={'comission_id': comission_id})

class StudentView(ListView, LoginRequiredMixin):
    template_name = 'students/student.html'
    model = Student
    def get_queryset(self, commission_id):
        """
        Obtiene la lista de estudiantes de la comisión especificada.

        Returns:
            QuerySet: Lista de estudiantes filtrados por comisión.
        """
        id_comission = commission_id
        student_list = Student.objects.filter(comission_id = id_comission)
        return student_list
    
    def get(self, request, *args, **kwargs):
        students = self.get_queryset(kwargs['comission_id'])
        commission = Commission.objects.get(id = kwargs['comission_id'])
        
        return render(request, self.template_name, context = {
            'students' : students, 
            'comission' : commission
            })

class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/'
    template_name = 'students/update_student.html'
    fields = ['name']

class SingUpView(CreateView):
    """
    Vista para registrar un nuevo usuario.
    """
    form_class = SingUpForm
    template_name = 'login/singup.html'
    
    def get_success_url(self):
        return reverse_lazy('Login')

class LoginView(LoginView):
    """
    Vista para el inicio de sesión del administrador.
    """
    template_name = 'login/login.html'

class LogoutView(LogoutView):
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
    url = reverse('Calculator', kwargs = {
            'comission_id' : register.current_comission, 
            })

    return redirect(url)

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
    url = reverse('Calculator', kwargs = {
            'comission_id' : register.current_comission, 
            })

    return redirect(url)

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
    url = reverse('Calculator', kwargs = {
            'comission_id' : register.current_comission, 
            })

    return redirect(url)

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
    url = reverse('Calculator', kwargs = {
            'comission_id' : register.current_comission, 
            })

    return redirect(url)