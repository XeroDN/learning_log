""" Defining URL patterns for the learning log application."""
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]