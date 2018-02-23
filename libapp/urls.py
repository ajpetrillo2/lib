'''
   Django determines which view (business logic) to use via the pattern 
   of the URL. 
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
