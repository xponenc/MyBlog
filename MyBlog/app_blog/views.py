from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import BlogForm, PostForm
from .models import Blog, Post


class BlogDetailView(DetailView):
    """Детальный просмотр блога"""
    model = Blog
    post_set = Prefetch("post_set", queryset=Post.objects.exclude(draft=True))
    queryset = Blog.objects.select_related("author").prefetch_related(post_set).all()


class BlogListView(ListView):
    """Списковый просмотр Блогов"""
    model = Blog
    queryset = Blog.objects.select_related("author").all()
    paginate_by = 6


class BlogCreateView(UserPassesTestMixin, CreateView):
    """Создание Блога"""
    model = Blog
    form_class = BlogForm


    def test_func(self):
        current_blogs_counter = Blog.objects.filter(author=self.request.user).count()
        if current_blogs_counter >= self.request.user.profile.max_blogs:
            return False
        if not self.request.user.groups.filter(name__in=['Верифицированный пользователь']).exists():
            return False
        return True

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect(blog.get_absolute_url())
        return render(request, "app_blogs/blog_form.html", {'form': form})


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
    queryset = Post.objects.select_related("blog__author").exclude(draft=True)
    paginate_by = 6


class PostCreateView(CreateView):
    """Создание Поста"""
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        blog_id = self.kwargs['blog_id']
        blog = get_object_or_404(Blog, id=blog_id)
        form.instance.blog = blog
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blogs:blog-detail", kwargs={"pk": self.kwargs['blog_id']})

    # def post(self, request, blog_id):
    #     post_form = PostForm(request.POST)
    #     if post_form.is_valid():
    #         try:
    #             blog = Blog.objects.get(pk=blog_id)
    #         except ObjectDoesNotExist:
    #             post_form.add_error(None, "Блог не существует")
    #             return render(request, "app_blog/post_form.html", {"form": post_form})
    #         post = post_form.save(commit=False)
    #         post.blog = blog
    #         post.save()
    #         return redirect(self.get_success_url())
    #
    #     return render(request=request,
    #                   template_name="app_blog/post_form.html",
    #                   context={"form": post_form, }
    #                   )

class PostUpdateView(UpdateView):
    """Редактирование Поста"""
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    """Удаление Поста"""
    model = Post
