from django.contrib import admin

from car.models import Auto


class AutoAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "show_image"]
