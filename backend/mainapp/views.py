from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "index.html"

class Test1(TemplateView):
    template_name="test_list.html"

class Test2(TemplateView):
    template_name="take_test.html"

class Test3(TemplateView):
    template_name="results.html"