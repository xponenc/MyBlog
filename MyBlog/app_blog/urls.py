from django.urls import path

from .views import BlogDetailView, BlogListView, PostDetailView, PostListView

app_name = 'blogs'

urlpatterns = [
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("", BlogListView.as_view(), name="blogs"),

    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="posts"),
]
