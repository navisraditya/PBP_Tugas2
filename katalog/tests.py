from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_show_catalog_url(self):
        url = reverse('katalog:show_katalog')
        self.assertEqual(resolve(url).func, show_katalog)