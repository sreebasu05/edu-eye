from django.shortcuts import render
from .forms import *
from account.models import *
# Create your views here.
def add_course(request):
    if request.method == 'POST':
        fm = CourseForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.save()
            return render(request,'principal/home.html')
            # return render(request,'teacher/home.html')
        else:
            messages.error(request, 'Please enter valid details')
            return render(request,'principal/home.html')
    else:
        fm=CourseForm()
        return render(request,'principal/create_course.html',{'form':fm})

def view_courses(request):
    courses = Course.objects.all()
    print(courses)
    context ={'courses' : courses}
    return render(request,'principal/viewcourses.html',context)

def completedetails_course(request,id):
    course = Course.objects.get(pk=id)

    print(course.name)
    units = Unit.objects.filter(course= course)
    context ={'course' : course, 'units' : units}
    return render(request,'principal/completedetails_course.html',context)


def add_unit(request):
    if request.method == 'POST':
        fm = UnitForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.save()
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
