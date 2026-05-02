from django.test import TestCase
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):
    """Тестирует базовую функциональность модели Post."""

    def test_post_creation(self):
        """Проверяет создание экземпляра модели Post."""
        post = Post.objects.create(
            title="Тестовый пост",
            text="Содержание тестового поста",
        )
        self.assertEqual(post.title, "Тестовый пост")
        self.assertIn("Содержание", post.text)
