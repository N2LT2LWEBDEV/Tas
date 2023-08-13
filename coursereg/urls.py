
from django.urls import path,include
from coursereg import views

app_name="coursereg"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("modules/", views.modules, name="module"),
    path("courses/", views.courses, name="courses"),
    path("modules/detail/<str:code>/", views.module_details, name="module_details"), 
    path("courses/detail/<int:pk>/", views.course_details, name="course_detail"), 
    path("courses/<int:pk>/enrol", views.course_enrol, name="course_enrol"), 
    path("courses/<int:pk>/unenrol", views.course_unenrol, name="course_unenrol"), 
    path("modules/<int:pk>/register/", views.module_register, name="module_register"), 
    path("modules/<int:pk>/unregister/", views.module_unregister, name="module_unregister"), 
]
