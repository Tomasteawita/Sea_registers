from django.urls import path
from .views import *
urlpatterns = [
     path('',index,name="index"),
     path('login/',AdminLoginView.as_view(),name="login"),
     path('singup/',SingUp.as_view(),name="singup"),
]