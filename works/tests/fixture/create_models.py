from django.utils import timezone

from works.models import Company, Manager, Work, Worker, WorkTime


class Create:
    """docstring for Create"""

    def create_company(self):
        return Company.objects.create(
            company_name="Reebok",
            pub_date=timezone.now()
        )

    def create_manager(self):
        company = self.create_company()
        return Manager.objects.create(
            company=company,
            name="Test Person",
        )

    def create_worker(self):
        return Worker.objects.create(
            first_name="test f_name",
            last_name="test l_name"
        )

    def create_work(self):
        company = self.create_company()
        return Work.objects.create(
            description='Test work',
            company=company
        )

    def create_worktime(self):
        return WorkTime.objects.create(
            date_start=timezone.now()
        )
