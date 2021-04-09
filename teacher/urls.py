from django.urls import path,include
from teacher import views

urlpatterns = [
    
    path('home_teacher', views.home_teacher, name="home_teacher"),
    path('profile_teacher', views.TeachProfile, name="profile_teacher"),
    path('profileform_teacher',views.CreateProfile,name="profileform_teacher"),

]