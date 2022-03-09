from django.http import HttpResponse
from django.shortcuts import  render

def getout(request):
    return HttpResponse('COME BACK')

def getin(request):
    return HttpResponse('lost')

def lil2(request):
    return HttpResponse('lets go')




