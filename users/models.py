from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    address = models.TextField(blank=True, verbose_name='Адрес')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Автора рецепта'
        verbose_name_plural = 'Авторы рецептов'


