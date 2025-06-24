# qotd/api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Quote
from .serializers import QuoteSerializer
import random

@api_view(['GET'])
def random_quote(request):
    quotes = Quote.objects.filter(approved=True)
    if not quotes.exists():
        return Response({"error": "No approved quotes available"}, status=404)

    quote = random.choice(quotes)
    serializer = QuoteSerializer(quote)
    return Response(serializer.data)
