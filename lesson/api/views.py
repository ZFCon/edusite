from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from lesson.models import Lesson
from student.models import Student
from teacher.models import Teacher
from lesson.api.serializers import LessonSerializer
from student.api.serializers import StudentSerializer
from teacher.api.serializers import TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class SCLessonViewSet(viewsets.ViewSet):
    serializer_class = LessonSerializer

    def list(self, request, student_pk=None, course_pk=None):
        queryset = Lesson.objects.filter(course=course_pk)
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, student_pk=None, course_pk=None):
        queryset = Lesson.objects.filter(id=pk, course=course_pk)
        lesson = get_object_or_404(queryset, id=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)


class SLesson(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']

class TLesson(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']


class ILessonViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def list(self, request, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None, crse_pk=None,):
        queryset = Lesson.objects.filter(course=crse_pk)
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None, crse_pk=None):
        queryset = Lesson.objects.filter(id=pk, course=crse_pk)
        lesson = get_object_or_404(queryset, id=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)