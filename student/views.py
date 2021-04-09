from django.shortcuts import render,HttpResponse,redirect

from django.contrib import messages
# Create your views here.
from account.models import *


def home_student(request):
    return render(request,'student/home.html')