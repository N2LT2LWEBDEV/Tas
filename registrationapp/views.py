from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from coursereg.models import Student, Module, Registration,Group
from .serializers import StudentSerializer, ModuleSerializer, RegistrationSerializer,CourseSerializer
from rest_framework.reverse import reverse

class ApiRoot(generics.GenericAPIView):
    """
    API homepage
    """

    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
        'students': reverse('student-list-create', request=request),
        'modules': reverse('module-list-create', request=request),
        'registrations': reverse('registration-list-create', request=request),
        'courses': reverse('course-list-create', request=request),
    })

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = CourseSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


