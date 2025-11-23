from django.shortcuts import render
from .models import Cat, Employee
from .forms import ApplicationForm, CatForm
# Create your views here.

def cat_list(request):
    cats = Cat.objects.all()
    return render(request, "cat_list.html", {'cats': cats})

def about_us(request):
    employees = Employee.objects.all()
    return render(request,"about_us.html", {'employees' : employees})

def how_to_help(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()
        
    return render(request, "how_to_help.html", {'form' : form})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CatForm()
    return render(request, "cat_detail.html", {'cat': cat, 'form' : form})