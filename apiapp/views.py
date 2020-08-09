from django.shortcuts import render
from apiapp.serializers import SnippetSerializers
from rest_framework import viewsets
from apiapp.models import Snippet

# Create your views here.

class Snippetviewset(viewsets.ModelViewSet):
    serializer_class=SnippetSerializers
    queryset=Snippet.objects.all()