
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
    
def profile(request, pk):
    if request.user.is_authenticated:
        student = Student.objects.get(id=pk)
        return render(request, 'accounts/profile.html', {'student': student})
    else:
        messages.warning(request, "You must be logged in to view this page")
        return redirect('coursereg:home')
