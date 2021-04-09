from django import forms

from account.models import *

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model=TeacherProfile
        fields=['first_name', 'last_name', 'department', 'gender',  'phone','dob' ]

        #   fields='__all__'