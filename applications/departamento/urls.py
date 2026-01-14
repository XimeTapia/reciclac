from django.contrib import admin
from django.urls import path
from . import views

app_name="departamento_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Página principal
    path('departamento/lista/', views.DepartamentoListView.as_view(), name='departamento-list'),
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),

]
