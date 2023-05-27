from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def signinuser(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.method=='POST':
            User.objects.create_user(username,email,password)
            messages.success(request,f'Account created Successfully ')
            return redirect('/loginuser')
    except Exception as e:
        messages.error(request, "Username already exists. Please choose a different username.")
    return render(request,'signin.html')

def loginuser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method=='POST':
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'You are now loged in')
            return redirect('/todo')
        
        else:
            messages.success(request,f'Username or password is incorrect')
            return render(request,'login.html') 
        
    return render(request,'login.html')

@login_required
def todo_list(request):
    todos = Todos.objects.filter(user=request.user)
    context = {
        'todos':todos,
        'user':request.user
    }
    return render(request,'dashboard.html',context)

def logoutuser(request):
    logout(request)
    messages.success(request,f'You are loged out')
    return redirect('loginuser')

def add_task(request):
    task = request.POST.get('task')
    desc = request.POST.get('desc')
    if request.method=='POST':
        Todos.objects.create(user=request.user,task=task,desc=desc)
        return redirect('/todo')
    return render(request,'add_task.html',locals())

def delete_item(request,id):
    todo_item = Todos.objects.get(id=id)
    todo_item.delete()
    return redirect('/todo')

def edit_item(request,id):
    todo_item = Todos.objects.get(id=id)
    if request.method=='POST':
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        complete = request.POST.get('complete')

        todo_item.task = task
        todo_item.desc = desc
        if complete=='on':
            todo_item.complete=True
        else:
            todo_item.complete=False
        
        todo_item.save()
        return redirect('/todo')
    return render(request,'edit_task.html',locals())

def add_to_complete(request,id):
    todo_item = Todos.objects.get(id=id)
    todo_item.complete = True
    todo_item.save()
    return redirect('/todo')