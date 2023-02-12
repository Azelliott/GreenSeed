from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

    rating = forms.DecimalField(min_value=1.0, max_value=5.0, decimal_places=1)