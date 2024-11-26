from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def shubam(request):
    return HttpResponse("<h1><marquee>shubam shinde is the captain of Telugutitans</marquee></h1>")

