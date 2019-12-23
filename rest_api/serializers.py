from rest_framework import serializers
from django.contrib.auth.models import User, Group

from works.models import Companies, Manager, Work, WorkPlace, WorkTime, Statistics, Worker


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Manager
        fields = ('url', 'name', 'company_name', 'user', 'company')


class CompaniesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Companies
        fields = ('url', 'company_name', 'pub_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')


    class Meta:
        model = Work
        fields = ['url', 'description', 'company_name', 'company', 'is_active']


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Worker
        fields = ['url', 'user_name', 'user']


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    stauts_str   = serializers.CharField(source='get_status_display')
    worker_name  = serializers.ReadOnlyField(source='worker.user.username')
    work_name    = serializers.ReadOnlyField(source='work.description')
    company_name = serializers.ReadOnlyField(source='work.company.company_name')

    class Meta:
        model = WorkPlace
        fields = ['url', 'work_name', 'company_name', 'work', 'stauts_str', 'status', 'worker_name', 'worker', 'status', 'is_copy', 'limit_hours']


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    stauts_str = serializers.CharField(source='get_status_display')
    date_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    date_end   = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)


    class Meta:
        model = WorkTime
        fields = ['url', 'date_start', 'date_end', 'status', 'stauts_str', 'work_place']


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    worker_name = serializers.ReadOnlyField(source='worker.user.username')

    class Meta:
        model = Statistics
        fields = ['url', 'number_weak', 'work_time_in_weak', 'worker_name', 'worker']
