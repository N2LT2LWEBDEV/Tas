
from django.urls import path,include
from coursereg import views

app_name="coursereg"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("modules/", views.modules, name="module"),
    path("modules/detail/<str:code>/", views.module_details, name="home"), 
]
