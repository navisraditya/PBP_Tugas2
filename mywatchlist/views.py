from multiprocessing import context
from django.shortcuts import render
from mywatchlist.models import watchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = watchlist.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'nama': 'Muhammad Navis Raditya Riayatsyah',
        'npm': '2106717291'
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")