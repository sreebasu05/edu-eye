from django.urls import path,include
from teacher import views

urlpatterns = [
    
    path('home_teacher',views.home_teacher,name="home_teacher"),

]