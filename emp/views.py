from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):
    return render(request, "emp/home.html",{})

def add_emp(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_departent = request.POST.get("emp_departent")

        e = Emp()
        e.name = emp_name
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_departent
        e.working = bool(emp_working)  # handles True/False
        
        e.save()

        return redirect("/emp/home/")

    return render(request, "emp/add_emp.html", {})


