from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views


from myapi import views as main_api
router = routers.DefaultRouter()
router.register(r'user', main_api.UserViewSet)
router.register(r'company', main_api.CompanyViewSet)

urlpatterns = [
    url(r'^', include('myapi.urls')),
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="try.html"), name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
    #url(r'^login/', include('dash.urls')),

]

