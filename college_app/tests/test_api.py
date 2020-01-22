from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from college_app.models import College, Student
from college_app.serializers import CollegeSerializer, StudentSerializer


class College_Test(APITestCase):  # without setup method
    def test_college(self):
        data = {"college_name": "SGSITS", "city": "Indore", "state": "MP"}

        # res1 = self.client.post('/college/',data, format="json")        # url from browser
        res = self.client.post(reverse("college"), data, format="json")
        self.assertEqual(res.status_code, 201)

        res2 = self.client.get(reverse("college"))
        self.assertEqual(res2.status_code, 200)

        res3 = self.client.get(reverse("college", kwargs={"pk": "1"}), data)
        self.assertEqual(res3.status_code, 200)

        res4 = self.client.delete(reverse("college", kwargs={"pk": 1}))
        self.assertEqual(res4.status_code, 204)

        data1 = {"college_name": "LNCT", "city": "Bhopal", "state": "UP"}
        res5 = self.client.put("college/1/", data1, format="json")
        # res5 = self.client.put(reverse('college', args=[{'pk':1}]), data)
        # res5 = self.client.put(reverse('college', kwargs={'pk': '1'}), data1)
        # res5 = self.client.put("college/1/", data1={"college_name": "gsits", "city": "ujjain", "state": "up"}, format="json")
        breakpoint()


# class Student_Test(APITestCase):
# using setup method
class CreateStudentTest(APITestCase):
    def setUp(self):
        self.student = {
            "first_name": "Mike",
            "last_name": "Tyson",
            "branch": "ex",
            "dob": "1993-05-19",
        }

    def test_create_student(self):
        res1 = self.client.post("/student/", self.student)
        self.assertEqual(res1.status_code, 201)


class GetStudentTest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Mike", last_name="Tyson", branch="ex", dob="1993-05-19"
        )

    def test_get_student(self):
        res2 = self.client.get("/student/")
        self.assertEqual(res2.status_code, 200)

    def test_get_pk_student(self):
        res3 = self.client.get(reverse("student", args=[self.student.id]))
        self.assertEqual(res3.status_code, 200)


class PutStudentTest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Mike", last_name="Tyson", branch="ex", dob="1993-05-11"
        )
        self.data = StudentSerializer(self.student).data
        self.data.update(
            {
                "first_name": "Shivam",
                "last_name": "Singh",
                "branch": "cs",
                "dob": "1991-05-19",
            }
        )

    def test_update_student(self,):
        res4 = self.client.put(reverse("student", args=[self.student.id]), self.data)
        self.assertEqual(res4.status_code, 200)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Mike", last_name="Tyson", branch="ex", dob="1993-05-11"
        )

    def test_delete_student(self):
        res5 = self.client.delete("/student/1/", args=[self.student.id])
        self.assertEqual(res5.status_code, 204)
