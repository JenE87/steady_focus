import time
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    """
    Stores a single blog post entry.

    This model represents both published blog posts and
    user-submitted article ideas. Published posts are visible
    on the public blog, while submissions require an admin review 
    before publication.
    """
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
        """
        Automatically generate a unique slug and publication date.

        - Generates a URL-friendly slug from the title if none is provided.
        - Appends a timestamp suffic if a slug collision occurs.
        - Automatically sets the published date when a post is published.
        """
        if not self.slug and self.title:
            base_slug = slugify(self.title)[:185]    # Leave room for suffix
            slug_candidate = base_slug
            if (
                Post.objects.
                filter(slug=slug_candidate)
                .exclude(pk=self.pk)
                .exists()
            ):
                timestamp = time.strftime("%Y%m%d%H%M")    # e.g. 202511201023
                slug_candidate = f"{base_slug}-{timestamp}"
            self.slug = slug_candidate

        if self.published and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_submission:
            return f"{self.title} (submission)"
        return self.title


class Idea(models.Model):
    """
    Stores a single blog idea submission.

    This model allows users to submit blog topic suggestions
    or article drafts, which can later be reviewed and converted
    into published blog posts.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    submitter_name = models.CharField(max_length=200, blank=True)
    submitter_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.created_at.date()})"
