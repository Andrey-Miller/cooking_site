from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['display_user', 'display_birth_date', 'display_address']
    raw_id_fields = ['user']

    def display_user(self, obj):
        return f"{obj.user}"

    display_user.short_description = 'Пользователь'

    def display_birth_date(self, obj):
        return f"{obj.birth_date}"

    display_birth_date.short_description = 'Дата рождения'

    def display_address(self, obj):
        return f"{obj.address}"

    display_address.short_description = 'Адрес'
