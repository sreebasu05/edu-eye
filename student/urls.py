from django.urls import path,include
from student import views

urlpatterns = [
    
    path('home_student',views.home_student,name="home_student"),
    path('profile_student', views.student_profile, name="profile_student"),
    path('profileform_student', views.StudProfile, name="profileform_student"),

]