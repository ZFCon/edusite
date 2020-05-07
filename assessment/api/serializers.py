from rest_framework import serializers
from django.conf.urls import url, include

from assessment.models import Assessment 
from question.api.serializers import QuestionSerializer

class AssessmentSerializer(serializers.ModelSerializer):
    qtn_reg = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = ['id', 'as_ce', 'as_type', 'as_name', 'qtn_reg']

