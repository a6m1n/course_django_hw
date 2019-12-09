from django.urls import reverse
from django.test import TestCase


from works import views

from works.tests.fixture.create_models import Create


           

class TestHomePage(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_workers(self):
        response = self.client.get(reverse("info_workers"))
        self.assertEqual(response.status_code, 200)

    def test_info_work(self):
        Create().create_company()
        response = self.client.get(reverse("info_work", kwargs={'work_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['company'])


    def test_info_worker(self):
        Create().create_worker()
        response = self.client.get(reverse("info_worker", kwargs={'worker_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['worker'])


