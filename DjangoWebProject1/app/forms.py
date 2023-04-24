"""
Definition of forms.
"""

from re import L
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Вас зовут', min_length=2, max_length=100)
    country = forms.CharField(label='Выживете в стране', min_length=2, max_length=100)
    city = forms.CharField(label='Вы живете в городе', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1', 'Мужской'), ('2', 'Женский')],
                             widget=forms.RadioSelect, initial=1)
    notice = forms.BooleanField(label='Вы хотите получать новости с сайта на e-mail?',
                                required=False)
    email = forms.EmailField(label='Укажите Ваш e-mail', min_length=7)
    message = forms.CharField(label='Отзыв о нашем сайте',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
