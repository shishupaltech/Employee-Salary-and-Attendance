from django import forms
from django.forms import ModelForm
from django import forms

from .models import AddDepartment,AddEmployee
# form for add department

class AddDepartmentForm(ModelForm):
    
    class Meta:
        
        #provide the model for what you want to create form
        model = AddDepartment
        fields = '__all__'
        
class AddEmployeeForm(ModelForm):
    class Meta:
        model = AddEmployee
        fields = '__all__'
        
        
        