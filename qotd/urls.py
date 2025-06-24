# qotd/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review_quotes, name='review_quotes'),
    path('review/edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('approve-all/', views.approve_all_quotes, name='approve_all_quotes'),
    path('unapprove-all/', views.unapprove_all_quotes, name='unapprove_all_quotes'),
]
