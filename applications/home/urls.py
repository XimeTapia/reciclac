from django.urls import path
from . import views  # Importa views.py

urlpatterns = [
    path('', views.home_view, name='home'),  # La vista de home ahora usa template
]
