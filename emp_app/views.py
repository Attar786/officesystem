from django.shortcuts import render
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
    return render(request,'add.html')

def remove_emp(request):
    return render(request,'remove.html')

def filter_emp(request):
    return render(request,'filter.html')


