from .models import Post, Author

"""
Name: utils.py
Author: Nomaan Abbasey
Date: May 9, 2019
"""



# gets query set of authors and passes it to list so that it may be unloaded for use


def authorchoices():
    author_list = Author.objects.values_list('name', flat=True)
    author_value = []
    for i in range(0, len(author_list)):
        author_value.append(i)
    authors = list(zip(author_value, author_list))
    return authors
