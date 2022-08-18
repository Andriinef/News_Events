from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django. contrib.auth import login, logout


from .models import NewsEvents, Category
from .form import NewsForm, UserRegisterForm, UserLoginForm
from .utils import DataMixin

# Create your views here.


class HomeNews(DataMixin, ListView):
    model = NewsEvents
    # template_name = "events/index.html"
    context_object_name = "news"
    # extra_context = {"title": "ІНФОРМАЦІЙНЕ АГЕНТСТВ"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ІНФОРМАЦІЙНЕ АГЕНТСТВ"
        return context

    def get_queryset(self):
        return NewsEvents.objects.filter(is_published=True).select_related("cat")


# def index(request):
#     news = NewsEvents.objects.all()
#     context = {"news": news,
#                "title": "ІНФОРМАЦІЙНЕ АГЕНТСТВ",
#                }
#     return render(request, template_name="events/index.html", context=context)


class NewsByCategory(DataMixin, ListView):
    model = NewsEvents
    template_name = "events/category.html"
    context_object_name = "news"
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs["cat_slug"])
        return context

    def get_queryset(self):
        return NewsEvents.objects.filter(cat__slug=self.kwargs["cat_slug"], is_published=True).select_related("cat")


# def get_category(request, category_id):
#     news = NewsEvents.objects.filter(cat_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, "events/category.html", {"news": news, "category": category})


class ViewNews(DetailView):
    model = NewsEvents
    context_object_name = "news_item"
    # pk_url_kwarg = "news_id"


# def view_news(request, news_id):
#     # news_item = NewsEvents.objects.get(pk=news_id)
#     news_item = get_object_or_404(NewsEvents, pk=news_id)
#     return render(request, "events/view_news.html", {"news_item": news_item})


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = "events/add_news.html"
    # success_url = reverse_lazy("home")
    login_url = "/admin/"
    # raise_exception = True


# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             #news = NewsEvents.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, "events/add_news.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація пройшла успішно")
            return redirect("home")
        else:
            messages.success(request, "Помилка реєстрація")
    else:
        form = UserRegisterForm()
    return render(request, "events/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "events/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")
