from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.views.generic.base import View
from django.contrib import messages
from .forms import StudentProfileForm
from account.models import *
from django.contrib.auth.decorators import login_required
from principal.models import Applicants_CR

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
            #num = Batch.objects.filter(in_class=request.POST.get('class'), section=request.POST.get('section')).count()

            # if(num == 0):
            #     Batch.objects.create(
            #         in_class=request.POST.get('class'),
            #         section=request.POST.get('section')
            #     ).save()
            #
            # instance.batch = Batch.objects.get(in_class=request.POST.get('class'), section=request.POST.get('section'))


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


def dash(request):
    uid = request.user.id
    print(request.user.email)
    student = StudentProfile.objects.get(student=User.object.get(id=uid))
    print(student.first_name)
    courses = BatchCourse.objects.filter(batch=student.student_batch)
    context = {
        'courses': courses,
        'name':student.first_name,
    }
    return render(request, 'student/student_dash.html', context)

def profile(request):
    student = student = StudentProfile.objects.get(student=User.object.get(id=request.user.id))
    context = {
        'student': student
    }

    return render(request, 'student/profile.html', context)


def apply_CR(request):
    
    if request.method=="POST":
        profile = StudentProfile.objects.get(student= request.user)
        print(type(profile), profile.id)
        try:
            app = Applicants_CR.objects.get(applicant=profile)
            messages.error(request,'You have already applied for batch representative')
            return redirect('home_student')

        except Applicants_CR.DoesNotExist:
            Applicants_CR.objects.create(
                applicant = profile,
            ).save()
            messages.success(request,'Your application is received!!')
            return redirect('home_student')
    else:

        return render(request,'student/home.html')