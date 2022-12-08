from django.contrib import admin
from django.utils.html import format_html

from house.models import House_property


class House_propertyAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.image.url))

    thumbnail.short_description = 'house pic'
    list_display = ('id', 'thumbnail', 'address', 'city', 'date')
    list_display_links = ('id', 'address')
    list_filter = ('city',)
    search_fields = ('state', 'city')


admin.site.register(House_property, House_propertyAdmin)
