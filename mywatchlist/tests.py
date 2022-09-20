from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_watchlist, show_xml, show_json

# Create your tests here.
class TestUrls(SimpleTestCase):
    
    def test_show_mywatchlist_url(self):
        url = reverse('mywatchlist:show_watchlist')
        self.assertEquals(resolve(url).func, show_watchlist)

    def test_show_mywatchlistxml_url(self):
        url = reverse('mywatchlist:show_xml')
        self.assertEquals(resolve(url).func, show_xml)

    def test_show_mywatchlistjson_url(self):
        url = reverse('mywatchlist:show_json')
        self.assertEquals(resolve(url).func, show_json)

# Source: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2