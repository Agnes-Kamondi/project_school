import datetime
from django.test import TestCase

from student.forms import StudentRegistrationForm
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


class StudentFormTest(TestCase):
    def test_student_form_valid(self):
        form_data = {
            'first_name': 'Derrick',
            'last_name' :"Momanyi",
            "email":"derrickmomanyi@gmail.com",
            "gender":"Male",
            "country":"Kenya",
            "bio":"Super Human",
            "guardian_phone_number":"0742070025",
            "guardian_name":"Agnes Auma",
        }
        form = StudentRegistrationForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_student_form_invalid(self):
        form_data ={"first_name": "Derrick","last_name": "Momanyi"}
        form = StudentRegistrationForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)