from django.urls import path
from . import views  # importa views.py

urlpatterns = [
    path('', views.home_view, name='home'),
]
