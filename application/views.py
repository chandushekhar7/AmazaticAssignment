from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .Serializers import *
from rest_framework.decorators import api_view
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['GET','POST'])
def login(request):

    # user=User.objects.get(id=id)
    data=request.data
    username = data['username']
    password = data['password']
    from django.contrib.auth import authenticate, login
    user = authenticate(username=username, password=password)
    if user:
        login(request,user)
        return Response('login successfully')
    else:
        return Response('you need to login first to access that record')

class RegisterAPI(ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class EmployeeCRUD(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [AllowAny]
