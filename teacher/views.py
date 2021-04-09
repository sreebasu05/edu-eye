from django.shortcuts import render,HttpResponse,redirect

from django.contrib import messages
# Create your views here.



def home_teacher(request):
    return render(request,'teacher/home.html')