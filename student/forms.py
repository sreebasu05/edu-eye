from django import forms

from account.models import *


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'gender', 'phone', 'dob']
