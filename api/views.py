from django.shortcuts import render
from api.serializer import Class_PeriodSerializer, CourseSerializer, Student_ClassSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from courses.models import Course

from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from student_class.models import Student_Class

from teacher.models import Teacher
from rest_framework import status


# Create your views here.
class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class Student_ClassListViews(APIView):
    def get(self, request):
        student_class = Student_Class.objects.all()
        serializer = Student_ClassSerializer(student_class, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Student_ClassSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class Student_ClassDetailView(APIView):
    def get(self, request,id):
        student_class = Student_Class.objects.get(id=id)
        serializer = Student_ClassSerializer(student_class)
        return Response(serializer.data)
    
    def put(self, request,id):
        student_class = Student_Class.objects.get(id=id)
        serializer = Student_ClassSerializer(student_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student_class = Student_Class.objects.get(id=id)
        student_class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class Class_PeriodListViews(APIView):
    def get(self, request):
        classperiod = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =Class_PeriodSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class Class_PeriodDetailView(APIView):
    def get(self, request,id):
        classperiod = Class_Period.objects.get(id=id)
        serializer = Class_PeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod= Class_Period.objects.get(id=id)
        serializer = Class_PeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = Class_Period.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)