from django.test import TestCase
from .models import Page
# Create your tests here.


class PageModelTest(TestCase):
    """Тестирует создание и базовые свойства модели Page."""

    def test_page_creation(self):
        """Проверяет создание экземпляра модели Page."""
        page = Page.objects.create(
            title="Главная страница",
            slug="home",
            content="Содержание главной страницы",
        )
        self.assertEqual(page.title, "Главная страница")
        self.assertEqual(page.slug, "home")
        self.assertFalse(page.is_published)
