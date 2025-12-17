from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Stores a single task entry related to :model:`auth.User`.

    This model represents an individual to-do item created by a user.
    Tasks can optionally include a description, due date, and estimated 
    completion time, and support completion tracking.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    estimated_minutes = models.PositiveIntegerField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"
