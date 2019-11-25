from django.shortcuts import render
from django.http import HttpResponse

from .models import Companies

# Create your views here.

def index(request):
    works = Companies.objects.order_by('id')[:10]
    return render(request, 'works/works_page.html', {'work_list':works})

def info_work(request, work_id):
    try:
        company = Companies.objects.get(id=work_id)
    except Question.DoesNotExist:
        raise Http404('Company does not exist')
        

    return render(request, 'works/info_work.html', {'company':company})