from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def index(request):
    return HttpResponse("hello!")


def blog(request,name):
    data = Blog.objects.get(pk=1)
    content = data
    return render(request,name+".html",{"blog":content})