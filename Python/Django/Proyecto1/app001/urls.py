#Capturar las urls de mi aplicación

from django.urls import path
from .views import index, saludar

urlpatterns = [
    path('', index),
    path('saludar/', saludar),
]
