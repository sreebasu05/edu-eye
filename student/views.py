from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm
from account.models import *

@login_required(login_url='login')
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
            if request.method == 'POST':
                fm = StudentProfileForm(request.POST)
                if fm.is_valid():
                    instance = fm.save(commit=False)
                    instance.student = request.user
                    print(instance.id)
                    # teacher_id=instance.id                #num = Batch.objects.filter(in_class=request.POST.get('class'), section=request.POST.get('section')).count()

                    # if(num == 0)
                    #     Batch.objects.create(                #         in_class=request.POST.get('class'),
                #         section=request.POST.get('section')
                    #     ).save()
                    #
                    # instance.batch = Batch.objects.get(in_class=request.POST.get('class'), section=request.POST.get('section'))


                    instance.save()
                    messages.success(request, 'Your profile has been created')
                    return render(request,'student/home.html')
                        # return render(request,'teacher/home.html')
                else:
                    messages.error(request, 'Please enter valid details')
                    return render(request,'student/profile-form.html')
            else:
                fm=StudentProfileForm()
                print("hello")
                return render(request,'student/profile-form.html',{'form':fm})




@login_required(login_url='login')
def dash(request):
    uid = request.user.id
    print(request.user.email)
    if request.user.is_student == True :
        student = StudentProfile.objects.get(student=User.object.get(id=uid))
        print(student.first_name)
        courses = BatchCourse.objects.filter(batch=student.student_batch)
        context = {
            'courses': courses,
            'student':student,
        }
        return render(request, 'student/student_dash.html', context)
    else:
        print("NOT A Student!!")
        return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.user.is_student == True :
        student = student = StudentProfile.objects.get(student=User.object.get(id=request.user.id))
        context = {
            'student': student
        }

        return render(request, 'student/profile.html', context)
    else:
        print("NOT A Student!!")
        return redirect('login')



@login_required(login_url='login')
def units(request, bid):
    if request.user.is_student ==True:
        batches = TrackProgressBatchCourse.objects.filter(batchcourse_id=bid)
        b = BatchCourse.objects.get(pk=bid)
        print(bid)
        return render(request, 'student/unit.html', {'batches': batches, 'batch':b})
    else:
        print("NOT AUTHORIZED!!")
        return redirect('login')
@login_required(login_url='login')
def giveRating(request,bid):
    if request.user.is_student ==True:

        track = TrackProgressBatchCourse.objects.get(pk=bid)


        print(track.batchcourse)

        if request.method == 'POST':
            rating = request.POST['rating']

            print(rating)

            track.rating = track.rating + int(rating)
            track.students_polled =track.students_polled+1
            track.save()
            uid = request.user.id
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


    else:
        print("NOT AUTHORIZED!!")
        return redirect('login')
