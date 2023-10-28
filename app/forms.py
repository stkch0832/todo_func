from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
        )
    status = forms.ChoiceField(
        label='ステータス',
        choices=Post.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    deadline = forms.DateTimeField(
        label='期限',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
            })
    )
    description = forms.CharField(
        label='詳細',
        max_length=255,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )
