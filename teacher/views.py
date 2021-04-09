from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import TeacherProfileForm
from account.models import *

from django.contrib import messages
# Create your views here.



def home_teacher(request):
    return render(request, 'teacher/home.html')
    
def TeachProfile(request):
    currUser = request.user.email
    Teacher = get_object_or_404(TeacherProfile, teacher_id=request.user.id)
    return render(request, 'teacher/profile.html',{'Teacher':Teacher})
          
 
            
def CreateProfile(request):
    mail = request.user.email
    print(mail)
    if request.method == 'POST':
        fm = TeacherProfileForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.teacher = request.user
            print(instance.id)
            # teacher_id=instance.id
            instance.save()
            messages.success(request, 'Your profile has been created')
            return render(request,'teacher/profileform.html')
            # return render(request,'teacher/home.html')     
        else:
            messages.error(request, 'Please enter valid details')
            return render(request,'teacher/home.html')   
    else:
        fm=TeacherProfileForm()
        print("hello")
        return render(request,'teacher/profileform.html',{'form':fm})
    