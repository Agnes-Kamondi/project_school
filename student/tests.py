import datetime
from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name="Derrick",
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
        self.student.save()  # Save the instance to the database

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

    def test_check_code(self):
        self.assertEqual(self.student.check_code(), "32323")  # Update expected value

    def test_get_age(self):
        age = self.student.get_age()
        self.assertIsInstance(age, int)
        self.assertGreaterEqual(age, 0)

    def test_get_age_no_date_of_birth(self):
        student_without_dob = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            date_of_birth= datetime.date(2000, 9, 12),
            code=12345,  # Valid small integer
            gender="Male",
            country="USA",
            bio="Just a student.",
            enrollment_date=datetime.date(2024, 1, 27),
            guardian_phone_number="1234567890",
            guardian_name="Jane Doe"
        )
        self.assertIsNone(student_without_dob.get_age())