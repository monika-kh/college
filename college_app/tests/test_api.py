from django.urls import reverse
from rest_framework.test import APITestCase

from college_app.models import College, Student
from college_app.serializers import CollegeSerializer, StudentSerializer


class College_Test(APITestCase):  # without setup method
    def test_college(self):
        self.data = {"college_name": "SGSITS", "city": "Indore", "state": "MP"}

        res = self.client.post(reverse("college1"), self.data, format="json")
        self.assertEqual(res.status_code, 201)

        res2 = self.client.get(reverse("college1"))
        self.assertEqual(res2.status_code, 200)

        res3 = self.client.get(reverse("college2", kwargs={"pk": "1"}), self.data)
        self.assertEqual(res3.status_code, 200)

        self.data1 = {"college_name": "LNCT", "city": "Bhopal", "state": "UP"}
        url = reverse('college2', args=[res3.data['id']])
        res4 = self.client.put(url, data=self.data1)
        breakpoint()

        res5 = self.client.delete(reverse("college2", kwargs={"pk": 1}))
        self.assertEqual(res5.status_code, 204)


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
        res3 = self.client.get(reverse("student2", args=[self.student.id]))
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

    def test_update_student(self):
        res4 = self.client.put(reverse("student2", args=[self.student.id]), self.data)
        self.assertEqual(res4.status_code, 200)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Mike", last_name="Tyson", branch="ex", dob="1993-05-11"
        )

    def test_delete_student(self):
        res5 = self.client.delete("/student/1/", args=[self.student.id])
        self.assertEqual(res5.status_code, 204)
