from django.urls import path,include
from teacher import views

urlpatterns = [
    
    path('home_teacher', views.home_teacher, name="home_teacher"),
    path('profile_teacher', views.TeachProfile, name="profile_teacher"),
    path('profileform_teacher', views.CreateProfile, name="profileform_teacher"),
    path('dashboard_teacher', views.dash, name="dashboard_teacher"),
    path('unit_teacher/<int:bid>',views.unitdetail,name="unit_teacher"),

]