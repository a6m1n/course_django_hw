from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import View

from .models import Companies, Worker, Work_place, Fineshed_work, Manager
from .forms import WorkFrorm, SetWorkPlace
# Create your views here.


def index(request):
    works = Companies.objects.order_by('id')[:10]
    return render(request, 'works/works_page.html', {'work_list': works})


def info_work(request, work_id):
    try:
        company = Companies.objects.get(id=work_id)
    except Companies.DoesNotExist:
        raise Http404('Company does not exist')

    return render(request, 'works/info_work.html', {'company': company})


def info_workers(request):
    workers = Worker.objects.order_by('id')[:10]

    return render(request, 'works/workers.html', {'workers': workers})


def info_worker(request, worker_id):
    try:
        worker = Worker.objects.get(id=worker_id)
    except Worker.DoesNotExist:
        raise Http404('Worker does not exist')

    list_work = Fineshed_work.objects.filter(worker_id=worker_id)

    return render(request, 'works/info_worker.html', {'worker': worker, 'list_work': list_work})


def info_managers(request, work_id):
    managers = Manager.objects.filter(company_id=work_id)[:10]

    return render(request, 'works/list_managers.html', {'managers': managers})


class WorkCreate(View):
    
    def get(self, request):
        form = WorkFrorm()
        return render(request, 'works/work_create.html', {'form': form})

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