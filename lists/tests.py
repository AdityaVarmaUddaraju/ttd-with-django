from django.test import TestCase
from django.urls import resolve
from .views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)
