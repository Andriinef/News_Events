from .models import *
from django.db.models import Count


menu = [{'title': "НОВИНИ УКРАЇНИ", 'url_name': "home"},
        {'title': "Головна", 'url_name': "home"},
        {'title': "Додати новини", 'url_name': "add_news"},
        ]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        categorys = Category.objects.annotate(Count("newsevens"))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context["menu"] = user_menu
        context["categorys"] = categorys
        if "categorys_selected" not in context:
            context["categorys_selected"] = 0
        return context
