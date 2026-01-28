from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import *

class Test(ListView):
    model = Test
    template_name = 'test.html'
    context_object_name = "objects"
