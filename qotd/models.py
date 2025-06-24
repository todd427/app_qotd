# qotd/models.py
from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author}: {self.text[:50]}"

