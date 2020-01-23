from django.test import SimpleTestCase
from django.urls import reverse, resolve

from college_app.views import CollegeView
from rest_framework.test import APITestCase

from college_app import views


class TestCollegeUrls(SimpleTestCase):
    def test_college_url(self):
        url = reverse("college1")
        self.assertEqual(resolve(url).func.cls, views.CollegeView)


class TestStudentUrls(SimpleTestCase):
    def test_college_url_pk(self):
        # url = reverse("student1")
        self.assertEqual(resolve(reverse("student1")).func.cls, views.StudentView)




