from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class TestsList(TemplateView):
    pass


class TakeTest(TemplateView):
    pass


class ResultsView(TemplateView):
    pass


class AccountView(TemplateView):
    pass