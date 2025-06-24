# qotd/admin.py
from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote', 'url', 'source', 'created_at')
    search_fields = ('quote', 'author', 'source')
    list_filter = ('source', 'created_at')
