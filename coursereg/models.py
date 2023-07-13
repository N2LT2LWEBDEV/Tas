
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,Group
from accounts.models import Student


class Module(models.Model):
    module_name=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    credit=models.IntegerField(default=15)
    module_desc=models.TextField()
    category=models.CharField(max_length=255, default='Compulsory')
    availability=models.BooleanField(default=True)
    courses=models.ManyToManyField(Group, related_name="modules") 

    def __str__(self):
        return self.module_name
    
    @property
    def registrations(self):
        return [registration.student for registration in Registration.objects.filter(module_registered=self)]

class Registration(models.Model):
    module_registered = models.ForeignKey(Module, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student ID: {self.student.user.username} registered for: {self.module_registered.module_name}"

    