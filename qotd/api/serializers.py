# qotd/api/serializers.py

from rest_framework import serializers
from ..models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'url', 'source', 'created_at']
