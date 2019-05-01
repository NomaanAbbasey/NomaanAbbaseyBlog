from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

"""
Name: urls.py
Author: Nomaan Abbasey
Date: May 1, 2019
"""

# manages all url routes/paths for django application and makes namespace visible

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('post', views.post, name='post'),
    path('publish/', views.publish, name='publish'),
    path('<int:post_id>/edit', views.edit, name='edit'),
    path('<int:post_id>/completeEdit', views.completeEdit, name='completeEdit')
]

urlpatterns += staticfiles_urlpatterns()