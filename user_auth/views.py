from django.shortcuts import render

from django.utils import formats
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.

def index(request):
    context = _("Hello. This is auth app.")
    # return render(request, "user_auth/index.html", {"context":_("Welcome to my site.")})
    return render(request, "user_auth/index.html", {"context":context})
