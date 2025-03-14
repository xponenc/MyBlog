import datetime
from django import template

register = template.Library()


@register.simple_tag
def blogs_limit_reached(test_u):
    """Проверка пользователя на максимальное количество разрешенных блоков"""
    current = len(test_u.blog_set.all())
    max_blogs = test_u.profile.max_blogs
    return current < max_blogs


@register.simple_tag
def check_post_pub_date(date):
    """Проверка даты публикации поста на будущее время"""
    return date > datetime.datetime.now().date()
