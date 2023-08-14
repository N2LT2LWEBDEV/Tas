from django.shortcuts import render, redirect
from .models import Module, Registration
from django.contrib.auth.models import Group
from accounts.models import Student
from django.contrib import messages


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
    is_student_enrolled = False
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        is_student_enrolled = request.user.groups.filter(
            name=course.name).exists()
    return render(request, "coursereg/course_details.html", {"title": "Courses details page", "course": course, 'student': student, 'modules': course_modules, 'is_student_enrolled': is_student_enrolled})


def module_details(request, code):
    student = None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
    module = Module.objects.filter(code=code).first()
    context = {}
    if module:
        is_student_registered = False
        student_module_registration = Registration.objects.filter(
            student=student, module_registered=module)
        if len(student_module_registration) > 0:
            is_student_registered = True
        context = {"title": module.module_name, "module": module, "courses": module.courses,
                   "registrations": module.registrations, 'student': student, 'is_student_registered': is_student_registered}
    else:
        context = {"title": "Module not found", 'student': student}
    return render(request, "coursereg/module_detail.html", context)


def module_register(request, pk):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        module = Module.objects.get(id=pk)
        student_module_registration = Registration.objects.filter(
            student=student, module_registered=module)
        if len(student_module_registration) > 0:
            messages.error(
                request, 'You have already registered with this module')
            return redirect('coursereg:module_details', code=module.code)
        else:
            student_module_registration = Registration(
                module_registered=module, student=student)
            student_module_registration.save()
            messages.success(
                request, 'You have successfully registered with this module')
            return redirect('coursereg:module_details', code=module.code)
    else:
        messages.warning(
            request, "You must be logged in to register with a module")
        return redirect('coursereg:home')


def module_unregister(request, pk):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        module = Module.objects.get(id=pk)
        student_module_registration = Registration.objects.filter(
            student=student, module_registered=module)
        if len(student_module_registration) == 0:
            messages.error(
                request, 'You are not registered with this module')
            return redirect('coursereg:module_details', code=module.code)
        else:
            student_module_registration[0].delete()
            messages.success(
                request, 'You have successfully unregistered from this module')
            return redirect('coursereg:module_details', code=module.code)
    else:
        messages.warning(
            request, "You must be logged in to register with a module")
        return redirect('coursereg:home')


def course_enrol(request, pk):
    if request.user.is_authenticated:
        user = request.user
        course = Group.objects.get(id=pk)
        user_groups = user.groups.all()
        if len(user_groups) > 0:
            if (user_groups[0].name == course.name):
                messages.error(
                    request, 'You are already enrolled in this course')
            else:
                messages.error(
                    request, 'You are already enrolled in another course')
            return redirect('coursereg:course_detail', pk=pk)

        else:
            user.groups.add(course)
            messages.success(
                request, 'You have successfully enrolled in this module')
            return redirect('coursereg:course_detail', pk=pk)
    else:
        messages.warning(request, "You must be logged in to enrol in a course")
        return redirect('coursereg:home')


def course_unenrol(request, pk):
    if request.user.is_authenticated:
        user = request.user
        course = Group.objects.get(id=pk)
        is_enrolled = user.groups.filter(name=course.name).exists()

        if not is_enrolled:
            messages.error(request, 'You are not enrolled in this course')
        else:
            user.groups.remove(course)
            messages.success(
                request, 'You have successfully unenrolled from this course')
        return redirect('coursereg:course_detail', pk=pk)

    else:
        messages.warning(request, "You must be logged in to enrol in a course")
        return redirect('coursereg:home')


def registrations(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        registrations = Registration.objects.filter(student=student)

        return render(request, 'coursereg/registrations.html', { 'registrations': registrations, 'student': student })

    else:
        messages.warning(request, "You must be logged in to view this page")
        return redirect('coursereg:home')
