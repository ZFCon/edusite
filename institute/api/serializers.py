from rest_framework import serializers 
from django.conf.urls import url, include

from institute.models import Institute

class InstituteSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = Institute
        fields =  ['id', 'abb', 'name'] 


class UpdateInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['id', 'abb', 'name']

    def validate_inst_id(self, pk):
        pprint(pk)

        existing = Institute.objects.filter(id=pk).count()
        pprint(existing)

        if existing > 1:
            raise serializers.ValidationError('Institute with this id exist')

        return abbr

    def validate(self, data): 
        pprint(data)
        return data
