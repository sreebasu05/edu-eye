from django.shortcuts import render
from .forms import *
from django.contrib import messages
from account.models import *
from principal.models import Applicants_CR
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
def add_course(request):
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
            return render(request,'principal/home.html')
            # return render(request,'teacher/home.html')
        else:
            messages.error(request, 'Please enter valid details')
            return render(request,'principal/home.html')
    else:
        fm=CourseForm()
        return render(request,'principal/create_course.html',{'form':fm})

def view_courses(request):
    teacher_profile = TeacherProfile.objects.get(teacher= request.user)
    print(teacher_profile.department)
    courses = Course.objects.filter(name= teacher_profile.department)
    print(courses)
    context ={'courses' : courses}
    return render(request,'principal/viewcourses.html',context)

def completedetails_course(request,id):
    course = Course.objects.get(pk=id)

    print(course.name)
    units = Unit.objects.filter(course= course)
    context ={'course' : course, 'units' : units}
    return render(request,'principal/completedetails_course.html',context)


def add_unit(request, id):
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
            return render(request,'principal/home.html')
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



def viewapplicants_CR(request):
    item = Applicants_CR.objects.all()
    context ={'item' : item}
    return render(request,'principal/viewapplicants_CR.html',context)


def completedetails_CR(request,id):
    
    item=Applicants_CR.objects.get(pk=id)
    context = {'viewjob':item}
    return render(request,'principal/completedetails_CR.html',context)

def deleteApplication_CR(request,id):
    
    item=Applicants_CR.objects.get(pk=id)
    item.delete()
    messages.warning(request,'Application has been deleted')
    return redirect('viewapplicants_CR')
    

def confirmApplication_CR(request,id):
    
    item = Applicants_CR.objects.get(pk=id)
    p = StudentProfile.objects.get(student=item.applicant.student)
    email= p.student.email
    flag=True
    

    if not StudentProfile.objects.filter(is_batchRepresntative=True).exists():
        p.is_batchRepresntative = True
        
        
        p.save()
        
        
        email_subject=' edu-eye'
        message='Congratulations!!! You are selected as BRANCH REPRESENTATIVE for your BATCH'
        email_message = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
        )
        email_message.send()
        messages.success(request,'Application for user '+p.student.email +' confirmed')
        print(p.student.email)
        it=Applicants_CR.objects.get(pk=id)
        it.delete()
        item = Applicants_CR.objects.all()
        context ={'item' : item}
        return redirect('viewapplicants_CR')

    else:
        messages.error(request,'Branch Representative for batch already exist')
        item = Applicants_CR.objects.all()
        context ={'item' : item}
        return redirect('viewapplicants_CR')