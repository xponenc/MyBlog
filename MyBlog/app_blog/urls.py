from django.urls import path

from .views import BlogDetailView, BlogListView, PostDetailView, PostListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blogs'

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("", BlogListView.as_view(), name="blogs"),
    path("create/", BlogCreateView.as_view(), name="blog-create"),
    path("update/", BlogUpdateView.as_view(), name="blog-update"),
    path("delete/", BlogDeleteView.as_view(), name="blog-delete"),

    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/update/", PostUpdateView.as_view(), name="post-update"),
    path("posts/delete/", PostDeleteView.as_view(), name="post-delete"),
]
