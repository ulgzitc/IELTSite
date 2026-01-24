from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView

class HomeView(TemplateView):
    template_name = "index.html"


class TestList(TemplateView):
    template_name = "test_list.html"


class TakeTest(TemplateView):
    template_name = 'take_test.html'


class ResultsView(TemplateView):
    template_name = 'results.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'