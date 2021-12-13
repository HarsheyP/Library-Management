from django.urls import path
from .import views

app_name = 'library'

urlpatterns = [
    path('', views.landingpage , name="landingpage"),
    path('/adminreg', views.adminreg, name="adminreg"),

]
