from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    return render(request,'all.html')

def add_emp(request):
    return render(request,'add.html')

def remove_emp(request):
    return render(request,'remove.html')

def filter_emp(request):
    return render(request,'filter.html')


