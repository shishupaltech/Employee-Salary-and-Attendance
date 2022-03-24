from django import forms
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper

from .models import AddDepartment,AddEmployee
# form for add department

class AddDepartmentForm(ModelForm):
    
    class Meta:
        
        #provide the model for what you want to create form
        model = AddDepartment
        fields = '__all__'
        
class AddEmployeeForm(ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    AddDepartment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter department','width':'550px','height':'55px'}))
    fullName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    class Meta:
        model = AddEmployee
        fields = '__all__'
        
        
        