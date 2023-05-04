from django import forms
from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Форма відгуків"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    """Форма добавлення рейтингу"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)