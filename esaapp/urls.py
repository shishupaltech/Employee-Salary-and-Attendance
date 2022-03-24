from django.urls import path
from numpy import nanvar

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('navbar1/',views.navbar1,name='navbar1'),
    path('adddepartment/',views.adddepartment,name="adddepartment"),
    path('showdepartment/',views.showdepartment,name="showdepartment"),
    path('updatedepartment/<str:pk>',views.updateDepartment,name="updatedepartment"),
    path('deletedepartment/<str:pk>',views.deleteDepartment,name="deletedepartment"),
    path('addemployee/',views.addemployee,name="addemployee"),
    path('showemployee/',views.showemployee,name="showemployee"),
    path('updateemployee/<str:pk>',views.Updateemployee,name="updateemployee"),
    path('deleteemployee/<str:pk>',views.Deleteemployee,name="deleteemployee"),
    path('empattendance/<str:pk>',views.empAttendance,name="empattendance"),
    path('showattendance/',views.showAttendance,name="showattendance"),
    path('updateattendance/<str:pk>',views.updateAttendance,name="updateattendance"),
    path('deleteattendance/<str:pk>',views.deleteAttendance,name="deleteattendance"),
    path('employeereport/',views.employeeReport,name="employeereport"),
    
    
]