from django.apps import AppConfig


class PomodoroConfig(AppConfig):
    """
    Provides primary key type for pomodoro app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pomodoro'
