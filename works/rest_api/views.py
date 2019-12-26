from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import renderers
from django.db.models import F
from django.shortcuts import get_object_or_404

from django.http import Http404
from django.contrib.auth.models import User, Group

from works.models import Companies, Manager, Work, Worker, WorkPlace, WorkTime, Statistics

from .serializers import (
    CompaniesSerializer, ManagerSerializer, UserSerializer, 
    GroupSerializer, WorkSerializer, WorkerSerializer, WorkPlaceSerializer, 
    WorkTimeSerializer, StatisticsSerializer, AccountSerializer,
    ManagerUsersSerializer, WorkerUsersSerializer, WorkPlaceTextSerializer,
    WorkTextSerializer, CompanyDetaliSerializer
)

from .permissions import IsOwnerOrReadOnly


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True)
    def works(self, request, pk):
        c = Companies.objects.get(pk=pk)
        queryset = c.work_set.all()
        serializer = WorkTextSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Companies.objects.all()
        сompany = get_object_or_404(queryset, pk=pk)
        serializer = CompanyDetaliSerializer(instance=сompany, context={'request': request})
        return Response(serializer.data)


class ManagersViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    @action(methods=['GET'], detail=False)
    def reviewers(self, request):
        queryset = User.objects.filter(groups__in='1')
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def managers(self, request):
        queryset = Manager.objects.all()
        serializer = ManagerUsersSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def workers(self, request):
        queryset = Worker.objects.all()
        serializer = WorkerUsersSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def super_users(self, request):
        queryset = User.objects.filter(is_superuser=True)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)



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
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=False)
    def status_new(self, request):
        queryset = WorkPlace.objects.filter(status='N')
        serializer = WorkPlaceTextSerializer(queryset, many=True)
        if len(serializer.data)<=0:
            return Response('No new wokers')
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def status_approved(self, request):
        queryset = WorkPlace.objects.filter(status='A')
        serializer = WorkPlaceTextSerializer(queryset, many=True)
        if len(serializer.data)<=0:
            return Response('No new wokers')
        return Response(serializer.data)

class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer
    permission_classes = (IsAuthenticated,)
    

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=False)
    def time_limit(self, request):
        queryset = Worker.objects.filter(statistics__work_time_in_weak__gte=F('workplace__limit_hours'))
        serializer = WorkerUsersSerializer(queryset, many=True)
        if len(serializer.data)<=0:
            return Response('No violation')
        return Response(serializer.data)