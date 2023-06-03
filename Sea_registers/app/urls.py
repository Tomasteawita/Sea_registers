from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
     path('',index,name="index"),
     path('login/',AdminLoginView.as_view(),name="login"),
     path('singup/',SingUp.as_view(),name="singup"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)