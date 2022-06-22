from calendar import month
from distutils.log import error
import email
import imp
from multiprocessing import context
from re import search
from django.shortcuts import redirect, render
# from .models import AddDepartment, AddEmployee
from .forms import AddDepartmentForm,AddEmployeeForm
from .models import SalaryReport
from .models import *
from django.contrib.auth import login, logout, authenticate

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
def registration(request):
    error = ""
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        employee_code = request.POST['empcode']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(first_name = firstname, last_name = lastname, username = email, password = password)
            EmployeeDetail.objects.create(user = user, empcode = employee_code)
            error = "no"
        except:
            error = "yes"
    return render(request,'esaapp/registration.html', locals())
def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['email']
        pa = request.POST['password']
        user = authenticate(username = u, password = pa)
        if user:
            login(request, user)
            # return redirect('home') #provided home url in the js code
            error = "no"
            
        else:
            error = "yes"
        
    return render(request,'esaapp/emp_login.html', locals())
def emp_page(request):
    details = EmployeeDetail.objects.all()
    return render(request,'esaapp/emp_page.html',{'details': details})

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