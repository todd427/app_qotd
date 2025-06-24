# qotd/urls.py
from django.urls import path
from . import views

app_name = 'qotd'

urlpatterns = [
    path('api/random/', views.random_quote, name='random_quote'),
    path('create/', views.create_quote, name='create_quote'),
]
