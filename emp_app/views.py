from django.shortcuts import render ,HttpResponse
from datetime import datetime
from .models import Employee, Role, Department
# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    employees =  Employee.objects.all()
    context = {
        'employees' : employees
        }
    print(context)
    return render(request,'all.html', context)


def add_emp(request):
    if request.method=="POST":
        firstname = (request.POST['firstname'])
        lastname = (request.POST['lastname'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        newemps = Employee(firstname = firstname, lastname= lastname, salary= salary, bonus= bonus, phone=phone , dept_id= dept, role_id= role, hire_date=datetime.now())
        newemps.save()
        
        return HttpResponse('employ added successfully')
    elif request.method=="GET":
        return render(request,'add.html')
    else:
        return HttpResponse("oopps!! Employee has not been register")

def remove_emp(request):
    return render(request,'remove.html')

def filter_emp(request):
    return render(request,'filter.html')


