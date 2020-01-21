# import self
from django.urls import reverse


from django.test import TestCase

from rest_framework.test import APIClient, APITestCase

from college_app.serializers import CollegeSerializer

from college_app.models import College


class Create_College_Test(APITestCase):
#     def setUp(self):
#         self.data = College.objects.create(college_name= "SGSITS",
#                                            city= "Indore",
#                                            state= "MP")
#         self.data1 = CollegeSerializer(self.data).data
#         breakpoint()
#
#     def test_create_college(self):
#         res = self.client.post(reverse("college"),self.data)
#         self.assertEqual(res.status_code,201)



    def test_college(self):
    #client = APIClient

        data = {"college_name": "SGSITS",
                "city": "Indore",
                "state": "MP"
                }


        #url = reverse('college', kwargs={'pk': '1'})

        res1 = self.client.post('/college/',data, format="json")
        #res = self.client.post("/college/", data, format="json")         # url from browser
        self.assertEqual(res1.status_code,201)

        res2 = self.client.get(reverse("college"))
        self.assertEqual(res2.status_code,200)

        #res_get_pk = self.client.get(reverse("college", args=[College.pk]))
        res3 = self.client.get(reverse('college', kwargs={'pk': '1'}),data)
        self.assertEqual(res3.status_code,200)


        res4 = self.client.delete(reverse('college', kwargs={'pk':1}))
        self.assertEqual(res4.status_code,200)


        # data1 = {
        #     "college_name": "LNCT",
        #     "city": "Bhopal",
        #     "state": "MP"
        # }
        # res4 = self.client.put(reverse("college",kwargs={'pk':'1'}), data1 ,format="json")
class TestEndPoint(APITestCase):
        def setUp(self):
            self.college = College.objects.create(college_name="Vits",city="indore", state="mp")
            self.data = CollegeSerializer(self.college).data
            self.data.update({"college_name":"gsits","city":"ujjain", "state":"up"})

        def test_put_college(self):
            response = self.client.put(reverse("college", args=[self.college.id]), self.data)
            breakpoint()








    # data1 = {"college_name": "LNCT",
    #          "city": "Bhopal",
    #          "state": "MP"
    #          }
    # res_put = self.client.put(url, data1, format="json")
    # breakpoint()