from audioop import reverse
from datetime import datetime
from django.test import TestCase
from api.serializer import StudentSerializer

from student.models import Student

# Create your tests here.

class SudentListAPIViewTest(APITestCase):
    def setUp(self): 
        self.student = Student.objects.create(
            fir<yst_name="Derrick",
            last_name="Momanyi",
            email="derrickmomanyi@gmail.com",
            date_of_birth=datetime.date(2000, 9, 12),
            code=32323,  # Ensure this value is within the valid range
            gender="Male",
            country="Kenya",
            bio="Super Human",
            enrollment_date=datetime.date(2024, 1, 27),
            guardian_phone_number="0742070025",
            guardian_name="Agnes Auma",
        )
    
    def test_get_student_list(self):
        url = reverse("register/")
        response = self.client.get(url)
        students  = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)