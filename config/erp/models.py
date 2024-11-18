from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(5)
    ])
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name


