from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginView(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")

    context = {

    }
    return render(request, "users/login.html", context)


def logoutView(request):
    # IF user is authenticated. 
    logout(request)
    return redirect("login")
