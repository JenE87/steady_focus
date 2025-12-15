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


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitter_name', 'submitter_email', 'created_at', 'reviewed')
    list_filter = ('reviewed', 'created_at')
    search_fields = ('title', 'body', 'submitter_name', 'submitter_email')
    ordering = ('-created_at',)
    actions = ['mark_reviewed', 'mark_unreviewed']

    def mark_reviewed(self, request, queryset):
        updated = queryset.update(reviewed=True)
        self.message_user(request, f"{updated} idea(s) marked as reviewed.")
    mark_reviewed.short_description = "Mark selected ideas as reviewed"

    def mark_unreviewed(self, request, queryset):
        updated = queryset.update(reviewed=False)
        self.message_user(request, f"{updated} idea(s) marked as unreviewed.")
    mark_unreviewed.short_description = "Mark selected ideas as unreviewed"
