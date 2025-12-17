"""
URL configuration for the Steady Focus project.

Routes incoming requests to the appropriate app URL configurations,
including authentication, blog, tasks, Pomodoro timer, and admins views.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('pomodoro/', include('pomodoro.urls', namespace='pomodoro')),
    path('summernote/', include('django_summernote.urls')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
