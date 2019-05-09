from django import forms
from .models import Post, Author
from django.forms import ModelForm
import datetime

from django import forms

"""
Name: forms.py
Author: Nomaan Abbasey
Date: May 1, 2019
"""

# Post Form represents the form used to create a new post and save it to the db


class PostForm(forms.Form):

    title = forms.CharField(label='Title', max_length=100)
    pub_date = forms.DateTimeField(label='Date',  initial=datetime.datetime.now())
    description = forms.CharField(label='Description', max_length=1600, widget=forms.Textarea)

    class Meta:
        model = Post
