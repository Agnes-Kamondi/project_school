from datetime import datetime
from django.db import models
from courses.models import Course

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
    courses = models.ManyToManyField(Course)
    enrollment_date = models.DateField()
    guardian_phone_number = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=100)
    class_enrolled = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='students')
    picture = models.ImageField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def check_code(self):
        return f"{self.code}"
    
    def get_age(self):
        if self.date_of_birth:
            today = datetime.now()
            age = today.year - self.date_of_birth.year
            
            if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
                age -= 1
            
            return age
        return None 