from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Provides primary key type for tasks app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
