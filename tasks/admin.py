from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Task Model.

    Display task ownershp, completion status, and dates,
    and allows filtering and searching to support moderation
    and debugging during development.
    """
    list_display = ('title', 'owner', 'completed', 'due_date', 'created_at')
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'description')
