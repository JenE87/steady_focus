from django.urls import path
from . import views


app_name = "pomodoro"

urlpatterns = [
    path('', views.pomodoro_home, name='pomodoro_home'),
]
