# qotd/views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm

@staff_member_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_quote')
    else:
        form = QuoteForm()

    return render(request, 'qotd/create_quote.html', {'form': form})
