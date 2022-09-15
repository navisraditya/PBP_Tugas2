from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

# Create your tests here.
class TestUrls(SimpleTestCase):
    
    def test_show_catalog_url(self):
        url = reverse('katalog:show_katalog')
        self.assertEqual(resolve(url).func, show_katalog)

# Source: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2