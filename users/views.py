from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, NewForm
from .models import Todo, DoneTodo
#import datetime
from datetime import datetime,timezone
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    date=datetime.now()
    return render(request,"users/home.html",{
        "date":date
    })


@login_required
def todo(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=NewForm(request.POST)
        if form.is_valid():
            t=form.save(commit=False)
            t.user=user
            t.save()
            return redirect("todo")
        else:
            form=NewForm()
        return render(request,"users/todo.html",{
            "form":form,
            "todo":Todo.objects.filter(user=user),
            "date":datetime.now()
        })


def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            raw_password=make_password(form.cleaned_data.get('password'))
            
            login(request, user)
            return redirect("login")

    else:
        form=SignUpForm()
    return render(request, 'users/signup.html',{
        "form":form,
        "date":datetime.now()

    })      
def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("todo"))
        else:
            return render(request,"users/home.html",{
                "message": "Invalid credentials.",
                "date":datetime.datetime.now()
                
            })
            
    return render(request,"users/home.html",{
        "date":datetime.now()
    })

def deletetodo(request, todo_id):
    if request.user.is_authenticated:
        user=request.user
        t=Todo.objects.filter(user=user)
        tobject=t.get(pk=todo_id)
        tobject.delete()
        return HttpResponseRedirect(reverse("todo"))

def updatetodo(request, todo_id):
    if request.user.is_authenticated:
        user=request.user
        t=Todo.objects.filter(user=user)
        tobject=t.get(pk=todo_id)
        tobject.text=request.POST.get("text")
        tobject.date_inserted=datetime.now()
        tobject.save()
        return HttpResponseRedirect(reverse("todo"))

def donetodo(request, todo_id):
    if request.user.is_authenticated:
        user=request.user
        if request.method=="POST":
            t=Todo.objects.filter(user=user)
            tobject=t.get(pk=todo_id)
            
            dtext=tobject.text
            dstart=tobject.date_inserted
            dend=datetime.now(timezone.utc)
            diff=dend-dstart
            dobject=DoneTodo.objects.create(user=user,text=dtext,start_date=dstart,finished_date=dend,difference=diff)
           
            tobject.delete()
        return HttpResponseRedirect(reverse("todo"))   

def viewdone(request):
    if request.user.is_authenticated:
        user=request.user
        return render(request,"users/donetodo.html",{
                "donetodo":DoneTodo.objects.filter(user=user),
                "date":datetime.now()
        })
 
        
def logout_view(request):
    
    logout(request)
    return render(request,"users/home.html",{
        "message": "Logged out.",
        "date":datetime.now()
    })