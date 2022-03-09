from multiprocessing import context
from django.shortcuts import redirect, render
from .models import AddDepartment, AddEmployee
from .forms import AddDepartmentForm,AddEmployeeForm

# Create your views here.

def home(request):
    return render(request,'esaapp/home.html')

def navbar1(request):
    return render(request,'esaapp/navbar1.html')

def adddepartment(request):
    form = AddDepartmentForm
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adddepartment')
    context =  {
        'form':form
    }
    
    return render(request,'esaapp/adddepartment.html',context)

def showdepartment(request):
    departmentData = AddDepartment.objects.all()
    context={
        'departmentData':departmentData
    }
    return render(request,'esaapp/showdepartment.html',context)

def addemployee(request):
    form = AddEmployeeForm
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addemployee')
    context={
        'form':form
    }
    return render(request,'esaapp/addemployee.html',context)

def showemployee(request):
    empData = AddEmployee.objects.all()
    context={
        'empData':empData
    }
    return render(request,'esaapp/showemployee.html',context)