from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text = request.POST['item_text'])
        return redirect('/lists/only-list/')
    return render(request, 'lists/home.html')

def lists_page(request):
    item_list = Item.objects.all()
    return render(request, 'lists/list.html', {
        'item_list':item_list
    })