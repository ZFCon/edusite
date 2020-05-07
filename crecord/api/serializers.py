from rest_framework import serializers  
from django.conf.urls import url, include

from course.models import Course, CourseStudent
from student.api.serializers import StudentSerializer 
from teacher.api.serializers import TeacherSerializer

#class CourseSerializer(serializers.ModelSerializer):
#    tc_crse_reg = TeacherSerializer(many=True, read_only=True) 
#    sc_crse_reg = StudentSerializer(many=True, read_only=True) 

#    class Meta:
#        model = Course
#        fields = ('url', 'ce_dptcls', 'ce_abb', 'ce_name', 'tc_crse_reg', 'sc_crse_reg') 


class CRecordSerializer(serializers.ModelSerializer): 
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    class Meta:
        model = Course
        fields = ['id', 'ce_dptcls', 'ce_abb', 'ce_name', 'tc_crse_reg', 'sc_crse_reg', 'screcord']


class CStudentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CourseStudent
        fields = ['course', 'student']

    def to_representation(self, instance):
        rep = super(CStudentSerializer, self).to_representation(instance)
        rep['course name'] = instance.course.ce_name
        rep['course id'] = instance.course.id
        return rep


    
