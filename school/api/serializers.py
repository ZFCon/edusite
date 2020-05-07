from rest_framework import serializers 
from django.conf.urls import url, include

from school.models import School

class SchoolSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = School
        fields =  ['id', 'sch_inst', 'sch_abb', 'sch_name']  
