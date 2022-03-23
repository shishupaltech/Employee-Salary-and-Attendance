from calendar import month
from distutils.command.upload import upload
from email.policy import default
from turtle import mode
from django.db import models
from numpy import require

# Create your models here.

#this is include the department for different employee
class AddDepartment(models.Model):
    departmentName = models.CharField(max_length=191,null=True)
    basicPay = models.BigIntegerField(blank=True,null=True)
    travelAllowance = models.BigIntegerField(blank=True,null=True)
    medicalAllowance=models.BigIntegerField(blank=True,null=True)
    washingAllowance = models.BigIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True) #when we create this model this autometcally generate current date and time after completing the models then register it in admin .py
    
    def __str__(self):
        return self.departmentName
    
class AddEmployee(models.Model):
    #relationship between two table by using the foreign key like this
    department  = models.ForeignKey(AddDepartment ,on_delete=models.SET_NULL,null=True)
    
    fullName = models.CharField(max_length=191,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    permanentAddr = models.CharField(max_length=250,null=True,blank=True)
    city=models.CharField(max_length=150,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    bankAccount = models.BigIntegerField(null=True,blank=True)
    email = models.EmailField(max_length=255)
    pasword = models.CharField(max_length=50)
    def __str__(self):
        return self.fullName
# ***************************from here*****************8
class SalaryReport(models.Model):
    fullName = models.CharField(max_length=191,null=True,blank=True)
    bankAccount = models.BigIntegerField(null=True,blank=True)
    TravelAllowance = models.IntegerField(max_length=100, null=True, blank=True)
    MedicalAllowance = models.IntegerField(max_length=100, null=True, blank=True)
    WashingAllowance = models.IntegerField(max_length=100, null=True, blank=True) 
    #from here
    # date = models.DateField(null = True)
    #to here added 3/20
    #from here
    month = models.CharField(max_length=20,null=True,blank=True)
    #to here 3/21
    total = models.BigIntegerField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.fullName

#**************************to here added 3/17***********************************
    
    
    

