from rest_framework import serializers 
from django.conf.urls import url, include 

from lesson.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'le_name', 'le_note', 'le_video']  


                                            