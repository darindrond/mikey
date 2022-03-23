from django.http import HttpResponse
from django.shortcuts import render

from lil.models import student


def login(request):
    return render(request,'index.html')

def logout(request):
    return HttpResponse('welcome to stupid earth')

def lil1(request):
    return render(request,'index.html')



def register(request):
    if request.method == "GET":
        return render(request,"insert.html")
    else:
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        DOB = request.POST.get("dob")
        Mark = request.POST.get("mark")

    student.objects.create(name=name, username=username, password=password, DOB=DOB, Mark=Mark)
    return render(request,"insert.html")

def display(request):
    ob=student.objects.all()
    return render(request,"display.html",{"ob":ob})
