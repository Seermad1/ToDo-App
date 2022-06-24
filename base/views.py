from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Task, User
from .form import MyUserCreationForm, EditUserForm
from django.contrib import messages
import datetime

# Create your views here.


@login_required(login_url="login")
def homepage(request):
    mydate = datetime.datetime.now()
    day = mydate.strftime("%A")
    date = mydate.strftime("%d")
    month = mydate.strftime("%B")

    q = request.GET.get("q") if request.GET.get("q") != None else ""
    user = request.user
    tasks = user.task_set.filter(title__icontains=q)
    if request.method == "POST":
        task = request.POST.get("added-item")
        Task.objects.create(
            user=request.user,
            title=task,
        )
        return redirect("home")


    context = {"tasks": tasks, "day": day, "month": month, "date": date}
    return render(request, "home.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not  None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, 'Password incorrect.')
        except:
            messages.error(request, "Email doesn't exist.")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login")



def register_user(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            # login(request, user)
            return  redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("home")


def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = EditUserForm(instance=user)
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect("home") 
    context = {"form": form}
    return render(request, "update.html",context)