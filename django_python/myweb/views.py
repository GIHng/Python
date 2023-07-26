from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # return HttpResponse("<h1>Hello Django</h1>")
    return render(request, 'index.html')
def hello(request):
    return HttpResponse("<h3>Hello</h3>")