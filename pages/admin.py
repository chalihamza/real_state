from django.contrib import admin
from django.utils.html import format_html

from pages.models import Agent, Testimonial


class AgentAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.image.url))

    thumbnail.short_description = 'Car image'
    list_display = ('id', 'thumbnail', 'FirstName', 'date')
    list_display_links = ('id', 'FirstName')
    search_fields = ('FirstName',)
    list_filter = ('FirstName',)


admin.site.register(Agent, AgentAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'date')
    list_display_links = ('id', 'Name')


admin.site.register(Testimonial, TestimonialAdmin)
