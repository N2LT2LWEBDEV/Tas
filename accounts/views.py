
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm


def profile(request):
    return render(request, 'accounts/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        student_form = ProfileUpdateForm(request.POST)
        if form.is_valid() and student_form.is_valid():
            user = form.save()

            existing_student_record = Student.objects.get(id=user.id)
            existing_student_record.address = student_form.cleaned_data['address']
            existing_student_record.city = student_form.cleaned_data['city']
            existing_student_record.country = student_form.cleaned_data['country']
            existing_student_record.date_of_birth = student_form.cleaned_data['date_of_birth']

            if 'profile_pic' in request.FILES:
                existing_student_record.profile_pic = request.FILES['profile_pic']
            
            existing_student_record.save()
            messages.success(
                request, f'Your account has been created! Now you can login!')
            return redirect('accounts:login')
        else:
            messages.warning(request, f'Unable to create account!')
        return render(request, 'accounts/register.html', {'form': form, 'student_form': student_form})
    else:
        form = UserRegisterForm()
        student_form = ProfileUpdateForm()
        return render(request, 'accounts/register.html', {'form': form, 'student_form': student_form})

@login_required
def profile(request, pk):
    if request.user.is_authenticated:
        student = Student.objects.get(id=pk)
        course = ""
        if len(student.user.groups.filter()) > 0:
            course = student.user.groups.filter()[0]
        return render(request, 'accounts/profile.html', {'student': student, 'course': course})
    else:
        messages.warning(request, "You must be logged in to view this page")
        return redirect('coursereg:home')

@login_required
def update_profile(request, pk):
    if request.user.is_authenticated:
        student = Student.objects.get(id = pk)
        student_form = ProfileUpdateForm(request.POST or None, instance=student)

        if request.method == 'POST':
            if student_form.is_valid():
                student.address = student_form.cleaned_data['address']
                student.city = student_form.cleaned_data['city']
                student.country = student_form.cleaned_data['country']
                student.date_of_birth = student_form.cleaned_data['date_of_birth']

                if 'profile_pic' in request.FILES:
                    student.profile_pic = request.FILES['profile_pic']
                
                student.save()
                messages.success(request, f'Your profile has been updated!')
                return redirect('accounts:profile', pk=pk)
            else:
                messages.warning(request, f'Unable to update profile!')
            return render(request, 'accounts/update_profile.html', {'student_form': student_form})
        else:
            return render(request, 'accounts/update_profile.html', { 'student_form': student_form })
    else:
        messages.warning(request, "You must be logged in to view this page")
        return redirect('coursereg:home')

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name='accounts/password_reset_email.html'
            )
            messages.success(request, 'Password reset email has been sent.')
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/reset_password.html', {'form': form})
