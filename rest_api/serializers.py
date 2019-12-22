from rest_framework import serializers
from works.models import Companies, Manager
from django.contrib.auth.models import User, Group


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')

    class Meta:
        model = Manager
        fields = ('url', 'name', 'company_name', 'user', 'company')


class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    # manager_set = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='manager-detail')

    class Meta:
        model = Companies
        fields = ('url', 'company_name', 'pub_date', 'manager_set')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
