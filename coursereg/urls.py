
from django.urls import path,include
from coursereg import views

app_name="coursereg"

urlpatterns = [
    path("", views.home, name="home"),
    path("modules/", views.modules, name="home"),
    path("modules/detail/<str:code>/", views.module_details, name="home"), 
]
