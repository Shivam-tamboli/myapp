from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_home(request):
    return render(request, "emp/home.html",{})