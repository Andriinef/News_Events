from django import template
from django.db.models import Count, F

from events.models import Category

register = template.Library()


@register.simple_tag(name="get_list_categories")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("events/list_categories.html")
def show_categories(category_class="category"):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count(
        'newsevents', filter=F("newsevents__is_published"))).filter(cnt__gt=0)
    return {"categories": categories, "category_class": category_class}
