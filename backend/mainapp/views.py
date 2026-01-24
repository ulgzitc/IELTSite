from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class TestsList(TemplateView):
    template_name = "test_list.html"


class TakeTest(TemplateView):
    template_name = 'take_test.html'


class ResultsView(TemplateView):
    template_name = 'results.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'