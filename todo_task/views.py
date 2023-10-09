from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import taskform
from .models import task
from users.models import userprofile
from datetime import date

#####################################################
#            User's home page                       #
#####################################################

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        uname = request.user.username
        ob= userprofile.objects.get(username=uname)
        obj= ob.task_set.all()
        incomplete_task = []
        completed_task = []
        Today = date.today()
        for i in obj:

            if f"markAsCompleted{i}" in request.POST:
                i.completed = True
                i.save()

            if f"markAsIncomplete{i}" in request.POST:
                i.completed = False
                i.save()

            if i.completed:
                completed_task.append(i)
            else:
                incomplete_task.append(i)


        return render(request,'todo_task/home.html',
                      {'incomplete':incomplete_task,'completed': completed_task, 'Today':Today})
    else:
        return redirect('/')




#####################################################
#           Adding new page                         #
#####################################################

@login_required(login_url='login')
def new_task(request):

    form = taskform()
    if request.method=="POST":
        form=taskform(request.POST)
        if form.is_valid():
            task_obj = form.save(commit=False)
            uname = request.user.username
            task_obj.user = userprofile.objects.get(username=uname)
            task_obj.save()
            return redirect('/')
    return render(request,'todo_task/new_task.html',{'form':form})

#####################################################
#           Edit or delete a task                   #
#####################################################

@login_required(login_url='login')
def details(request,taskid):
    obj1 = task.objects.get(id=taskid)
    obj = taskform(request.POST or None, instance=obj1)
    if 'save' in request.POST:
        if obj.is_valid():
            obj.save()
            return redirect(home)
    elif 'delete' in request.POST:
        return render(request,'todo_task/delete.html',{'task':obj1})


    else:
        return render(request,'todo_task/details.html',{'obj':obj})


def delete_task(request,taskid):
    obj1 = task.objects.get(id=taskid)
    if request.method=='POST':
        obj1.delete()
        return redirect(home)