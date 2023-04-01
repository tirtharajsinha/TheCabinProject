from django.contrib import admin
from django.urls import path, include, re_path
from home import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.png', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', views.index, name="home"),
    path('appearance', views.appearance, name="appearance"),
    path('addapp', views.addapp, name="addapp"),
    path('monitor', views.sysmonitor, name="monitor"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),



    path('savetheme', views.saveTheme, name="savetheme"),
    path('saveapporder', views.saveAppOrder, name="saveapporder"),
    path('appstatuschange', views.updateAppPinnedState,
         name="pdateAppPinnedState"),
    path('check', views.check, name="check"),
    path('poweroff', views.poweroff, name="poweroff"),
    path('reboot', views.reboot, name="reboot"),
    path('api1', views.api1, name="api1"),
    path('api2', views.api2, name="api2"),
]
