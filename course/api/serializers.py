from rest_framework import serializers  
from django.conf.urls import url, include

from course.models import Course, CourseStudent, CourseSRecord
from student.api.serializers import StudentSerializer, SCRecordSerializer
from teacher.api.serializers import TeacherSerializer

class CSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSRecord
        fields = ['course', 'screcord']

        
class CourseSerializer(serializers.ModelSerializer): 
    tc_crse_reg = TeacherSerializer(many=True, read_only=True)  
    sc_crse_reg = StudentSerializer(many=True, read_only=True)
    screcord = SCRecordSerializer(many=True, read_only=True)
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





    
