from asyncio import events
from gc import get_objects
from multiprocessing import context
from urllib import request
from django.shortcuts import render, get_object_or_404


from .models import *

# Create your views here.


def index(request):
    news = NewsEvents.objects.all()
    context = {'news': news,
               'title': 'ІНФОРМАЦІЙНЕ АГЕНТСТВ',
               }
    return render(request, template_name='events/index.html', context=context)


def get_category(request, category_id):
  news = NewsEvents.objects.filter(cat_id=category_id)
  category = Category.objects.get(pk=category_id)
  return render(request, 'events/category.html', {'news': news, 'category': category})

def view_news(request, news_id):
  # news_item = NewsEvents.objects.get(pk=news_id)
  news_item = get_object_or_404(NewsEvents, pk=news_id)
  return render(request, "events/view_news.html", {"news_item": news_item})
