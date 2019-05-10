from rest_framework import viewsets

from .models import myuser,company
from .serializers import UserSerializer,CompanySerializer

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
class CompanyViewSet(viewsets.ModelViewSet):

    queryset = company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = myuser.objects.all()
    serializer_class = UserSerializer

def myhome(request):
	return render(request=request,template_name="login.html",context={})


def login(request):
	return render(request=request,template_name="index.html",context={})