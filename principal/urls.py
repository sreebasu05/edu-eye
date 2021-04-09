from django.urls import path,include
from principal import views

urlpatterns = [

    path('add_course', views.add_course, name="add_course"),
    path('add_unit', views.add_unit, name="add_course"),
    path('view_courses', views.view_courses, name="view_courses"),
    path('completedetails_course/<int:id>',views.completedetails_course,name="completedetails_course"),

]
