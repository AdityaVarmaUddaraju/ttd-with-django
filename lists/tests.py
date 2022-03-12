from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest

from .models import Item

from .views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_renders_home_page_template(self):
        self.c = Client()
        response = self.c.get('/lists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_add_item_to_db_on_post(self):
        self.client.post('/lists/',data={'item_text': 'a new list item'})
        self.assertEqual(Item.objects.count(), 1)
        item = Item.objects.first()
        self.assertEqual(item.text, 'a new list item')

    def test_redirect_after_post(self):
        response = self.client.post('/lists/',data={'item_text': 'a new list item'})
        self.assertEqual(response.status_code, 302)
    
    def test_multiple_items_in_list(self):
        Item.objects.create(text='item1')
        Item.objects.create(text='item2')

        response = self.client.get('/lists/')

        self.assertIn('1. item1', response.content.decode())
        self.assertIn('2. item2', response.content.decode())


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        item1 = Item()
        item1.text = 'first item'
        item1.save()

        item2 = Item()
        item2.text = "second item"
        item2.save()

        total_items = Item.objects.all()
        self.assertEqual(total_items.count(), 2)

        first_item = total_items[0]
        second_item = total_items[1]

        self.assertEqual(first_item.text, 'first item')
        self.assertEqual(second_item.text, 'second item')



