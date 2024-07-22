from django.db import models
from courses.models import Course
from student_class.models import Student_Class


class Class_Period(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='student_class')
    student_class = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='course')
    day_of_week = models.CharField(max_length=30)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.name
