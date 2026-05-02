from django.contrib import admin
from .models import Page, MenuItem
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Админ‑панель для Page: отображение, фильтрация, поиск, авто‑slug."""

    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Админ‑панель для MenuItem: редактирование порядка и активности."""

    list_display = ('name', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
