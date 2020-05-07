from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from dptclass.models import DptClass
from dptclass.api.serializers import DptClassSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

# Baseless Class Lookup
class DptClassViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsSuperUser,)
    serializer_class = DptClassSerializer
    queryset = DptClass.objects.all()

# Class Lookup based on Institute, School and Department
class IDptclsViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = DptClassSerializer
    queryset = DptClass.objects.all()

    def list(self, request, inst_pk=None, sch_pk=None, dept_pk=None,):
        queryset = DptClass.objects.filter(dcls_dpt=dept_pk)
        serializer = DptClassSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None, sch_pk=None, dept_pk=None,):
        queryset = DptClass.objects.filter(id=pk, dcls_dpt=dept_pk)
        dptcls = get_object_or_404(queryset, id=pk)
        serializer = DptClassSerializer(dptcls)
        return Response(serializer.data)