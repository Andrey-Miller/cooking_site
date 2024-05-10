from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Recipe, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['display_id', 'title', 'category', 'cooking_time', 'author']
    list_filter = ['products', 'cooking_time']
    readonly_fields = ['preview']
    search_fields = ['description']
    search_help_text = 'Поиск рецепта по описанию'
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title']
            }
        ),
        (
            'Описание рецепта',
            {
                'description': 'Подробная информация о рецепте',
                'fields': ['description', 'cooking', 'cooking_time'],
            }
        ),
        (
            'Продукты',
            {
                'description': 'Продукты для приготовления',
                'fields': ['products'],
            }
        ),
        (
            'Изображение',
            {
                'description': 'Добавить изображение',
                'fields': ['image'],
            }
        ),
        (
            'Превью',
            {
                'fields': ['preview'],
            }
        ),
        (
            'Прочее',
            {
                'classes': ['collapse'],
                'description': 'Категория и автор рецепта',
                'fields': ['category', 'author'],
            }
        ),
    ]

    def display_id(self, obj):
        return f"Рецепт №{obj.id}"

    display_id.short_description = 'Рецепт'

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 200px; height: auto;" alt="Нет изображение">')

    preview.short_description = 'Изображение'