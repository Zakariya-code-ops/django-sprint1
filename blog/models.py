from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)  # Место
    date = models.DateField()  # Дата
    category = models.CharField(max_length=50)  # Категория
    text = models.TextField()  # Полный текст
    preview_text = models.TextField()  # Краткое описание

    def __str__(self):
        return self.title
