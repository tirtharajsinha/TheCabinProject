from django.shortcuts import render, HttpResponse, redirect
from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from .utils import *
import os
from .models import Apps, AppOrder, SystemVar, Services

# superuser username-cabin /  passward-cabin
# Create your views here.
# Create your views here.


def index(request):
    context = {
        "theme": getTheme()
    }
    return render(request, "index.html", context=context)


def manageapp(request):
    context = {
        "theme": getTheme()
    }
    return render(request, "manageapp.html", context=context)


def appearance(request):
    context = {
        "theme": getTheme()
    }
    return render(request, "appearance.html", context=context)


def sysmonitor(request):
    context = {
        "theme": getTheme(),
        "pidata": pidata()
    }
    return render(request, "monitor.html", context=context)


def addapp(request):
    context = {
        "theme": getTheme(),
    }
    if request.method == "POST":
        username = request.user.username
        icon = request.FILES['icon']
        name = request.POST.get("name")
        description = request.POST.get("sub")
        url = request.POST.get("url")
        checked = request.POST.get("pinned") == "on"

        print(name, url, checked, username)
        # user = Upload(image=img, orgimage=orgimage,
        #               action=action, username=username)
        app = Apps(username=username, appname=name, description=description,
                   icon=icon,  url=url, pinned=checked)
        app.save()
        return render(request, "addapp.html", context=context)
    return render(request, "addapp.html", context=context)

###############
####  APIs ####
###############


def check(request):
    return JsonResponse({"status": "connected"})


def poweroff(request):
    if request.method == "POST":
        sudopass = request.POST.get("sudopass")
        print(sudopass)
        command = 'echo "{}" | sudo poweroff'.format(sudopass)
        # feed=os.popen(command).read()
        # print(feed)
    return JsonResponse({"status": "connected"})


def reboot(request):
    if request.method == "POST":
        sudopass = request.POST.get("sudopass")
        print(sudopass)
        command = 'echo "{}" | sudo reboot'.format(sudopass)
        # feed=os.popen(command).read()
        # print(feed)
    return JsonResponse({"status": "connected"})


def api1(request):
    data = pidata()
    return JsonResponse({"data": data})


def api2(request):
    data = pidataReload()
    return JsonResponse({"data": data})


def getTheme():
    accentList = ["#c7053d", "#4058F2", "#0FD267", "#EABE10",
                  "#EA9E10", "#EA1093", "#5910EA", "#479dbb", "#09bb90", "#3f8ff7"]

    theme = SystemVar.objects.get(var="theme")
    accentcolor = SystemVar.objects.get(var="accentcolor")
    theme = {
        "themeName": theme.value,
        "accentColor": accentcolor.value
    }
    print(theme)
    return theme


def saveTheme(request):
    theme = request.GET.get("theme")
    accentcolor = request.GET.get("accentcolor")

    if theme:
        dbtheme = SystemVar.objects.get(var="theme")
        dbtheme.value = theme
        dbtheme.save()
        print(theme)
    if accentcolor:
        dbaccentcolor = SystemVar.objects.get(var="accentcolor")
        dbaccentcolor.value = accentcolor
        dbaccentcolor.save()

        print(accentcolor)

    return JsonResponse({"saved": True})
