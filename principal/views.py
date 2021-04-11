from django.shortcuts import render
from .forms import *
from django.contrib import messages
from account.models import *
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home_HOD(request):
    if request.user.is_principal ==True:
        return redirect('profile_teacher')
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')

@login_required(login_url='login')
def add_course(request):
    if request.user.is_principal ==True:
        if request.method == 'POST':
            fm = CourseForm(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.save()

                i = instance.id
                curr_course = Course.objects.get(pk = i)
                batches = Batch.objects.filter(in_class = curr_course.class_no)
                for b in batches:
                    BatchCourse.objects.create(
                    batch= b,
                    course= curr_course,
                ).save()
                messages.success(request,'created')
                return redirect('profile_teacher')
                # return render(request,'teacher/home.html')
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'principal/home.html')
        else:
            fm=CourseForm()
            return render(request,'principal/create_course.html',{'form':fm})
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')



@login_required(login_url='login')
def view_courses(request):
    if request.user.is_principal ==True:
        courses = Course.objects.all()
        print(courses)
        context ={'courses' : courses}
        return render(request,'principal/viewcourses.html',context)
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')



@login_required(login_url='login')
def completedetails_course(request,id):
    if request.user.is_principal ==True:
        course = Course.objects.get(pk=id)

        print(course.name)
        units = Unit.objects.filter(course= course)
        context ={'course' : course, 'units' : units}
        return render(request,'principal/completedetails_course.html',context)
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')


@login_required(login_url='login')
def add_unit(request, id):
    if request.user.is_principal ==True:
        c = Course.objects.get(pk=id)
        print(c)
        if request.method == 'POST':
            fm = UnitForm(request.POST)
            if fm.is_valid():

                instance = fm.save(commit=False)
                instance.course = c
                instance.save()
                i=instance.id
                u = Unit.objects.get(pk=i)
                batchcourses = BatchCourse.objects.filter(course = c)
                # print(batchcourses)
                for b in batchcourses:
                    TrackProgressBatchCourse.objects.create(
                    unit= u,
                    batchcourse= b,
                ).save()
                return redirect('profile_teacher')
            # return render(request,'teacher/home.html')
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'principal/home.html')
        else:
            fm=UnitForm()
            profile=TeacherProfile.objects.get(teacher=request.user)
            print(profile)
        # form = UnitForm(initial={'course': request.user.teacher.})
            return render(request,'principal/create_unit.html',{'form':fm})
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')


@login_required(login_url='login')
def coursebatchdetails(request):
    if request.user.is_principal ==True:
        profile=TeacherProfile.objects.get(teacher=request.user)
        courses=Course.objects.filter(name=profile.department)
        batchcourse=[]
        for c in courses:
            batchcourse.append(BatchCourse.objects.filter(course=c))

        return render(request,'principal/coursebatchdetails.html',{'batchcourses':batchcourse})
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')

@login_required(login_url='login')
def add_teacherbatch(request,bc):
    if request.user.is_principal ==True:
        if request.method == 'POST':
            fm = TeacherBatchForm(request.POST)
            if fm.is_valid():

                instance = fm.save(commit=False)
                instance.save()
                return render(request,'principal/home.html')
            # return render(request,'teacher/home.html')
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'principal/home.html')
        else:
            fm=TeacherBatchForm()
            return render(request,'principal/create_teacherbatch.html',{'form':fm})
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')


@login_required(login_url='login')
def principal_graph(request, uid):
    if request.user.is_principal == True:
        course = Course.objects.get(id=uid)
        labels = []
        batchcourses = BatchCourse.objects.filter(course=course)
        for bc in batchcourses:
            x = TeacherBatchCourse.objects.get(batchcourse=bc).teacher_details.first_name
            labels.append(x)
        print(labels)

        data = []
        for bc in batchcourses:
            tp = TrackProgressBatchCourse.objects.filter(batchcourse=bc)
            ctr = 0
            for u in tp:
                if u.is_completed == True:
                    ctr += 1;
            if ctr:
                data.append(ctr)
            else:
                data.append(0)
        print(data)
        return render(request, 'principal/progress.html', {
            'labels': labels,
            'data': data,
        })
    else:
        print("NOT A HOD!! login as HOD :P")
        return redirect('login')
