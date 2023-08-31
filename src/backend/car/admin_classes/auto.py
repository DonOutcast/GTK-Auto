from django.contrib import admin
from django.utils.html import format_html

from car.models import Auto


class AutoAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "show_image"]
    filter_vertical = ("country", "city")

    @admin.display(description="Изображение", ordering="image")
    def show_image(self, obj):
        if obj.image:
            return format_html(
                '<img src={} style="width: 60px; height: 60px;"/>', obj.image.url
            )
        else:
            return format_html(
                '<span style="color: red;">Нету фото<span/>'
            )
