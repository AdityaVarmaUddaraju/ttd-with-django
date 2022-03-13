from unicodedata import name
from django.urls import path

from .views import home_page, lists_page, new_list, add_item

app_name = 'lists'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('<int:id>/', lists_page, name="lists_page"),
    path('<int:id>/add_item', add_item, name="add_item"),
    path('new/', new_list, name='new_list'),
]
