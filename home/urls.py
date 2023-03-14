from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('check', views.check, name="check"),
    path('poweroff', views.poweroff, name="poweroff"),
    path('reboot', views.reboot, name="reboot"),
    path('api1', views.api1, name="api1"),
]
