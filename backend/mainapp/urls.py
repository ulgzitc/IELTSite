from django.urls import path
from .views import *


urlpatterns = [
    path('', TestView.as_view()),
    path('test1/', Test1.as_view()),
    path('test2/', Test2.as_view()),
    path('test3/', Test3.as_view()),
]

