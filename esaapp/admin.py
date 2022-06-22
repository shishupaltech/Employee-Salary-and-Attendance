from django.contrib import admin
from .models import AddDepartment, AddEmployee, EmployeeDetail, SalaryReport

# Register your models here.
admin.site.register(AddDepartment)
admin.site.register(AddEmployee)
admin.site.register(SalaryReport)
admin.site.register(EmployeeDetail)
