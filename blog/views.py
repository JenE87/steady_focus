from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Post, Idea
from .forms import IdeaForm


def post_list(request, template_name='blog/post_list.html'):
    posts = Post.objects.filter(published=True).order_by('-published_at')
    return render(request, template_name, {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def idea_submit(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks - your idea has been submitted!")
            return redirect('blog:home')
    else:
        form = IdeaForm()
    return render(request, 'blog/idea_submit.html', {'form': form})
