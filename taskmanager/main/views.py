from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"main/index.html")

def about(request):
    return HttpResponse("<h4>About us<h4>")