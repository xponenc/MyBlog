from django.urls import path

from .views import BlogDetailView, BlogListView, PostDetailView, PostListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blogs'

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("", BlogListView.as_view(), name="blogs"),
    path("create/", BlogCreateView.as_view(), name="blog-create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog-update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog-delete"),

    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("<int:blog_id>/posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
