from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog

def post_list(request):
    posts = Blog.objects.all()
    return render(request, 'blog/post_list.html', locals())

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_detail.html', locals())


def post_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/post_edit.html', locals())

def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = BlogForm(instance=post)
    return render(request, 'blog/post_edit.html', locals())
