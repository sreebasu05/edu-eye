from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import TeacherProfileForm
from account.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def home_teacher(request):
    if request.user.is_teacher ==True:
        return render(request, 'teacher/home.html')
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

@login_required(login_url='login')
def TeachProfile(request):
    if request.user.is_teacher ==True:
        currUser = request.user.email
        Teacher = get_object_or_404(TeacherProfile, teacher_id=request.user.id)
        return render(request, 'teacher/profile.html',{'Teacher':Teacher})
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

@login_required(login_url='login')
def CreateProfile(request):
    if(TeacherProfile.objects.filter(teacher=request.user).exists()):
        Teacher = get_object_or_404(TeacherProfile, teacher_id=request.user.id)
        return render(request, 'teacher/profile.html',{'Teacher':Teacher}) 
    if request.method == 'POST':
        fm = TeacherProfileForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.teacher = request.user
            print(instance.id)
            # teacher_id=instance.id
            instance.save()
            Teacher = get_object_or_404(TeacherProfile, teacher_id=request.user.id)
            messages.success(request, 'Your profile has been created')
            return render(request,'teacher/profile.html',{'Teacher':Teacher})
            # return render(request,'teacher/home.html')
        else:
            messages.error(request, 'Please enter valid details')
            return render(request,'teacher/profileform.html',{'form':fm})
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

@login_required(login_url='login')
def dash(request):
    if request.user.is_teacher ==True:
        uid = request.user.id
        Teacher = get_object_or_404(TeacherProfile, teacher_id=uid)
        Teaches = TeacherBatchCourse.objects.filter(teacher_details=Teacher)
        return render(request,'teacher/dashboard.html',{'Teaches':Teaches})
        print(Teach)
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

@login_required(login_url='login')
def unitdetail(request, bid):
    if request.user.is_teacher ==True:
        if request.user.is_teacher ==True:
            batchdetail = TrackProgressBatchCourse.objects.filter(batchcourse_id=bid)
            print(batchdetail)
            # print(batchdetail.unit.unit_no)
            # print(batchdetail.batchcourse)
            # print(batchdetail)

        return render(request, 'teacher/unitdash.html', {'batchdetails': batchdetail,'bid':bid})
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

        
@login_required(login_url='login')
def isCompleteUint(request, bid, unitid):
    if request.user.is_teacher ==True:
        batchdetail = TrackProgressBatchCourse.objects.get(batchcourse_id=bid,unit_id=unitid)
        if request.method == 'POST':
            comp = request.POST['comp']
            lecture = request.POST['lecture']
            print(comp)
            print(lecture)
            if comp == "Completed":
                batchdetail.is_completed = True

            batchdetail.lecture_taken = lecture
            print(batchdetail)
            batchdetail.save()
            uid = request.user.id
            Teacher = get_object_or_404(TeacherProfile, teacher_id=uid)
            Teaches = TeacherBatchCourse.objects.filter(teacher_details=Teacher)
            return render(request,'teacher/dashboard.html',{'Teaches':Teaches})    
        else:
            print("hello")
            return render(request,'teacher/unitform.html',{'bid':bid,'unitid':unitid})
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')
