# import self
from django.urls import reverse

from college_app.models import College, Student
from django.test import TestCase

from rest_framework.test import APIClient, APITestCase


class College_Test(APITestCase):
    def test_college(self):
        #client = APIClient

        # url_int = reverse('college_int/')

        data = {"college_name": "SGSITS",
                "city": "Indore",
                "state": "MP"
                }
        path = reverse('/college/')
        breakpoint()


    # res_post = self.client.post(url, data, format="json")
        # self.assertEqual(res_post.status_code,201)
        #
        # res_get = self.client.get(url,data,format="json")
        # self.assertEqual(res_get.status_code,200)

        #res_put

        # res_put





# url = reverse('account-list')
# data = {'name': 'DabApps'}
# response = self.client.post(url, data, format='json')
# self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# self.assertEqual(Account.objects.count(), 1)
# self.assertEqual(Account.objects.get().name, 'DabApps')
