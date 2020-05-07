from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from school.models import School
from school.api.serializers import SchoolSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication): 

    def enforce_csrf(self, request):
        return

class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = SchoolSerializer 
    queryset = School.objects.all()


class ISchoolViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    def list(self, request, inst_pk=None,):
        queryset = School.objects.filter(sch_inst=inst_pk)
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None):
        queryset = School.objects.filter(id=pk, sch_inst=inst_pk)
        school = get_object_or_404(queryset, id=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)


