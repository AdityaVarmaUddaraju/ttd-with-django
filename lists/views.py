from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item, List
# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html')

def lists_page(request, id):
    list_ = List.objects.get(id=id)
    return render(request, 'lists/list.html', {
        'list':list_
    })

def new_list(request):
    list_ = List.objects.create()
    print(list_.id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, id):
    list_ = List.objects.get(id=id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')