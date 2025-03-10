from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import BlogForm, PostForm
from .models import Blog, Post


class BlogDetailView(DetailView):
    """Детальный просмотр блога"""
    model = Blog
    queryset = Blog.objects.select_related("author").prefetch_related("post_set").all()


class BlogListView(ListView):
    """Списковый просмотр Блогов"""
    model = Blog
    queryset = Blog.objects.select_related("author").all()


class BlogCreateView(CreateView):
    """Создание Блога"""
    model = Blog
    form_class = BlogForm


class BlogUpdateView(UpdateView):
    """Редактирование Блога"""
    model = Blog
    form_class = BlogForm


class BlogDeleteView(DeleteView):
    """Удаление Блога"""
    model = Blog


class PostDetailView(DetailView):
    """Детальный просмотр Поста"""
    model = Post
    queryset = Post.objects.select_related("blog__author").all()


class PostListView(ListView):
    """Списковый просмотр Постов"""
    model = Post
    queryset = Post.objects.select_related("blog__author").all()


class PostCreateView(CreateView):
    """Создание Поста"""
    model = Post
    form_class = PostForm


class PostUpdateView(UpdateView):
    """Редактирование Поста"""
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    """Удаление Поста"""
    model = Post
