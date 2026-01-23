from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('testslist/', TestsList.as_view(), name='testslist'),
    path('taketest/', TakeTest.as_view(), name='taketest'),
    path('results/', ResultsView.as_view(), name='testresults'),
    path('account/', AccountView.as_view(), name='account'),
]

