from django.contrib import admin


from core.admin_classes.city import CityAdmin
from core.admin_classes.country import CountryAdmin
from core.models import Country, City


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
