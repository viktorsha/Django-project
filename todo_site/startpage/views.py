from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def startpage(request):
    return render(request, "startpage.html")

# Create your views here.
