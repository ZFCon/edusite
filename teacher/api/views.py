from pprint import pprint
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from teacher.models import Teacher
from teacher.api.serializers import TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class TCourseViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher_id']

