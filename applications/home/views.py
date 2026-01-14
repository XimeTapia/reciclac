from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')  # index.html está en templates/
