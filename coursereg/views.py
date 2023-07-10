from django.shortcuts import render


def home(request):
    return render(request, "coursereg/home.html", {"title": "Home page"})

