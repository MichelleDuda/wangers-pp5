from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'menu_item', 'title', 'body']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'type': 'range',
                'min': 1,
                'max': 5,
                'class': 'form-range',
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'menu_item': forms.Select(attrs={'class': 'form-control'}),
        }
