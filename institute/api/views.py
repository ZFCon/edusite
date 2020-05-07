from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from institute.models import Institute
from institute.api.serializers import InstituteSerializer, UpdateInstSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class InstituteViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication, SessionAuthentication, )
    serializer_class = InstituteSerializer 
    queryset = Institute.objects.all()

    def partial_update(self, request, pk=None):
        pprint(request.data)

        institute = Institute.objects.get(id=pk)
        serializer = UpdateInstSerializer(institute, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DInstViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = InstituteSerializer
    queryset = Institute.objects.all()

    def list(self, request,):
        lookup_field = 'id'
        queryset = Institute.objects.filter()
        serializer = InstituteSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Institute.objects.filter()
        institute = get_object_or_404(queryset, id=pk)
        serializer = InstituteSerializer(institute)
        return Response(serializer.data)