from rest_framework import viewsets

from .models import myuser,company
from .serializers import UserSerializer,CompanySerializer
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
class CompanyViewSet(viewsets.ModelViewSet):

    queryset = company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = myuser.objects.all()
    serializer_class = UserSerializer



@login_required
def mysport(request):
	#bus_ns,buss_img=sports()
	return render(request=request,template_name="sports.html", context={"bus_ns":bus_ns,"buss_img":buss_img})


@login_required
def mybusiness(request):
	#bus_ns,buss_img=bussiness()
	return render(request=request,template_name="market.html", context={"bus_ns":bus_ns,"buss_img":buss_img})
	


def myhome(request):
	return render(request=request,template_name="login.html",context={})

@login_required
def show(request):
	return render(request=request,template_name="index.html",context={})