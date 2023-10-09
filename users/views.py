from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import registrationform
from django.contrib import messages
from todo_task.views import home
from todo_task.models import task
from .models import userprofile

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        uname = request.POST['user_name']
        password = request.POST['password']
        valid_user = authenticate(request, username = uname, password = password )
        if valid_user is not None:
            login(request,valid_user)
            return redirect(request.GET['next'] if 'next' in request.GET else '/tasks')
        else:
            messages.error(request,"Username or password is incorrect")
    return render(request, 'users/login_page.html')

def signup(request):
    form = registrationform()
    if request.method == "POST":
        form = registrationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid data")

    return render(request, 'users/signup_page.html', {'form': form})

def logoutpage(request):
    logout(request)
    return redirect('/')
