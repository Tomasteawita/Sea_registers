from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
     path('login/', AdminLoginView.as_view(),name = "Login"),
     path('logout/', AdminLogoutView.as_view(),name = "Logout"),
     path('singup/', SingUp.as_view(),name="Singup"),
     path('', Index.as_view(), name = "Index"),
     path('calculator/<int:comission_id>/', Calculator.as_view(), name="Calculator"), 
     path('sub_assistence/<int:student_id>/', sub_assistence, name = "Sub")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)