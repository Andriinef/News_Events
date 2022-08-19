from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import NewsEvents, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsEvents
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "get_html_photo", "views",
                    "updated_at", "is_published", "cat")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "cat", "content",
              "photo", "get_html_photo", "views", "is_published", "created_at", "updated_at")
    readonly_fields = ("get_html_photo", "views", "created_at", "updated_at")
    save_on_top = True
    # save_as = True
    form = NewsAdminForm

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50>")

    get_html_photo.short_description = "Мініатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(NewsEvents, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
