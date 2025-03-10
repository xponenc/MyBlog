from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """Модель Блога"""
    author = models.ForeignKey(User, verbose_name="автор", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="название", max_length=200, unique=True)
    created_at = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="дата редактирования", auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogs:blog-detail', kwargs={"pk": self.pk})


class Post(models.Model):
    """Модель Поста"""
    blog = models.ForeignKey(Blog, verbose_name="блог", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="название", max_length=200, unique=True)
    content = models.TextField(verbose_name="содержание")
    draft = models.BooleanField(verbose_name="Черновик", default=False)
    created_at = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="дата редактирования", auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at", "-updated_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post-detail', args=[str(self.id)])
