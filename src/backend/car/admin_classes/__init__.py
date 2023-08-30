from django.contrib import admin

from car.admin_classes.auto import AutoAdmin
from car.models import Auto

admin.site.register(Auto, AutoAdmin)
