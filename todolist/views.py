import datetime
from todolist.models import todolist
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

from .forms import AddList


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = todolist.objects.filter(user = request.user)
    context = {
        'todolist' : data_todolist,
        # 'last_login' : 
        'last_login_datetime' : request.COOKIES['last_login_datetime'],
    }
    return render(request, "todolist.html", context)

def show_json(request):
    data_todolist = todolist.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_todolist))

def add_todolist_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.COOKIES['last_login_datetime']
        description = request.POST.get("description")

        new_task = todolist(title=title, date=date, description=description)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login_datetime', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login_datetime')
    return response

def add_list_todo(request):
    if request.method == "POST":
        form = AddList(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/todolist/")
    else:
        form = AddList()
    return render(request, "addtask.html", {"form": form})