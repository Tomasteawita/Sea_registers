from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

url_logins = [
     path('login/', LoginView.as_view(), name = "Login"),
     path('logout/', LogoutView.as_view(), name = "Logout"),
     path('singup/', SingUpView.as_view(), name = "Singup")
]

url_calculates = [
     path('sub_assistence/<str:student_id>/', sub_assistence, name = "Sub"),
     path('add_assistence/<str:student_id>/', add_assistence, name = "Add"),
     path('sub_all/', sub_all_students, name = "Sub all"),
     path('add_all/', add_all_students, name = "Add all")
]

url_crud = [
     path('students/<int:comission_id>/', StudentView.as_view(), name = 'Student'),
     path('create_student/<int:comission_id>/', StudentCreateView.as_view(), name = 'StudentCreate'),
     path('delete_student/<pk>/', StudentDeleteView.as_view(), name = 'StudentDelete'),
     path('update_studant/<pk>/',StudentUpdateView.as_view(), name = "StudentUpdate"),
     path('create_comission/<pk>/', ComissionCreateView.as_view(), name = 'ComissionCreate'),
     path('delete_comission/<pk>/', ComissionDeleteView.as_view(), name = 'ComissionDelete'),
     path('create_school/<pk>/', SchoolCreateView.as_view(), name = 'SchoolCreate')
]

urls_utils = url_calculates + url_logins + url_crud

urlpatterns = [
     path('', IndexView.as_view(), name = "Index"),
     path('calculator/<int:comission_id>/', CalculatorView.as_view(), name="Calculator"),     
     path('config/<int:comission_id>/', ConfigView.as_view(), name = 'Config'),
] + urls_utils + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)