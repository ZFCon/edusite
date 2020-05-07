from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from course.models import Course, CourseStudent
from course.api.serializers import CourseSerializer, CStudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class CourseViewSet(viewsets.ModelViewSet):  
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class SCourseViewSet(viewsets.ViewSet):
    serializer_class = CourseSerializer 

    def list(self, request, student_pk=None,):
        queryset = CourseStudent.objects.filter(student=student_pk)
        serializer = CStudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, student_pk=None):
        queryset = CourseStudent.objects.filter(course=pk, student=student_pk)
        course = get_object_or_404(queryset, course=pk)
        serializer = CStudentSerializer(course)
        return Response(serializer.data)


class ICrseViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None,):
        queryset = Course.objects.filter(ce_dptcls=dptcls_pk)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None,):
        queryset = Course.objects.filter(id=pk, ce_dptcls=dptcls_pk)
        dptcls = get_object_or_404(queryset, id=pk)
        serializer = CourseSerializer(dptcls)
        return Response(serializer.data)

