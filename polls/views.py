from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello! world, i am at the index of siteporject')

# Create your views here.
