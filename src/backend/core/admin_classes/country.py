from django.contrib import admin


class CountryAdmin(admin.ModelAdmin):
    list_display = ["custom_title"]
    search_fields = ("title",)

    @admin.display(description="Название страны", ordering="title")
    def custom_title(self, obj):
        return obj.title
