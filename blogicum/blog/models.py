from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Модель поста в блоге."""

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
    )
    text = models.TextField(verbose_name='Текст поста')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликован',
    )

    def __str__(self):
        """Возвращает заголовок поста."""
        return self.title

    class Meta:
        """Метаданные модели."""

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
