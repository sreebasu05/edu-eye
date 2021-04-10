from django.urls import path,include
from principal import views

urlpatterns = [

    path('add_course', views.add_course, name="add_course"),
    path('add_unit/<int:id>', views.add_unit, name="add_unit"),
    path('view_courses', views.view_courses, name="view_courses"),
    path('completedetails_course/<int:id>',views.completedetails_course,name="completedetails_course"),
    path('viewapplicants_CR',views.viewapplicants_CR,name="viewapplicants_CR"),
    path('completedetails_CR/<int:id>',views.completedetails_CR,name="completedetails_CR"),
    path('confirmApplication_CR/<int:id>',views.confirmApplication_CR,name="confirmApplication_CR"),
    path('deleteApplication_CR/<int:id>',views.deleteApplication_CR,name="deleteApplication_CR"),

]
