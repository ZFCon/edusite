from rest_framework import serializers 
from django.conf.urls import url, include

from dptclass.models import DptClass

class DptClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = DptClass
        fields = ['id', 'dcls_dpt', 'dcls_abb', 'dcls_name', ] 

