from rest_framework import serializers
from django.contrib.auth.models import User, Group

from works.models import Companies, Manager, Work, WorkPlace, WorkTime, Statistics, Worker


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Manager
        fields = ('url', 'id', 'name', 'company_name', 'user', 'company')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Work
        fields = ['url', 'id', 'description', 'company_name', 'company', 'is_active']


class CompaniesSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return Companies.objects.create(
            company_name=validated_data['company_name'],
            pub_date=validated_data['pub_date']
        )

    def update(self, instance, validated_data):

        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()

        return instance

    class Meta:
        model = Companies
        fields = ('url', 'id', 'company_name', 'pub_date',)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'id', 'name']




class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Worker
        fields = ['url', 'id', 'user_name', 'user']


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    stauts_str = serializers.CharField(source='get_status_display')
    worker_name = serializers.ReadOnlyField(source='worker.user.username')
    work_name = serializers.ReadOnlyField(source='work.description')
    company_name = serializers.ReadOnlyField(source='work.company.company_name')

    class Meta:
        model = WorkPlace
        fields = ['url', 'id', 'work_name', 'company_name', 'work', 'stauts_str', 'status', 'worker_name', 'worker', 'status', 'is_copy', 'limit_hours']


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    stauts_str = serializers.CharField(source='get_status_display')
    date_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    date_end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = WorkTime
        fields = ['url', 'id', 'date_start', 'date_end', 'status', 'stauts_str', 'work_place']


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    worker_name = serializers.ReadOnlyField(source='worker.user.username')

    class Meta:
        model = Statistics
        fields = ['url', 'id', 'number_weak', 'work_time_in_weak', 'worker_name', 'worker']

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class ManagerUsersSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Manager
        fields = ('id', 'name', 'company_name', 'user', 'company')

class WorkerUsersSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Worker
        fields = ['id', 'user_name', 'user']


class WorkPlaceTextSerializer(serializers.ModelSerializer):
    stauts_str = serializers.CharField(source='get_status_display')
    worker_name = serializers.ReadOnlyField(source='worker.user.username')
    work_name = serializers.ReadOnlyField(source='work.description')
    company_name = serializers.ReadOnlyField(source='work.company.company_name')

    class Meta:
        model = WorkPlace
        fields = ['id', 'work_name', 'company_name', 'work', 'stauts_str', 'status', 'worker_name', 'worker', 'status', 'is_copy', 'limit_hours']

class WorkTextSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Work
        fields = [ 'description', 'company_name', 'company', 'is_active']

class CompanyDetaliSerializer(serializers.Serializer):
    manager_set = ManagerSerializer(many=True, read_only=True)
    work_set = WorkSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class  = CompaniesSerializer
        model = Companies
        fields = ('url', 'id', 'company_name', 'pub_date', 'manager_set', 'work_set')

