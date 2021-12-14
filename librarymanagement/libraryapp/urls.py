from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'library'

urlpatterns = [
    path('', views.landingpage , name="landingpage"),
    path('adminreg/', views.adminreg, name="adminreg"),
    path('studentreg/', views.studentreg, name="studentreg"),

]
