from django import http
from django.contrib.auth import authenticate, login
from django.forms.fields import NullBooleanField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import todomodel
from .forms import todoform ,usersign,userlogin
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def usersignup(request) :
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = usersign(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Welcome Your account created")
                return HttpResponseRedirect("/login/")
        else:
            form=usersign()
        return render(request,'signup.html',{'form':form})
    else :
        return HttpResponseRedirect("/login/")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = userlogin(request,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname,password = upass)
                if user is not None:
                    login(request,user)
                    # data = user.objects.get(pk=request)
                return HttpResponseRedirect('/profile/')

        else :
            form =userlogin()
        return render(request,'login.html',{'form':form})
    else :
        return HttpResponseRedirect("/profile/")

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def profile(request):
    if request.user.is_authenticated:
        form = todomodel.objects.filter(user = request.user)
        # form = 5
        return render(request,'profile.html',{'form':form})
    else:
        messages.error(request,'Login to visit profile')
        return HttpResponseRedirect('/login/')


def addtask(request):
    if request.method == 'POST':
        form = todoform(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request,"Task Added successfully ")
            return HttpResponseRedirect('/')
    else :
        form = todoform()
    return render(request,'task.html',{'form':form})


def viewdata(request,id):
    form = todomodel.objects.get(pk=id)
    return render(request,'view.html',{'form':form})

def done(request,id):
    if request.method == 'POST':
        md = todomodel.objects.get(pk=id)
        md.delete()
    return HttpResponseRedirect('/profile/')
    
def edit(request,id):
    if request.method == 'POST':
        pi=todomodel.objects.get(pk=id)
        form = todoform(request.POST,instance=pi)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.user = request.user
            # instance.save()
            form.save()
            return HttpResponseRedirect('/profile/')
    else :
        pi=todomodel.objects.get(pk=id)
        form = todoform(instance=pi)
    return render(request,'edit.html',{'form':form})