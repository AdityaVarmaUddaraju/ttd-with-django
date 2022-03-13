from unicodedata import name
from django.urls import path

from .views import home_page, lists_page, new_list

app_name = 'lists'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('only-list/', lists_page, name='lists_page'),
    path('new/', new_list, name='new_list'),
]
