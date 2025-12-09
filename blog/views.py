from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Post, Idea
from .forms import IdeaForm


def home(request):
    """
    Home view: render blog/home.html with a small list of latest posts.
    Keeps the homepage separate from the paginated post_list.
    """
    posts_qs = Post.objects.filter(published=True).order_by('-created_at')

    paginator = Paginator(posts_qs, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/home.html', {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        })


def post_list(request, *args, **kwargs):
    """
    Function-based post list view with pagination (mobile-first grid).
    Shows 6 posts per page by default.
    """
    qs = Post.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(qs, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def idea_submit(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks - your idea has been submitted!")
            return redirect('blog:post_list')
    else:
        form = IdeaForm()
    return render(request, 'blog/idea_submit.html', {'form': form})
