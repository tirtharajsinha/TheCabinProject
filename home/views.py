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
from .models import Apps, SystemVar, Services
from django.contrib.auth import authenticate, login, logout
import requests


# superuser username- tirtharajsinha /  passward-tirtha098
# Create your views here.
# Create your views here.


def index(request):
    appview = SystemVar.objects.get(var="appview")
    apporder = SystemVar.objects.get(var="apporder")
    apporderlist = apporder.value.strip().split(",")
    removedApps = []
    apps = Apps.objects.all()
    appdict = {}
    applist = []
    for app in apps:
        appdict[app.id] = app

    for appid in apporderlist:
        if int(appid) in appdict.keys():
            applist.append(appdict.pop(int(appid)))
        else:
            removedApps.append(int(appid))

    for appid in appdict.keys():
        applist.append(appdict[int(appid)])

    if len(removedApps) > 0:
        refreshAppOrder(removedApps)
    # print(applist)
    # print(apporderlist)

    context = {
        "theme": getTheme(),
        "appview": appview.value,
        "apps": applist
    }
    return render(request, "index.html", context=context)


def appearance(request):
    appview = SystemVar.objects.get(var="appview")
    context = {
        "theme": getTheme(),
        "appview": appview.value
    }
    return render(request, "appearance.html", context=context)


def sysmonitor(request):
    context = {
        "theme": getTheme(),
        "pidata": pidata()
    }
    return render(request, "monitor.html", context=context)


def addapp(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        context = {"messages": "Please Sign in to add a new app."}
        return redirect("/login?next=/addapp")

    context = {
        "theme": getTheme()
    }
    if request.method == "POST":
        username = request.user.username
        icon = request.FILES['icon']
        name = request.POST.get("name")
        description = request.POST.get("sub")
        url = request.POST.get("url")
        checked = request.POST.get("pinned") == "ON"

        print(name, url, checked, username)
        # user = Upload(image=img, orgimage=orgimage,
        #               action=action, username=username)
        app = Apps(username=username, appname=name, description=description,
                   icon=icon,  url=url, pinned=checked)
        app.save()
        return render(request, "addapp.html", context=context)
    return render(request, "addapp.html", context=context)


def editapp(request, id):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        context = {"messages": "Please Sign in to update a app."}
        return redirect("/login?next=/editapp/"+id)

    context = {
        "theme": getTheme()
    }

    app = Apps.objects.get(id=id)

    if request.method == "POST":
        if not app:
            return redirect("/")
        username = request.user.username
        icon = request.FILES
        print(len(icon))
        if len(icon) == 1:
            icon = icon["icon"]
            app.icon = icon
        name = request.POST.get("name")
        description = request.POST.get("sub")
        url = request.POST.get("url")
        checked = request.POST.get("pinned") == "ON"

        app.appname = name
        app.description = description
        app.url = url
        app.pinned = checked

        print(icon, name, url, checked, username)
        app.save()
        return redirect("/")
    context["app"] = app
    return render(request, "editapp.html", context=context)


def logoutuser(request):
    logout(request)
    return redirect("/")


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login successful.")
            if next == "":
                next = "/"
            return redirect(next)
        else:
            context = {"messages": "Username or password is not correct"}
            print("Login Not successful.")
            if next != "":
                context["next"] = next
            return render(request, "login.html", context=context)
    next = request.GET.get("next")
    context = {}

    if next:
        if next == "/addapp":
            context["message"] = "Please Sign in to add a new app."
        context["next"] = next
        return render(request, "login.html", context=context)
    return render(request, "login.html")

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
    appview = request.GET.get("appview")

    if theme:
        dbtheme = SystemVar.objects.get(var="theme")
        dbtheme.value = theme
        dbtheme.save()
        print(theme)
    if accentcolor:
        dbaccentcolor = SystemVar.objects.get(var="accentcolor")
        dbaccentcolor.value = accentcolor
        dbaccentcolor.save()
    if appview:
        dbappview = SystemVar.objects.get(var="appview")
        dbappview.value = appview
        dbappview.save()

    return JsonResponse({"saved": True})


def saveAppOrder(request):
    apporder = request.GET.get("apporder")
    apporderlist = apporder.strip().split(",")
    print(apporderlist)
    dbapporder = SystemVar.objects.get(var="apporder")
    dbapporder.value = apporder
    dbapporder.save()

    return JsonResponse({"saved": True})


def refreshAppOrder(removedapps):
    print(removedapps)
    dbapporder = SystemVar.objects.get(var="apporder")
    apporder = dbapporder.value.strip().split(",")
    newapporder = [p for p in apporder if int(p) not in removedapps]
    dbapporder.value = ",".join(newapporder)
    dbapporder.save()
    print(removedapps, newapporder)


def updateAppPinnedState(request):
    appid = request.GET.get("appid")
    app = Apps.objects.get(id=appid)

    app.pinned = not app.pinned
    app.save()

    print(appid, app.pinned)
    return JsonResponse({"saved": True})


def checkurllive(request):
    url = request.GET.get("url")
    try:
        res = requests.get(url)
        return JsonResponse({"live": True})
    except:
        return JsonResponse({"live": False})
