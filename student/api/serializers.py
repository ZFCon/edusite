from rest_framework import serializers 
from django.conf.urls import url, include

from student.models import Student, SCRecord
from course.models import Course


class SCourseSerializer(serializers.ModelSerializer): 
    parent_lookup_kwargs = {
		'student_id': 'student_id',
	}
    class Meta:
        model = Student
        fields = ['student_id', 'school', 'department', 'dptclass', 'course']
        

class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    class Meta:
        model = Student
        fields = ['student_id', 'courses']

    courses = SCourseSerializer(many=True, read_only=True)


class SCRecordSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
		'student_id': 'student_id',
	}
    class Meta:
        model = SCRecord
        fields = ['student', 'course', 'caone', 'catwo', 'midterm', 'cathree', 'cafour', 'project', 'exam', 'total', 'grade']





