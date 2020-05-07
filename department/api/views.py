from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from department.models import Department
from department.api.serializers import DepartmentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication): 

    def enforce_csrf(self, request):
        return

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class IDeptViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request, inst_pk=None, sch_pk=None,):
        queryset = Department.objects.filter(dpt_sch=sch_pk)
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None, sch_pk=None):
        queryset = Department.objects.filter(id=pk, dpt_sch=sch_pk)
        dept = get_object_or_404(queryset, id=pk)
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data)