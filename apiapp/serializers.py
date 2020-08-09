from rest_framework import serializers
from apiapp.models import Snippet

class SnippetSerializers(serializers.ModelSerializer):

    class Meta:
        model=Snippet
        fields='__all__'