from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('posts', views.post_lists, name='post_lists'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<str:pk>', views.post_detail, name='post_detail'),
    path('post/<str:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<str:pk>/delete', views.post_delete, name='post_delete'),
]
