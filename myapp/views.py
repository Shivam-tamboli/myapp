from django.http import HttpResponse
from datetime import datetime

def index(request):
    date = datetime.now()
    print("test function is called from view")
    return HttpResponse("<h1>Hello this is index page</h1>" + str(date)) 

def about(request):
    return HttpResponse("<h1>This is about page</h1>")

def part(request):
    print("This is from part function")
    return HttpResponse("<h1>This is from part side</h1>")

def services(request):
    print("Services are running")
    return HttpResponse("<h1>This is from services side</h1>")