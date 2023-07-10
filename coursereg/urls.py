
from django.urls import path,include
from coursereg import views

app_name="coursereg"

urlpatterns = [
    path("", views.home, name="home"),
]
