"""
URL configuration for MyBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy("blogs:blogs"), permanent=True)),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('blogs/', include('app_blog.urls')),
    path('users/', include('app_users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)