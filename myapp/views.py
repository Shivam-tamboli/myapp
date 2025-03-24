from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
    date = datetime.now()
    # sending data dynamically to the client.
    isActive=True
    name="Shivam Tamboli"
    list_of_program=[
        'WAP to print even and odd numbers',
        'WAP to print prime numbers'
    ]
    
    Student={
        'Student_name':'Satyam',
        'Student_college':'xyz',
        'Student_city':'Indore'
    }
    
    # how to share this data on the template.
    data={
        "date":date,
        "isActive":isActive,
        "name":name,
        "list_of_program":list_of_program,
        "Student":Student
        
    }
    print("test function is called from view")
    # return HttpResponse("<h1>Hello this is index page</h1>" + str(date)) 
    return render(request,"home.html",data)#we will use third paramater of render to share the data with the template.

def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def part(request):
    print("This is from part function")
    return HttpResponse("<h1>This is from part side</h1>")

def services(request):
    print("Services are running")
    # return HttpResponse("<h1>This is from services side</h1>").
    return render(request,"services.html",{})