from django import forms

from app_blog.models import Blog, Post


class BlogForm(forms.ModelForm):
    """Форма создания/редактирования объекта app_blog:Blog"""
    class Meta:
        model = Blog
        fields = ("name", )


class PostForm(forms.ModelForm):
    """Форма создания/редактирования объекта app_blog:Post"""
    class Meta:
        model = Post
        fields = ("title", "content", "draft")
