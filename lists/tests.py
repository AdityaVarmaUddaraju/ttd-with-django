from urllib import response
from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest

from .models import Item, List

from .views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_renders_home_page_template(self):
        self.c = Client()
        response = self.c.get('/lists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')


class ListViewTest(TestCase):
    def test_display_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='item1', list=list_)
        Item.objects.create(text='item2', list=list_)

        response = self.client.get('/lists/only-list/')

        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')   

    def test_uses_list_template(self):
        response = self.client.get('/lists/only-list/')
        self.assertTemplateUsed(response, 'lists/list.html')     



class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()
        
        item1 = Item()
        item1.text = 'first item'
        item1.list = list_
        item1.save()

        item2 = Item()
        item2.text = "second item"
        item2.list = list_
        item2.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        total_items = Item.objects.all()
        self.assertEqual(total_items.count(), 2)

        first_item = total_items[0]
        second_item = total_items[1]

        self.assertEqual(first_item.text, 'first item')
        self.assertEqual(first_item.list, list_)
        self.assertEqual(second_item.text, 'second item')
        self.assertEqual(second_item.list, list_)

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new/', data={'item_text': 'new item'})
        self.assertEqual(Item.objects.count(),1)
        item = Item.objects.first()
        self.assertEqual(item.text, 'new item')

    def test_redirects_after_post(self):
        response = self.client.post('/lists/new/', data={'item_text': 'new_item'})
        self.assertRedirects(response, '/lists/only-list/')



