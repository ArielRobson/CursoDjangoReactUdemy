from base import Base
from companies.utils.permissions import EmployeesPermission, GroupsPermission
from companies.models import Employee, Enterprise
from companies.serializers import EmployeeSerializer, EmployeesSerializer

from accounts.auth import Authentication
from accounts.models import User, User_Groups

from rest_framework.views import Response, status
from rest_framework.exceptions import APIException

class Employee(Base):
    permission_classes = [EmployeesPermission]

    def get(self, request):
        enterprise_id = self.get_enterpise_id(request.user.id)

        #Get owner of enterprise
        owner_id = Enterprise.objects.values('user_id').filter(id=enterprise_id).first()['user_id']

        employees = Employee.objects.filter(enterprise_id=enterprise_id).exclude(user_id=owner_id).all()
        