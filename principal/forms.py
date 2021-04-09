from django import forms

from account.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
