from rest_framework import serializers 
from django.conf.urls import url, include

from teacher.models import Teacher
from course.models import Course
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from rest_framework_nested.relations import NestedHyperlinkedRelatedField


class TeacherSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'school', 'course']


class TCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'school', 'course']

    course = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,   # Or add a queryset
        view_name='teacher-course-detail',
        parent_lookup_kwargs={'teacher_id': 'teacher_id'}
    )
