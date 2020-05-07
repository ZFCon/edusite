from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes  
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from assessment.models import Assessment
from student.models import Student
from teacher.models import Teacher
from student.api.serializers import StudentSerializer
from teacher.api.serializers import TeacherSerializer
from assessment.api.serializers import AssessmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()

class StudentCourse(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class TeacherCourse(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SCAssessViewSet(viewsets.ViewSet):
    serializer_class = AssessmentSerializer

    def list(self, request, student_pk=None, course_pk=None):
        queryset = Assessment.objects.filter(as_ce=course_pk)
        serializer = AssessmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, student_pk=None, course_pk=None):
        queryset = Assessment.objects.filter(id=pk, as_ce=course_pk)
        assessment = get_object_or_404(queryset, id=pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)


class IAssessViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()

    def list(self, request, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None, crse_pk=None,):
        queryset = Assessment.objects.filter(as_ce=crse_pk)
        serializer = AssessmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, inst_pk=None, sch_pk=None, dept_pk=None, dptcls_pk=None, crse_pk=None,):
        queryset = Assessment.objects.filter(id=pk, as_ce=crse_pk)
        assessment = get_object_or_404(queryset, id=pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)