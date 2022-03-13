from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item, List
# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html')

def lists_page(request):
    item_list = Item.objects.all()
    return render(request, 'lists/list.html', {
        'item_list':item_list
    })

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/only-list/')