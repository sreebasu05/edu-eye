from django.urls import path,include
from principal import views

urlpatterns = [
    path('home_HOD',views.home_HOD, name="home_HOD"),
    path('add_course', views.add_course, name="add_course"),
    path('add_unit/<int:id>', views.add_unit, name="add_unit"),
    path('view_courses', views.view_courses, name="view_courses"),
    path('completedetails_course/<int:id>',views.completedetails_course,name="completedetails_course"),
    path('add_teacherbatch', views.add_teacherbatch, name="add_teacherbatch"),
    path('coursebatchdetails', views.coursebatchdetails, name="coursebatchdetails"),
    path('status/<int:uid>', views.principal_graph, name="status"),
]
