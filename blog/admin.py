from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Idea

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'published', 'published_at', 'is_submission', 
                    'reviewed', 'created_at')
    list_filter = ('published', 'is_submission', 'reviewed',)
    search_fields = ('title', 'body', 'submitter_name', 'submitter_email')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'published_at')
    summernote_fields = ('body',)


admin.site.register(Idea)