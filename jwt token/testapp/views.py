from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    permission_classes = [IsAdminUser,]
    # ******to overside global setting only for this class , allowany authentication is used
    # permission_classes = [AllowAny, ]
