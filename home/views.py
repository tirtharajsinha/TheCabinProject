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
        "theme": getTheme,
        "pidata": pidata()
    }
    return render(request, "monitor.html", context=context)


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
    theme = {
        "themeName": "dark",
        "accentColor": accentList[0]
    }
    return theme
