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
            rating = []
            for bd in batchdetail:
                if bd.is_completed==True:
                    if bd.students_polled!=0:
                        x=bd.rating/bd.students_polled
                        rating.append(x)
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
            return render(request,'teacher/unitdash.html',{'bid':bid,'unitid':unitid})
    else:
        print("NOT A Teacher!! login as teacher :P")
        return redirect('login')

# def unit_progress(request):
#     teacher = TeacherProfile.objects.get(teacher=request.user)
#     query_set = TeacherBatchCourse.objects.filter(teacher_details=teacher)
#     print(query_set)
#
#     for q in query_set:
#         i = TrackProgressBatchCourse.objects.filter(batchcourse=q.batchcourse)
#         print(i)
#     return render(request, 'teacher/home.html')




def pie_chart(request, bid):
    batchcourse = BatchCourse.objects.get(pk=bid)
    course=batchcourse.course

    labels = []
    batchcourses = BatchCourse.objects.filter(course=course)
    for bc in batchcourses:
        x=TeacherBatchCourse.objects.get(batchcourse=bc).teacher_details.first_name
        labels.append(x)
    print(labels)

    data = []
    for bc in batchcourses:
        tp=TrackProgressBatchCourse.objects.filter(batchcourse=bc)
        ctr=0
        for u in tp:
            if u.is_completed==True:
                ctr+=1;
        if ctr:
            data.append(ctr)
        else:
            data.append(0)
    print(data)
    labels2=[]
    data2A=[]
    data2B=[]
    tp=TrackProgressBatchCourse.objects.filter(batchcourse=batchcourse)
    for t in tp:
        if t.is_completed==True:
            x = t.unit.name
            y1 = t.lecture_taken
            y2 = t.unit.ideallecture
            labels2.append(x)
            data2A.append(y1)
            data2B.append(y2)

    return render(request, 'teacher/pie_chart.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2A': data2A,
        'data2B' : data2B

    })
