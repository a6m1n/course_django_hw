from django.test import TestCase
from django.utils import timezone

from works.models import Companies, Manager, Work, Worker
from works.tests.fixture.create_models import Create 

class CompanieModelsTest(TestCase):


    def test_create_company(self):
        company = Create().create_company()
        self.assertTrue(company.company_name)


    def test_create_manager(self):
        manager = Create().create_manager()
        self.assertTrue(manager.company.id)

    def test_create_work(self):
        work = Create().create_work()
        self.assertTrue(work.company.id)

    def test_create_worker(self):
        worker = Create().create_worker()
        self.assertTrue(worker.first_name)

    def test_create_worktime(self):
        work_time = Create().create_worktime()
        work_time.set_date_end()
        self.assertTrue(work_time.status)
