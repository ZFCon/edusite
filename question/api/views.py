from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from question.models import Question
from question.api.serializers import QuestionSerializer
  

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()