from django.urls import path
from django.views.decorators.cache import cache_page


from .views import *


urlpatterns = [
    # path("", index, name="home"),
    # path("", HomeNews.as_view(), name="home"),
    path("", cache_page(60) (HomeNews.as_view()), name="home"),
    # path("category/<slug:cat_slug>/", get_category, name="category"),
    path("category/<slug:cat_slug>/", NewsByCategory.as_view(), name="category"),
    # path("news/<int:news_id>/", view_news, name="view_news"),
    path("news/add_news/", CreateNews.as_view(), name="add_news"),
    path("news/<str:slug>/", ViewNews.as_view(), name="view_news"),
    #path("news/add_news/", add_news, name="add_news"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("search/", Search.as_view(), name="search"),
]
