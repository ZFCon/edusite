from pprint import pprint
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsActive, IsSuperUser
from django_filters import rest_framework as filters

from account.models import Account, Student, Teacher
from account.api.serializers import RegistrationSerializer, AccountPropertiesSerializer, StudentSerializer, UpdateStdSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

# Get All Account including Student, Teacher, Admin
class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = AccountPropertiesSerializer
    queryset = Account.objects.all()

# Get All Students Account
class AccountStudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication, SessionAuthentication, )
    serializer_class = StudentSerializer 
    queryset = Student.objects.all()

    def partial_update(self, request, pk=None):
        pprint(request.data)

        student = Student.objects.get(id=pk)
        serializer = UpdateStdSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get unregistered Students
class UnregStudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StudentSerializer
    queryset = Student.objects.filter(status=False)

# Get Students By Institute
class BSInstViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request):
        lookup_field = 'id'
        queryset = Student.objects.filter()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.filter(institute=pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


# Get Students By Institute & School
class BSSchoolViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, binst_pk=None):
        lookup_field = 'id'
        queryset = Student.objects.filter(institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, binst_pk=None):
        queryset = Student.objects.filter(school=pk, institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


# Get Students By Institute & School & Department
class BSDeptViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, binst_pk=None, bsch_pk=None,):
        queryset = Student.objects.filter(school=bsch_pk, institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, binst_pk=None, bsch_pk=None):
        queryset = Student.objects.filter(department=pk, school=bsch_pk, institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


# Get Students By Institute & School & Department & Class
class BSDptclsViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, binst_pk=None, bsch_pk=None, bdept_pk=None,):
        queryset = Student.objects.filter(department=bdept_pk, school=bsch_pk, institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, binst_pk=None, bsch_pk=None, bdept_pk=None,):
        queryset = Student.objects.filter(dptclass=pk, department=bdept_pk, school=bsch_pk, institute=binst_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered new user."
            data['email'] = account.email
            data['username'] = account.username
            data['user_type'] = account.user_type
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)



@api_view(['GET',])
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


@api_view(['PUT',])
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data ={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account update success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def logout_view(request):
    logout(request)

    data['success'] = 'Succeesfully logged out'
    return Response(data=data, status=status.HTTP_200_OK)