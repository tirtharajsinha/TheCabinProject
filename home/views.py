from django.shortcuts import render, HttpResponse, redirect
from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from .utils import *

# superuser username-cabin /  passward-cabin
# Create your views here.
# Create your views here.


def index(request):
    return render(request, "index.html")



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
    print(getCpuUsage())
    try:
        return JsonResponse(getCpuUsage())
    except Exception as e:
        return JsonResponse({"status":"error","log":str(e)})