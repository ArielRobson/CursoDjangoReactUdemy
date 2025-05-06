from rest_framework import serializers
from companies.models import Employee, Task
from accounts.models import User_Groups, User, Group, Group_Permissions

from django.contrib.auth.models import Permmission

class EmployeesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email'
        )

    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email',
            'groups'
        )

    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email