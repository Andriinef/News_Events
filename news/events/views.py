from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
  news = NewsEvents.objects.order_by('-created_at')
  context = {'news': news,
            'titel': 'Сисок новостей'
  }
  return render(request, 'events/index.html', context)
