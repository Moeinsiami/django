from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, world')

def mamad(request):
    return HttpResponse('hello, mamad')

def javad(request):
    return HttpResponse('hello, javad')


