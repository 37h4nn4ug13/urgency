from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

from users.forms import NewUserForm
# Create your views here.

@csrf_protect
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    context = {

    }
    return render(request, "users/login.html", context)


@csrf_protect
def logoutView(request):
    # IF user is authenticated. 
    logout(request)
    return redirect("login")


@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    form = NewUserForm()
    context = {
        "form": form,
    }
    return render(request, 'users/register.html', context)


