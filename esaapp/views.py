from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import AddDepartment, AddEmployee, Attendance
from .forms import AddDepartmentForm,AddEmployeeForm
from django.core.files.storage import FileSystemStorage
# from .models import Post

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'esaapp/home.html')

def navbar1(request):
    return render(request,'esaapp/navbar1.html')

# def adddepartment(request):
#     form = AddDepartmentForm
#     if request.method == 'POST':
#         form = AddDepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adddepartment')
#     context =  {
#         'form':form
#     }
    
#     return render(request,'esaapp/adddepartment.html',context)
def adddepartment(request):
    if request.method == 'POST':
        if request.POST.get('department') and request.POST.get('basicpay') and request.POST.get('travelallowance') and request.POST.get('medicalallowance') and request.POST.get('washingallowance'):
            print(request.POST.get('department'), request.POST.get('basicpay') , request.POST.get('travelallowance') , request.POST.get('medicalallowance') , request.POST.get('washingallowance'))
            post = AddDepartment()
            post.departmentName=request.POST.get('department')
            post.basicPay=request.POST.get('basicpay')
            post.travelAllowance=request.POST.get('travelallowance')
            post.medicalAllowance=request.POST.get('medicalallowance')
            post.washingAllowance=request.POST.get('washingallowance')
            post.save()
            messages.info(request, 'New Department Recorde Added Successfully')
            return redirect('adddepartment')
    return render(request,'esaapp/adddepartment.html')

def showdepartment(request):
    departmentData = AddDepartment.objects.all()
    context={
        'departmentData':departmentData
    }
    return render(request,'esaapp/showdepartment.html',context)

def updateDepartment(request,pk):
    postobj= get_object_or_404(AddDepartment, pk=pk)
    if request.method == 'POST':
        if request.POST.get('department') and request.POST.get('basicpay') and request.POST.get('travelallowance') and request.POST.get('medicalallowance') and request.POST.get('washingallowance'):
            AddDepartment.objects.filter(id=pk).update(
                departmentName=request.POST.get('department'),
                basicPay = request.POST.get('basicpay'),
                travelAllowance = request.POST.get('travelallowance'),
                medicalAllowance = request.POST.get('medicalallowance'),
                washingAllowance = request.POST.get('washingallowance')
            )
            messages.info(request, 'One Employee Recorde Updated Successfully')
            return redirect('showdepartment')
    context = {
            'postobj':postobj
        }
    return render(request,'esaapp/updatedepartment.html',context)
        
def deleteDepartment(request,pk):
    deleteDepartment = AddDepartment.objects.get(id=pk)
    deleteDepartment.delete()
    messages.info(request, 'One Employee Recorde Deleted Successfully')
    return redirect("showdepartment")
     

# def addemployee(request):
#     form = AddEmployeeForm
#     if request.method == 'POST':
#         form = AddEmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('addemployee')
#     context={
#         'form':form
#     }
#     return render(request,'esaapp/addemployee.html',context)
# request.POST.get('')
def addemployee(request):
    departmentData = AddDepartment.objects.all()
    # if request.method=='POST' and request.FILES['photo'] and request.FILES['adhaarcard'] and request.FILES['pancard'] :
    if request.method == 'POST':
        if(request.POST.get('department'),request.POST.get('fullname'),request.POST.get('address'),request.POST.get('permanentaddress'),request.POST.get('city'),request.POST.get('pincode'),request.POST.get('state'),request.POST.get('mobile'),request.POST.get('bankaccountno'),request.POST.get('email'),request.POST.get('password')):
            post= AddEmployee()
            
            post.department= request.POST.get('department')  
            # post.photo= request.FILES['photo']
            post.fullName = request.POST.get('fullname')
            post.address = request.POST.get('address')
            post.permanentAddr = request.POST.get('permanentaddress')
            post.city =request.POST.get('city')
            post.pincode = request.POST.get('pincode')
            post.state = request.POST.get('state')
            post.mobile = request.POST.get('mobile')
            post.bankAccount = request.POST.get('bankaccountno')
            # post.adhaar = request.FILES['adhaarcard']
            # post.pancard= request.FILES['pancard']
            post.email= request.POST.get('email')
            post.pasword =request.POST.get('password')
            post.save()
            messages.info(request, 'New Employee Recorde Added Successfully')
            return redirect('addemployee')
        
        
    # if request.method=='POST' and request.FILES['photo'] and request.FILES['adhaarcard'] and request.FILES['pancard'] :
    #     photo = request.FILES['photo']
    #     adhaar = request.FILES['adhaarcard']
    #     pancard = request.FILES['pancard']
        
    #     print(photo,request.POST.get('department'),request.POST.get('fullname'),request.POST.get('address'),request.POST.get('permanentaddress'),request.POST.get('city'),request.POST.get('pincode'),request.POST.get('state'),request.POST.get('mobile'),request.POST.get('bankaccountno'),adhaar,pancard,request.POST.get('email'),request.POST.get('password'))
        
    #     return redirect('addemployee')
    context={
        'departmentData':departmentData
    }
    return render(request,'esaapp/addemployee.html',context)


