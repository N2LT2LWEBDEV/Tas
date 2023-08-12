from django.shortcuts import render
from .models import Module
from django.contrib.auth.models import Group
from accounts.models import Student


def home(request):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, "coursereg/home.html", {"title": "Home page", 'student': student})


def about(request):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, 'coursereg/about.html', {'student': student})


def contact(request):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, 'coursereg/contact.html', {'student': student})


def modules(request):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, "coursereg/modules.html", {"title": "Modules page", "modules": Module.objects.all(), 'student': student})


def courses(request):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, "coursereg/courses.html", {"title": "Courses page", "courses": Group.objects.all(), 'student': student})


def course_details(request, pk):
    course = Group.objects.get(id=pk)
    course_modules = Module.objects.filter(courses=course)
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    return render(request, "coursereg/course_details.html", {"title": "Courses details page", "course": course, 'student': student, 'modules': course_modules})


def module_details(request, code):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    module = Module.objects.filter(code=code).first()
    if module:
        context = {"title": module.module_name, "module": module, "courses": module.courses,
                   "registrations": module.registrations, 'student': student}
    else:
        context = {"title": "Module not found", 'student': student}
    return render(request, "coursereg/module_detail.html", context)
