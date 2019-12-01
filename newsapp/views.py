from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.

def index(request):
    news=News.objects.all()
    return render(request,"index.html",{'news':news})

def details(request,id):
    news=News.objects.get(id=id)
    return render(request,"details.html",{'news':news})

    
