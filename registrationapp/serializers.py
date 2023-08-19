from rest_framework import serializers
from django.contrib.auth.models import Group
from coursereg.models import Student, Module, Registration

class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['module_name', 'code']

class CourseSerializer(serializers.ModelSerializer):
    modules = CourseModuleSerializer(many=True, source='modules_set', read_only=True)
    class Meta:
        model = Group
        fields = ['name', 'modules']


class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Student
        fields = ['address', 'city', 'country', 'date_of_birth', 'course', 'user']

class ModuleSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Module
        fields = ['module_name', 'code', 'credit', 'module_desc', 'category', 'availability', 'courses']

class RegistrationSerializer(serializers.ModelSerializer):
    module_registered_name = serializers.CharField(source='module_registered.module_name')
    student_name = serializers.CharField(source='student.user.username')
    class Meta:
        model = Registration
        fields = ['module_registered_name', 'student_name', 'reg_date']
