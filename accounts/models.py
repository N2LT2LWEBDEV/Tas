from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,Group


class Student(models.Model):
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True, blank=True)
    course=models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.png", upload_to="profile_photos")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
