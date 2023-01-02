from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('api1',views.overviewapi1,name="api1"),
    path('api2',views.overviewapi2,name="api2"),
    path('api3',views.overviewapi3,name="api3")
]
