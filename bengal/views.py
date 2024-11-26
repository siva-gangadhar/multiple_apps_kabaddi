from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def manindher(request):
    return HttpResponse("<h1><marquee>Maninder Singh is the captain of Telugutitans</marquee></h1>")
