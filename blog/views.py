from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post,Author
# Create your views here.


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = Author.objects.filter(id=post.author_id)
    return render(request, 'blog/detail.html', {'post': post, 'author': author})


def post(request, post_id):
    return HttpResponse("Added Post %s." % post_id)

