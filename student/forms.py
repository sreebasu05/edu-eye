from django import forms

from account.models import *


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = ['first_name', 'last_name','student_batch', 'gender', 'phone', 'dob']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_batch'].queryset = Batch.objects.all()
