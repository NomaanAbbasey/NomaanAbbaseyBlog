from django import forms
from .models import Post, Author
from django.forms import ModelForm
import datetime

from django import forms


def authorchoices():
    author_list = Author.objects.values_list('name', flat=True)
    author_value = []
    for i in range(0, len(author_list)):
        author_value.append(i)
    authors = list(zip(author_value, author_list))
    return authors


class PostForm(forms.Form):
    author = forms.ChoiceField(choices=authorchoices())
    title = forms.CharField(label='Title', max_length=100)
    pub_date = forms.DateTimeField(label='Date',  initial=datetime.datetime.now())
    description = forms.CharField(label='Description', max_length=1600, widget=forms.Textarea)

    class Meta:
        model = Post
