from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "index.html"

class Test1(TemplateView):
    template_name = "index2.html"

class Test2(TemplateView):
    template_name = "index3.html"

class Test3(TemplateView):
    pass