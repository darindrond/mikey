from django.shortcuts import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse("welcome to my world")

def logout(request):
    return HttpResponse("welcome to my hell")

def robert(request):
    return HttpResponse("home page")
