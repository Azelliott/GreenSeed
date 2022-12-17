from django import forms
from .models import ContactForm, NewsletterForm


# Contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False


# Newsletter form
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterForm
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
        }

        self.fields['email'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-0 form-control pe-3 ps-3'
            self.fields[field].label = False
