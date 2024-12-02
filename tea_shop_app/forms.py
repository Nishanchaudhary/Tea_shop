# forms.py
from django import forms
from .models import NewsletterSubscriber

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'style': 'padding: 10px; font-size: 1rem; border-radius: 5px; border: 2px solid #267e07; width: 100%;'
            })
        }
