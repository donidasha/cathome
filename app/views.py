from django.shortcuts import render
from .models import Cat, Employee
# Create your views here.

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, "cat_list.html", {'cats': cats})

def about_us(request):
    employees = Employee.objects.all()
    return render(request,"about_us.html", {'employees' : employees})