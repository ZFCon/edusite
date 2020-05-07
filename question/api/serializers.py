from rest_framework import serializers 
from django.conf.urls import url, include 

from question.models import Question 

class QuestionSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Question
        fields = (
            'qtn', 
            'qtn_ans', 
            'qtn_opta', 
            'qtn_optb', 
            'qtn_optc', 
            'qtn_optd', 
            'qtn_opte'
        )
