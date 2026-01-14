from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departamento/', include('applications.departamento.urls')),
    path('', include('applications.home.urls')),  # Home en la raíz
]
