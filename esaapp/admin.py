from django.contrib import admin
from .models import AddDepartment, AddEmployee,Attendance

# Register your models here.
admin.site.register(AddDepartment)
admin.site.register(AddEmployee)
admin.site.register(Attendance)
