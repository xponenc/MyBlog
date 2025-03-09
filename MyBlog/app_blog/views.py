from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Blog, Post


class BlogDetailView(DetailView):
    """Детальный просмотр блога"""
    model = Blog
    queryset = Blog.objects.select_related("author").prefetch_related("post_set").all()


class BlogListView(ListView):
    """Списковый просмотр Блогов"""
    model = Blog
    queryset = Blog.objects.select_related("author").all()


class PostDetailView(DetailView):
    """Детальный просмотр Поста"""
    model = Post
    queryset = Post.objects.select_related("blog__author").all()


class PostListView(ListView):
    """Списковый просмотр Постов"""
    model = Post
    queryset = Post.objects.select_related("blog__author").all()

