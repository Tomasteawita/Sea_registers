from typing import Any
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import * 
from .models import *
from .register import Register
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#@login_required
def index(request):
    
    try:
        teacher = Teacher.objects.get(user_id = request.user.id)
    except:
        print('NO SE PUDO TRAER A LA PROFE')
        teacher = False
        commission = False
    else:
        try:
            commission = Commission.objects.filter(teacher_id = teacher.id)
        except:
            commission = False
    finally:
        context = {
            'teacher' : teacher,
            'commission' : commission 
        }        
    
    return render(request, 'index.html', context = context)

def calculator(request):
    return render(request,'calculator.html')

def inicialization_params_calculator(request, id_comission):
    students = Student.objects.filter(comission_id = id_comission)
    register = Register(request)
    register.set_students(students)
    return redirect('calculator')

class Index(ListView):
    
    template_name = 'indexClass.html'
    
    def get_queryset(self):
        user_id = 2
        teacher = get_object_or_404(Teacher, user_id = user_id)
        commission = get_list_or_404( Commission,teacher_id = teacher.id)
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