from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_renders_home_page_template(self):
        self.c = Client()
        response = self.c.get('/lists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')




