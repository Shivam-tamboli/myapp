from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):
    return render(request, "emp/home.html",{})

def add_emp(request):
    if request.method == "POST":
     
        #fetch data.
        emp_name=request.POST.get(emp_name)
        emp_id=request.POST.get(emp_id)
        emp_phone=request.POST.get(emp_phone)
        emp_address=request.POST.get(emp_address)
        emp_working=request.POST.get(emp_working)
        emp_departent=request.POST.get(emp_departent)
        
        
        #create models object to set the data
        
        #create constructor
        e=Emp()
        
        e.name=emp_name
        e.id=emp_id
        e.phone=emp_phone
        e.address=emp_address
       # e.working=emp_working
        e.department=emp_departent
        #if nothing is filled it will be false.
        if emp_working is None:
            e.working=False
            #if something is filled then true.
        else:
            e.working=True
        
        # -------object is ready.---------
        
        
        #save the object.
        e.save()
        
        return redirect("/emp/home/")
        
    return render(request, "emp/add_emp.html",{})

