from django.shortcuts import render
from .models import Module


def home(request):
    return render(request, "coursereg/home.html", {"title": "Home page"})

def modules(request):
    return render(request, "coursereg/modules.html", {"title": "Modules page","modules":Module.objects.all()})

def module_details(request,code):
    module= Module.objects.filter(code=code).first()
    if module:
        context={"title" : module.module_name, "module" : module, "courses" : module.courses, "registrations" : module.registrations}
    else:
        context={"title": "Module not found"}
    return render(request,"coursereg/module_detail.html",context )