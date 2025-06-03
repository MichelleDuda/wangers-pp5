from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'menu_item', 'title', 'body']
        widgets = {
            'rating': forms.RadioSelect(),
        }