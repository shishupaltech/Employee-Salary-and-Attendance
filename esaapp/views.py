from calendar import month
from multiprocessing import context
from re import search
from django.shortcuts import redirect, render
from .models import AddDepartment, AddEmployee
from .forms import AddDepartmentForm,AddEmployeeForm
from .models import SalaryReport

# Create your views here.

def home(request):
    return render(request,'esaapp/home.html')
    #*******************from here******* works well
def salary_report(request):
    salary = SalaryReport.objects.all
    return render(request, 'esaapp/salary_report.html', {'salary': salary})
#     #*****************to here added 3/18*********
    #from here
# def salary_report(request):
#     salary = SalaryReport.objects
#     if request.method == "post":
#         datef = request.post['datef']
#         datet = request.post['datet']
#         try:
#             t = SalaryReport.objects.filter(date__lte=datet, date__gte=datef)
#         except:
#             t = None
#         return render(request, 'esaapp/salary_report.html', {'t':t})
#     else:
#         return render(request, 'esaapp/salary_report.html')
#         #  return redirect('addepartment')
  #to here 3/20
  #from here*****for search bar option
def search_salary(request):
    sea = request.GET['search']
    sal = SalaryReport.objects.filter(month = sea)
    return render(request, 'esaapp/search_salary.html', {'sal': sal})
  #to here added 3/20

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