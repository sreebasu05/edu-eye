from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import StudentProfileForm
from account.models import *


def home_student(request):
    return render(request, 'student/home.html')

def StudProfile(request):
    currUser = request.user.email
    student = get_object_or_404(StudentProfile, student_id=request.user.id)
    return render(request, 'student/profile.html',{'Student':student})


def student_profile(request):
    mail = request.user.email
    print(mail)
    if request.method == 'POST':
        fm = StudentProfileForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.student = request.user
            print(instance.id)
            # teacher_id=instance.id
            num = Batch.objects.filter(in_class=request.POST.get('class'), section=request.POST.get('section')).count()

            if(num == 0):
                Batch.objects.create(
                    in_class=request.POST.get('class'),
                    section=request.POST.get('section')
                ).save()

            instance.batch = Batch.objects.get(in_class=request.POST.get('class'), section=request.POST.get('section'))


            instance.save()
            messages.success(request, 'Your profile has been created')
            return render(request,'student/profile.html')
            # return render(request,'teacher/home.html')
        else:
            messages.error(request, 'Please enter valid details')
            return render(request,'student/home.html')
    else:
        fm=StudentProfileForm()
        print("hello")
        return render(request,'student/profile-form.html',{'form':fm})