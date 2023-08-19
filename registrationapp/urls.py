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
from django.urls import path
from .views import StudentListCreateView, ModuleListCreateView, RegistrationListCreateView,ApiRoot,CourseListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("coursereg.urls")),
    path("accounts/", include("accounts.urls")),
    path('api/', ApiRoot.as_view(), name='api-root'),
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/modules/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('api/registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('api/courses/', CourseListCreateView.as_view(), name='course-list-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)