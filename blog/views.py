from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post,Author
# Create your views here.


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    authors = Author.objects.all()
    latest_post_authors = []
    for item in latest_post_list:
        latest_post_authors.append(authors.filter(id=item.author_id))

    blogLandingDict = dict(zip(latest_post_authors, latest_post_list))
    context = {
        'blogLandingDict': blogLandingDict,
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    return HttpResponse("Welcome to Post %s." % post_id)


def post(request, post_id):
    return HttpResponse("Added Post %s." % post_id)

