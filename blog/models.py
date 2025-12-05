import time
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    excerpt = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    is_submission = models.BooleanField(default=False)
    submitter_name = models.CharField(max_length=200, blank=True)
    submitter_email = models.EmailField(blank=True)
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['published', 'published_at']),
        ]
    
    def save(self, *args, **kwargs):
        # Simple slug auto-generation if slug is not provided
        if not self.slug and self.title:
            base_slug = slugify(self.title)[:185] # leave room for suffix
            slug_candidate = base_slug
            # If a slug collision exists, append a timestamp suffix
            if Post.objects.filter(slug=slug_candidate).exclude(pk=self.pk).exists():
                timestamp = time.strftime("%Y%m%d%H%M") # e.g. 20251120 1023
                slug_candidate = f"{base_slug}-{timestamp}"
            self.slug = slug_candidate
        
        # Auto-set published_at when selecting published
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if not self.is_submission else f"{self.title} (submission)"

class Idea(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    submitter_name = models.CharField(max_length=200, blank=True)
    submitter_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.created_at.date()})"