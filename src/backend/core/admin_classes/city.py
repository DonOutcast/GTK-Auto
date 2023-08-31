from django.contrib import admin


class CityAdmin(admin.ModelAdmin):
    list_display = ["custom_title"]
    autocomplete_fields = ("country",)

    @admin.display(description="Название города", ordering="title")
    def custom_title(self, obj):
        return obj.title

