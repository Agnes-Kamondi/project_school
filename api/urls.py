
from django.urls import path
from .views import Class_PeriodListViews, CourseListViews, Student_ClassListViews, StudentListViews , TeacherListViews


urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Courses/",CourseListViews.as_view(),name = "course_list_view"),
    path("Student_Class/",Student_ClassListViews.as_view(),name = "student_class_list_view"),
    path("Class_Period/",Class_PeriodListViews.as_view(),name = "class_period_list_view")

]