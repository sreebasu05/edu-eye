from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.views.generic.base import View

from .forms import StudentProfileForm
from account.models import *


def home_student(request):
    return render(request, 'student/home.html')

def student_profile(request):
    if(StudentProfile.objects.filter(student=request.user).exists()):
        student = student = StudentProfile.objects.get(student=User.object.get(id=request.user.id))
        context = {
         'student': student
        }
        return render(request, 'student/profile.html', context)
    else:
        if request.method == 'POST':
            fm = StudentProfileForm(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.student = request.user
                print(instance.id)
                instance.save()
                messages.success(request, 'Your profile has been created')
                student = student = StudentProfile.objects.get(student=User.object.get(id=request.user.id))
                context = {
                'student': student
                    }

                return render(request, 'student/profile.html', context)
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'student/profile-form.html',{'form':fm})
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
        'student':student,
    }
    return render(request, 'student/student_dash.html', context)

def profile(request):
    student = student = StudentProfile.objects.get(student=User.object.get(id=request.user.id))
    context = {
        'student': student
    }

    return render(request, 'student/profile.html', context)


def units(request, bid):
    batches = TrackProgressBatchCourse.objects.filter(batchcourse_id=bid)
    b = BatchCourse.objects.get(pk=bid)
    print(bid)
    return render(request, 'student/unit.html', {'batches': batches, 'batch':b})


def giveRating(request,bid):
    track = TrackProgressBatchCourse.objects.get(pk=bid)

    print(track.batchcourse)

    if request.method == 'POST':
        rating = request.POST['rating']
        
        print(rating)
        
        track.rating = track.rating + int(rating)
        track.students_polled =track.students_polled+1
        track.save()
        uid = request.user.id
        print(request.user.email)
        student = StudentProfile.objects.get(student=User.object.get(id=uid))
        print(student.first_name)
        courses = BatchCourse.objects.filter(batch=student.student_batch)
        context = {
         'courses': courses,
         'student':student,
        }
        return render(request, 'student/student_dash.html', context)

    else:
        print("hello")
        return render(request,'student/unit.html',{'bid':bid})

    