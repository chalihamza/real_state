from django.contrib import admin
from django.utils.html import format_html

from news.models import Blognews


class BlognewsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30px" style="border-radius:20px" />'.format(object.Cover_pic.url))

    thumbnail.short_description = 'book pic'
    list_display = ('id', 'thumbnail', 'Category', 'name', 'date')
    list_display_links = ('id', 'Category')
    search_fields = ('name', 'Category')
    list_filter = ('Category',)


admin.site.register(Blognews, BlognewsAdmin)
