from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.views.generic import View
from sentry_sdk import capture_message


from .models import Companies, Worker, WorkPlace, WorkTime, Manager
from .forms import WorkFrorm, SetWorkPlace, WorkTimeForm


import logging


logger = logging.getLogger(__name__)


def index(request):
    companies = Companies.objects.order_by('id')[:10]
    return render(request, 'works/list_company.html', {'companies_list': companies, 'room_name':'1'})


def info_work(request, work_id):
    try:
        company = Companies.objects.get(id=work_id)
    except Companies.DoesNotExist:
        logger.error('Company does not exist!')
        return HttpResponseNotFound('Company does not exist')

    return render(request, 'works/detail_company.html', {'company': company, 'room_name':'2'})


def info_workers(request):
    workers = Worker.objects.order_by('id')[:10]

    return render(request, 'works/list_workers.html', {'workers': workers})


def info_worker(request, worker_id):
    try:
        worker = Worker.objects.get(id=worker_id)
    except Worker.DoesNotExist:
        return HttpResponseNotFound('Worker does not exist')

    list_work = WorkPlace.objects.filter(worker_id=worker_id, status="F")

    return render(request, 'works/detail_worker.html', {'worker': worker, 'list_work': list_work})


def info_managers(request, work_id):
    managers = Manager.objects.filter(company_id=work_id)[:10]

    return render(request, 'works/list_managers.html', {'managers': managers})


class WorkCreate(View):

    def get(self, request):
        form = WorkFrorm()
        return render(request, 'works/create_work.html', {'form': form})

    def post(self, request):
        forms = WorkFrorm(request.POST)
        if forms.is_valid():
            new_work = forms.save()
            return HttpResponse('Success create work!')


class SetWorker(View):

    def get(self, request):
        form = SetWorkPlace()
        return render(request, 'works/set_worker.html', {'form': form})

    def post(self, request):
        forms = SetWorkPlace(request.POST)
        if forms.is_valid():
            new_work = forms.save()
            return HttpResponse('Success set in work!')


class SetWorkTime(View):
    """docstring for ClassName"""

    def get(self, request, worker_id):
        form = WorkTimeForm(worker_id)
        list_work_place = WorkPlace.objects.filter(worker_id=worker_id)
        return render(request, 'works/crete_worktime.html', {'form': form, 'list_wp': list_work_place})

    def post(self, request, worker_id):
        forms = WorkTimeForm(worker_id, request.POST)
        if forms.is_valid():
            new_work = forms.save()
            return HttpResponse('Success set in work!')
        return HttpResponse('Form not valid!')
