
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include, url
app_name="myapi"

urlpatterns = [
	path("",views.myhome, name="myhome"),
    path("login",views.login, name="mylogin"),

]
