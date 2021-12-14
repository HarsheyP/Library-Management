from django.shortcuts import render
from . import models,forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from librarymanagement.settings import EMAIL_HOST_USER

# Create your views here.

def landingpage(request):
    return render(request, 'landingpage.html')

def adminreg(request):

    form=forms.LibrarianRegForm()

    if request.method=='POST':
        form=forms.LibrarianRegForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('')

    return render(request, 'adminregister.html',{'form':form}) 

def studentreg(request):

    form1=forms.StudentRegForm()

    context={}

    if request.method=='POST':
        form1=forms.StudentRegForm(request.POST)
        if form1.is_valid:
            user=form1.save()
            user.set_password(user.password)
            user.save()

            my_student_group = Group.objects.get_or_create(mane='STUDENT')
            my_student_group[0].user_set.add(user)

            return HttpResponseRedirect('')

    context['form1']=form1
    return render(request,'studentregister.html',context)