def Updateemployee(request,pk):
    # print(pk)
    # employee_id = AddEmployee.objects.get(id=pk)
    # print(employee_id.department)
    # employee = AddEmployee.objects.all()
    # print(employee)
    postobj= get_object_or_404(AddEmployee, pk=pk)
    print(postobj)
    departmentData = AddDepartment.objects.all()
    # addEmployee = AddEmployee(instance=employee_id)
    # if request.method=='POST' and request.FILES['photo'] and request.FILES['adhaarcard'] and request.FILES['pancard'] :
    if request.method == 'POST':
        if(request.POST.get('department'),request.POST.get('fullname'),request.POST.get('address'),request.POST.get('permanentaddress'),request.POST.get('city'),request.POST.get('pincode'),request.POST.get('state'),request.POST.get('mobile'),request.POST.get('bankaccountno'),request.POST.get('email'),request.POST.get('password')):
            AddEmployee.objects.filter(id=pk).update(
            department= request.POST.get('department'), 
            # photo= request.FILES['photo'],
            fullName = request.POST.get('fullname'),
            address = request.POST.get('address'),
            permanentAddr = request.POST.get('permanentaddress'),
            city =request.POST.get('city'),
            pincode = request.POST.get('pincode'),
            state = request.POST.get('state'),
            mobile = request.POST.get('mobile'),
            bankAccount = request.POST.get('bankaccountno'),
            # adhaar = request.FILES['adhaarcard'],
            # pancard= request.FILES['pancard'],
            email= request.POST.get('email'),
            pasword =request.POST.get('password'))
           
            messages.info(request, 'One Employee Recorde Updated Successfully')
            return redirect('showemployee')
    context={
        'postobj':postobj,
        'departmentData':departmentData
    }
    return render(request,'esaapp/updateemployee.html',context) 

def showemployee(request):
    empData = AddEmployee.objects.all()
    context={
        'empData':empData,
        
    }
    return render(request,'esaapp/showemployee.html',context)

def Deleteemployee(request,pk):
    deleteEmployee = AddEmployee.objects.get(id=pk)
    deleteEmployee.delete()
    messages.info(request, 'One Employee Recorde Deleted Successfully')
    return redirect('showemployee')

def empAttendance(request,pk):
    postobj= get_object_or_404(AddEmployee, pk=pk)
    if request.method == 'POST':
        if(request.POST.get('employeename'),request.POST.get('attendance'),request.POST.get('date')):
            print(request.POST.get('employeename'),request.POST.get('attendance'),request.POST.get('date'))
             
            
            attendance = Attendance()
            attendance.empName = request.POST.get('employeename')
            attendance.date = request.POST.get('date')
            attendance.status = request.POST.get('attendance')
            attendance.save()
            messages.info(request, 'Attendence Successfull')
            return redirect('showemployee')
        
    context={
        'postobj':postobj
    }
    return render(request,'esaapp/empattendance.html',context)

def showAttendance(request):
    allAttendance = Attendance.objects.all()
    context = {
        'allAttendance':allAttendance
    }
    return render(request,'esaapp/showattendance.html',context)

def updateAttendance(request,pk):
    postobj= get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        if(request.POST.get('employeename'),request.POST.get('attendance'),request.POST.get('date')):
            
            Attendance.objects.filter(id=pk).update(
                empName=request.POST.get('employeename'),
                date = request.POST.get('date'),
                status=request.POST.get('attendance')
            )
            # print(request.POST.get('employeename'),request.POST.get('attendance'),request.POST.get('date'))
            messages.info(request, 'One Employee Attendance Successfully')
            return redirect('showattendance')
    context={
        'postobj':postobj
    }
    return render(request,'esaapp/updateattendance.html',context)

def deleteAttendance(request,pk):
    deleteAttendance1 = Attendance.objects.get(id=pk)
    deleteAttendance1.delete()
    return redirect('showattendance')

def employeeReport(request):
    # queryset = Attendance.objects.filter(date="March")
    
    # print(date)
    # print(queryset)
    year1 = []

    for i in range(1900,2023):
        year1.append(i)
    context={
        'year1':year1
    }
    # print(year1)
    # print("shishupal")
     
    
    
    return render(request,'esaapp/emplyeereport.html',context)
    