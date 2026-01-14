from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home OK")

urlpatterns = [
    path('', home, name='home'),
]
