from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
     path('login/', AdminLoginView.as_view(),name = "Login"),
     path('logout/', AdminLogoutView.as_view(),name = "Logout"),
     path('singup/', SingUp.as_view(),name="Singup"),
     path('', Index.as_view(), name = "Index"),
     path('calculator/<int:comission_id>/<int:days>/', Calculator.as_view(), name="Calculator"), 
     path('sub_assistence/<str:student_id>/', sub_assistence, name = "Sub"),
     path('add_assistence/<str:student_id>/', add_assistence, name = "Add"),
     path('config/<int:comission_id>', Config.as_view(), name = 'Config'),
     path('sub_all/', sub_all_students, name = "Sub all"),
     path('add_all/', add_all_students, name = "Add all")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)