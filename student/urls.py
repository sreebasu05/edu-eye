from django.urls import path,include
from student import views

urlpatterns = [
    
    path('home_student', views.home_student, name="home_student"),
    

]