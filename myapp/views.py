from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
    date = datetime.now()
    print("test function is called from view")
    # return HttpResponse("<h1>Hello this is index page</h1>" + str(date)) 
    return render(request,"home.html",{})

def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def part(request):
    print("This is from part function")
    return HttpResponse("<h1>This is from part side</h1>")

def services(request):
    print("Services are running")
    # return HttpResponse("<h1>This is from services side</h1>")
    return render(request,"services.html",{})