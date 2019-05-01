from django.db import models
import datetime

# Create your models here.

# Author model represents the author data


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=400)

    def __str__(self):
        return self.name

# Post Model represents the information about the post


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1600)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title


