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
    return render(request, "index.html")

def check(request):
    return JsonResponse({"status":"connected"})

def poweroff(request):
    if request.method == "POST":
        sudopass = request.POST.get("sudopass")
        print(sudopass)
        command='echo "{}" | sudo poweroff'.format(sudopass)
        #feed=os.popen(command).read()
        #print(feed)
    return JsonResponse({"status":"connected"})

def reboot(request):
    if request.method == "POST":
        sudopass = request.POST.get("sudopass")
        print(sudopass)
        command='echo "{}" | sudo reboot'.format(sudopass)
        #feed=os.popen(command).read()
        #print(feed)
    return JsonResponse({"status":"connected"})

def mainsysteminfo(request):
    try:
        return JsonResponse(systeminfo())
    except Exception as e:
        return JsonResponse({"status":"error","log":str(e)})

def overviewapi1(request):
    try:
        return JsonResponse(mainsysteminfo1())
    except Exception as e:
        return JsonResponse({"status":"error","log":str(e)})

def overviewapi2(request):
    try:
        return JsonResponse(mainsysteminfo2())
    except Exception as e:
        return JsonResponse({"status":"error","log":str(e)})

def overviewapi3(request):
    # print(getCpuUsage())
    try:
        return JsonResponse(getCpuUsage())
    except Exception as e:
        return JsonResponse({"status":"error","log":str(e)})
