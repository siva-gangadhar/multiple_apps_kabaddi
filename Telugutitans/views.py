from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pavan(request):
    return HttpResponse("<h1><marquee>pavan kumar sharawath is the captain of Telugutitans</marquee></h1>")
