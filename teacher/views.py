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
    if(TeacherProfile.objects.filter(teacher=request.user).exists()):
        return render(request, 'teacher/home.html')
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

def dash(request):
    uid = request.user.id
    Teacher = get_object_or_404(TeacherProfile, teacher_id=uid)
    Teaches = TeacherBatchCourse.objects.filter(teacher_details=Teacher)
    return render(request,'teacher/dashboard.html',{'Teaches':Teaches})
    print(Teach)

def unitdetail(request, bid):
    batchdetail = TrackProgressBatchCourse.objects.filter(batchcourse_id=bid)
    print(batchdetail)
    # print(batchdetail.unit.unit_no)
    # print(batchdetail.batchcourse)
    # print(batchdetail)

    return render(request, 'teacher/unitdash.html', {'batchdetails': batchdetail,'bid':bid})
    
def isCompleteUint(request, bid, unitid):
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
            
        return render(request,'teacher/home.html')
    else:
        print("hello")
        return render(request,'teacher/unitform.html',{'bid':bid,'unitid':unitid})
