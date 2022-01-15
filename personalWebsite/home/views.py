from django.shortcuts import render
# create home view and import http response
from django.http import HttpResponse

# make home view
def home(request):
    return HttpResponse('<h1>Hello World!</h1>')
    