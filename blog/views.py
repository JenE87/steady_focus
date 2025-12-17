from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Post, Idea
from .forms import IdeaForm


def home(request):
    """
    Display the homepage with a small selection of recent blog posts.

    Returns published instances of :model:`blog.Post` and displays them 
    in a limited, paginated preview to keep the homepage lightweight and
    distinct from the main blog listing.

    **Context**

    ``posts``
        A list of published :model:`blog.Post` objects for the current page.
    
    ``page_obj``
        A :class:`django.core.paginator.Page` instance.
    ``is_paginated``
        Boolean indicating whether pagination is required.
    
    **Template**

    :template:`blog/home.html`

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
    Display a paginated list of published blog posts.

    Returns published instances of :model:`blog.Post` and presents them
    in a responsive, mobile-first grid layout.

    **Context**
    ``post_list``
        A list of publisehd :model:`blog.Post` objects for the current page.
    ``page_obj``
        A :class:`django.core.paginator.Page` instance.
    ``is_paginated``
        Boolean indicating whether pagination is required.

    **Template**

    :template:`blog/post_list.html`
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
    """
    Display an individual blog post.

    Returns a single published instance of :model:`blog.Post` identified
    by its slug.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.

    **Template**
    :template:`blog/post_detail.html`.
    """
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def idea_submit(request):
    """
    Allow users to submit blog post ideas.

    Handles the submission of new instances of :model:`blog.Idea`
    using :form:`blog.IdeaForm`. Successful submissions provide
    user feedback and redirect back to the blog list.

    **Context**

    ``form``
        An instance of :form:`blog.IdeaForm`
    
    **Template**
    :template:`blog/idea_submit.html`
    """
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks - your idea has been submitted!")
            return redirect('blog:post_list')
    else:
        form = IdeaForm()
    return render(request, 'blog/idea_submit.html', {'form': form})
