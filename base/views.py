from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import Settings
from .forms import SettingsForm, LoginForm
import datetime


def home(request):
    page = "home"
    settings = Settings.objects.get(id=1)
    title = settings.name + " | Home"

    context = {"page": page, "title": title, "settings": settings}
    return render(request, "base/home.html", context)


def aboutPage(request):
    page = "about"
    settings = Settings.objects.get(id=1)
    title = settings.name + " | About"

    context = {"page": page, "title": title, "settings": settings}
    return render(request, "base/about.html", context)


def loginPage(request):
    page = "login"
    settings = Settings.objects.get(id=1)
    title = settings.name + " | Login"
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username OR password does not exist")

    context = {"page": page, "title": title, "settings": settings, "form": form}
    return render(request, "base/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


@login_required(login_url="/login")
def globalSettings(request):
    settings = Settings.objects.get(id=1)
    title = settings.name + " | Global Settings"

    if request.method == "POST":
        form = SettingsForm(request.POST, instance=settings)

        if form.is_valid():
            form.save()

            response = HttpResponseRedirect("/")

            return response

    else:
        form = SettingsForm(instance=settings)

    context = {"title": title, "settings": settings, "form": form}
    return render(request, "base/global_settings_form.html", context)
