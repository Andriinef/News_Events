from turtle import title
from django.db import models

# Create your models here.
class NewsEvents(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статті")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Час створення")
    updated_at =models.DateTimeField(auto_now_add=True, verbose_name="Час зміни")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Публікація")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорії")


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
