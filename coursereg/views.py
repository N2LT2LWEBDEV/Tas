from django.shortcuts import render
from .models import Module


def home(request):
    return render(request, "coursereg/home.html", {"title": "Home page"})

def modules(request):
    return render(request, "coursereg/modules.html", {"title": "Modules page","modules":Module.objects.all()})

