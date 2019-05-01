from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Post, Author
from .forms import PostForm
# Create your views here.

"""
Name: views.py
Author: Nomaan Abbasey
Date: May 1, 2019
"""

# index is the landing page view and renders index.html


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'blog/index.html', context)

# detail view render detail.html that displays whole blog post with option to edit or return to landing page


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

# post view renders the creation page for the creation of a blog post


def post(request):
    form = PostForm()
    return render(request, 'blog/post.html', {'form': form})


# publish view is used to take the POST request from post and create a new post. Then redirects to landing page.


def publish(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
           author = int(post.cleaned_data['author']) + 1
           title = post.cleaned_data['title']
           date = post.cleaned_data['pub_date']
           description = post.cleaned_data['description']
           p = Post()
           p.author = Author.objects.get(id=author)
           p.title = title
           p.pub_date = date
           p.description = description
           p.save()

    return HttpResponseRedirect(reverse('blog:index'))


# edit view renders the edit.html where the selected blog post can be edited


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/edit.html', {'post': post})

"""
 completeEdit view is used to take the POST request 
 from edit and update the blog post. Redirects back to that blog post
"""


def completeEdit(request, post_id):
    edit_Post = get_object_or_404(Post, pk=post_id)
    edit_Post.description = request.POST.get("description")
    edit_Post.save();
    return HttpResponseRedirect(reverse('blog:detail', args=(post_id,)))
