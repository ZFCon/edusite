from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive, IsSuperUser

from book.models import Book
from book.api.serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()