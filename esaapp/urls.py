from django.urls import path
from numpy import nanvar

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('navbar1/',views.navbar1,name='navbar1'),
    path('adddepartment/',views.adddepartment,name="adddepartment"),
    path('showdepartment/',views.showdepartment,name="showdepartment"),
    path('addemployee/',views.addemployee,name="addemployee"),
    path('showemployee/',views.showemployee,name="showemployee"),
    path('salary_report/',views.salary_report,name="salary_report"),
    path('search_salary/',views.search_salary,name="search_salary"),
    
    
]