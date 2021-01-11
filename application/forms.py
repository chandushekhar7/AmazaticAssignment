from django import forms
from .models import *

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
