from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):
    news = NewsEvents.objects.all()
    categories = Category.objects.all()
    context = {'news': news,
               'title': 'ІНФОРМАЦІЙНЕ АГЕНТСТВ',
               'categories': categories,
               }
    return render(request, template_name='events/index.html', context=context)


def get_category(request, category_id):
  news = NewsEvents.objects.filter(cat_id=category_id)
  categories = Category.objects.all()
  category = Category.objects.get(pk=category_id)
  return render(request, 'events/category.html', {'news': news, 'categories': categories, 'category': category})
