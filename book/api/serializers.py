from rest_framework import serializers 
from django.conf.urls import url, include

from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bk_dpt', 'bk_title']
