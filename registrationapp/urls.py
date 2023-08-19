"""
URL configuration for registrationapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import reset_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("coursereg.urls")),
    path("accounts/", include("accounts.urls")),    
    path('reset_password/', reset_password, name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/', views.ApiRoot.as_view(), name='api-root'),
    path('api/students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('api/modules/', views.ModuleListCreateView.as_view(), name='module-list-create'),
    path('api/registrations/', views.RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('api/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)