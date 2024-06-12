from django import forms
from .models import *

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'