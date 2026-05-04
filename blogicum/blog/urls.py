from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
=======
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # ← ВАЖНО
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
>>>>>>> 9fd46ef (Исправил замечания ревьюера)
]
