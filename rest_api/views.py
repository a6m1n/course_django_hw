from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from django.http import Http404
from django.contrib.auth.models import User, Group

from works.models import Companies, Manager, Work, Worker, WorkPlace, WorkTime, Statistics

from .serializers import (
    CompaniesSerializer, ManagerSerializer, UserSerializer, 
    GroupSerializer, WorkSerializer, WorkerSerializer, WorkPlaceSerializer, 
    WorkTimeSerializer, StatisticsSerializer
)

class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer


class ManagersViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer
    

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
