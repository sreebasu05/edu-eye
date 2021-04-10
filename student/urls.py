from django.urls import path,include
from student import views

urlpatterns = [

    path('home_student',views.home_student,name="home_student"),
    path('profile_student', views.student_profile, name="profile_student"),
    path('profileform_student', views.StudProfile, name="profileform_student"),
    path('student_dash', views.dash, name='StudentDash'),
    path('student_profile', views.profile, name="StudentProfile"),
    path('apply_CR',views.apply_CR,name="apply_CR"),

]
