from django.db import models

from student_class.models import Student_Class


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    id = models.AutoField(primary_key=True)
    code = models.PositiveSmallIntegerField(unique=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField()
    guardian_phone_number = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=100)
    class_enrolled = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='students')
    picture = models.ImageField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
