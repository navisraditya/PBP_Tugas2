import datetime
from todolist.models import todolist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = todolist.objects.all()
    context = {
        'todolist' : data_todolist,
        'last_login' : request.COOKIES['last_login'],
        'last_login_datetime' : request.COOKIES['last_login_datetime'],
    }
    return render(request, "todolist.html", context)

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
            response.set_cookie('last_login', str(user.get_username))
            response.set_cookie('last_login_datetime', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('last_login_datetime')
    return response