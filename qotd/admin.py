# qotd/admin.py
from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'approved', 'created_at')
    list_filter = ('approved', 'author')
    search_fields = ('text', 'author', 'source', 'url')
    ordering = ('-created_at',)
    actions = ['approve_quotes']

    @admin.action(description='Mark selected quotes as approved')
    def approve_quotes(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} quotes marked as approved.")
