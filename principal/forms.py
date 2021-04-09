from django import forms

from account.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields='__all__'
