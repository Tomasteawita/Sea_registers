from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import * 
from .models import *
from .register import Register
from django.views.generic import ListView ,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Calculator(ListView):
    template_name = 'calculator/calculator.html'
    model = Student 

    def get_queryset(self):
        id_comission = self.kwargs['comission_id']
        student_list = Student.objects.filter(comission_id = id_comission) 
        return student_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #id_comission = self.kwargs['comission_id']
        students = self.get_queryset()
        register = Register(self.request)
        register.set_students(students)
        # Agrega cualquier otro dato adicional al contexto si es necesario
        print(context)
        return context
    


class Index(ListView,View):
    
    template_name = 'index.html'
        
    def get_queryset(self):
        commission = Commission.objects.filter( user_id = self.request.user.id)
        queryset = {
            'commission' : commission
            }
        return queryset
    
    
"""    
class delete_post(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'confirm_post_delete.html'
    
class EditPost(UpdateView):
    model = Post
    success_url = '/'
    template_name = 'edit_post.html'
    fields = ['title','description','image','user','category']
    
class UpdatePost(CreateView):
    model = Post
    success_url = '/'
    template_name = 'edit_post.html'
    fields = ['title','description','image','category','avatar'] 
"""
class SingUp(CreateView):
    form_class = SingUpForm
    success_url = '/'
    template_name = 'login/singup.html'

class AdminLoginView(LoginView):
    template_name = 'login/login.html'
    
class AdminLogoutView(LogoutView):
    template_name = 'login/logout.html'
    

def sub_assistence(request,student_id):
    register = Register(request)
    student = Student.objects.get(id = student_id)
    register.sub_student(student.name)
    return redirect("Calculator",1)