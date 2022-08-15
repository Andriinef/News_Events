from django import template
from django.db.models import Count

from events.models import Category

register = template.Library()


@register.simple_tag(name="get_list_categories")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("events/list_categories.html")
def show_categories(arg1, arg2):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('newsevents')).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
