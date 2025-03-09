import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from app_blog.models import Blog, Post

fake = Faker()


class Command(BaseCommand):
    help = "Создает тестовые блоги и посты для всех пользователей"

    def handle(self, *args, **options):
        self.stdout.write("Create USER")

        users = self.create_test_user(user_counter=4)
        self.create_blogs_and_posts(users=users)

        self.stdout.write((self.style.SUCCESS("Products created")))

    @staticmethod
    def create_test_user(user_counter: int = 1):
        bulk_container = []
        for _ in range(user_counter):
            username = fake.user_name()
            email = fake.email()
            password = "test123"
            is_superuser = False
            bulk_container.append(
                User(
                    username=username,
                    email=email,
                    password=password,
                    is_superuser=is_superuser, )
            )
        users = User.objects.bulk_create(bulk_container)
        return users

    @staticmethod
    def create_blogs_and_posts(users, n_blogs=3, m_posts=5):
        """Создает n блогов с m постами для каждого пользователя из списка."""
        for user in users:
            for _ in range(n_blogs):
                blog = Blog.objects.create(
                    author=user,
                    name=fake.unique.company()
                )
                print(f"Created blog: {blog.name} for user {user.username}")

                for _ in range(m_posts):
                    post = Post.objects.create(
                        blog=blog,
                        title=fake.unique.sentence(nb_words=6),
                        content=fake.text(max_nb_chars=1000),
                        draft=random.choice([True, False])
                    )
                    print(f"\tCreated post: {post.title} in blog {blog.name}")


