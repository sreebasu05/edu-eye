from django.urls import path,include
from principal import views

urlpatterns = [

    path('add_course', views.add_course, name="add_course"),
    path('add_unit', views.add_unit, name="add_course"),

]
