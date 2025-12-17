"""
URL configuration for the pomodoro app.

Provides access to the public Pomodoro timer page.
"""

from django.urls import path
from . import views


app_name = "pomodoro"

urlpatterns = [
    path('', views.pomodoro_home, name='pomodoro_home'),
]
