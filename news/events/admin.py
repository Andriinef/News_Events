from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "get_html_photo",
                    "updated_at", "is_published", "cat_id")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "cat", "content",
              "photo", "get_html_photo", "views", "is_published", "created_at", "updated_at")
    readonly_fields = ("get_html_photo", "views", "created_at", "updated_at")
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50")

    get_html_photo.short_description = "Мініатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(NewsEvents, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
