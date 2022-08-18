from django import forms
from .models import NewsEvents, Category
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label="Назва", widget=forms.TextInput(
#         attrs={"class": "form-control"}))
#     content = forms.CharField(label="Текст", required=False, widget=forms.Textarea(
#         attrs={"class": "form-control",
#             "rows": 5}))
#     is_published = forms.BooleanField(label="Опубліковувати", initial=True)
#     cat = forms.ModelChoiceField(
#         empty_label="Оберіть категорію", label="Категорії", queryset=Category.objects.all(),
#         widget=forms.Select(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Категорія не обрана"

    class Meta:
        model = NewsEvents
        fields = ["title", "slug", "content", "photo", "is_published", "cat"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "cat": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r'\d', title):
            raise ValidationError("Назва не повинна починатися з цифри")
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='Логін повинен складатися максимум із 150 символів',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', help_text="user@user.com",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text="Пароль має складатися не менше 8 символів",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
