from django import forms
from allauth.account.forms import LoginForm
from django import forms

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Форма відгуків"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
        self.fields['login'].label = ''
        self.fields['password'].label = ''