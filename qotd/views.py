# qotd/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Quote
from django.core.paginator import Paginator
from django import forms
from django.views.decorators.http import require_POST


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'url', 'source', 'approved']

def review_quotes(request):
    quotes = Quote.objects.all().order_by('-created_at')
    paginator = Paginator(quotes, 10)  # 10 per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'qotd/review_quotes.html', {'page_obj': page_obj})

def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)

    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('review_quotes')
    else:
        form = QuoteForm(instance=quote)

    return render(request, 'qotd/edit_quote.html', {'form': form, 'quote': quote})



@require_POST
def approve_all_quotes(request):
    Quote.objects.filter(approved=False).update(approved=True)
    return redirect('review_quotes')

@require_POST
def unapprove_all_quotes(request):
    Quote.objects.filter(approved=True).update(approved=False)
    return redirect('review_quotes')


def view_approved_quotes(request):
    quotes = Quote.objects.filter(approved=True).order_by('-created_at')
    paginator = Paginator(quotes, 10)  # 10 per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'qotd/view_quotes.html', {'page_obj': page_obj})
