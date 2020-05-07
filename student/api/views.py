from pprint import pprint
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from student.models import Student, SCRecord
from student.api.serializers import StudentSerializer, SCRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token


class StudentViewSet(viewsets.ModelViewSet):  
    permission_classes = (IsSuperUser,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class PStudentViewSet(viewsets.ViewSet):
    serializer_class = StudentSerializer

    def list(self, request,):
        lookup_field = 'student_id'
        queryset = Student.objects.filter()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.filter()
        student = get_object_or_404(queryset, student_id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class SCRecordViewSet(viewsets.ViewSet):
    serializer_class = SCRecordSerializer 

    def list(self, request, student_pk=None, course_pk=None):
        queryset = SCRecord.objects.filter(student=student_pk, course=course_pk)
        serializer = SCRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, student_pk=None, course_pk=None):
        queryset = SCRecord.objects.filter(id=pk, student=student_pk, course=course_pk)
        course = get_object_or_404(queryset, course=pk)
        serializer = SCRecordSerializer(course)
        return Response(serializer.data)
    



#class SCourseViewSet(viewsets.ModelViewSet):
#    filter_backends = [DjangoFilterBackend]
#    filterset_fields = ['student_id',]
#
#    def get_queryset(self):
#        return Student.objects.filter(student_id)