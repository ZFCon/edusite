from rest_framework import serializers 
from django.conf.urls import url, include

from department.models import Department

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'dpt_sch', 'dpt_abb', 'dpt_name'] 

