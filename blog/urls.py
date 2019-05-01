from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

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