from django.shortcuts import render,redirect
from .forms import * 
from .models import *
from .register import Register
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin



def calculator(request):
    return render(request,'calculator.html')

def inicialization_params_calculator(request, id_comission):
    students = Student.objects.filter(comission_id = id_comission)
    register = Register(request)
    register.set_students(students)
    return redirect('calculator')
"""def login(request):
    
    context = None
    return render(request, 'login.html', {'context': context })
"""
"""class Index(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'index.html'
    
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
    template_name = 'singup.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'
    
"""class AdminLogoutView(LogoutView):
    template_name = 'logout.html'"""