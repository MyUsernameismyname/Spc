from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0] == '?':
            raise ValidationError('Текст заголовка не может начинаться с "?"')

        return title
