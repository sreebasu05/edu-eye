"""edu_eye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from account import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup_student',views.Studentsignup,name='signup_student'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate'),
    path('login',views.login_view,name='login'),
    path('logout', views.logout_view,name='logout'),
    path('request-reset-email',views.RequestResetEmail.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('student/',include('student.urls') ),
    path('teacher/',include('teacher.urls') ),
    path('principal/', include('principal.urls'))

]
