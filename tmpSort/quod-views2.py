# qotd/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Quote
from .serializers import QuoteSerializer
from .forms import QuoteForm
import random

@api_view(['GET'])
def random_quote(request):
    quotes = Quote.objects.all()
    if not quotes.exists():
        return Response({"error": "No quotes available"}, status=404)

    quote = random.choice(quotes)
    serializer = QuoteSerializer(quote)
    return Response(serializer.data)

@staff_member_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qotd:create_quote')
    else:
        form = QuoteForm()

    return render(request, 'qotd/create_quote.html', {'form': form})
