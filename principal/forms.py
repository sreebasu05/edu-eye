from django import forms

from account.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields=['unit_no','name']

class TeacherBatchForm(forms.ModelForm):
    class Meta:
        model=TeacherBatchCourse
        fields='__all__'

class TeacherCourseForm(forms.ModelForm):
    class Meta:
        model=TeacherBatchCourse
        fields=['teacher_details']
