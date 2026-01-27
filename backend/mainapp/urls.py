from django.urls import path
from .views import *


urlpatterns = [
    path('', Test.as_view(), name='home'),
#    path('testlist/', TestList.as_view(), name='testlist'),
#    path('taketest/', TakeTest.as_view(), name='taketest'),
#    path('results/', ResultsView.as_view(), name='testresults'),
#    path('account/', ProfileView.as_view(), name='profile'),
#    path('test/', Test.as_view(), name='test'),
]

