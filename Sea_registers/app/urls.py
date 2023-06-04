from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
     path('',index,name = "index"),
     path('login/',AdminLoginView.as_view(),name = "login"),
     path('logout/',AdminLogoutView.as_view(),name = "logout"),
     path('singup/',SingUp.as_view(),name="singup"),
     path('indexClass/',Index.as_view(), name = "indexClass")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)