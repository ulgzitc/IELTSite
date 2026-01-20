from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "index.html"

class Test1(TemplateView):
    pass

class Test2(TemplateView):
    pass

class Test3(TemplateView):
    pass