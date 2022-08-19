from django.db import models
from django.urls import reverse


class NewsEvents(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статті")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Час публікації")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Час зміни")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Публікація")
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="Категорії")
    views = models.IntegerField(verbose_name="Перегляди", default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новини"
        verbose_name_plural = "Новини"
        ordering = ["-created_at", "id"]


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категорії"
        verbose_name_plural = "Категорії"
        ordering = ["id"]
