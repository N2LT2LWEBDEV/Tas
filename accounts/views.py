
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from .models import Student


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
