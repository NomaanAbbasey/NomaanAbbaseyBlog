from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Post,Author
from .forms import PostForm
# Create your views here.


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def post(request):
    authors = Author.objects.all()[::len(Author.objects.all())]
    return render(request, 'blog/post.html', {'authors': authors})


def publish(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            new_post = post.save()

        print(post)
    return HttpResponseRedirect(reverse('blog:index'))
