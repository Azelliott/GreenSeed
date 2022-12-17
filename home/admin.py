from django.contrib import admin
from .models import ContactForm, NewsletterForm


# ContactFormAdmin
class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_added',
        'message',
    )

    ordering = ('date_added',)

    search_fields = ('name', 'email', 'message')
    list_per_page = 25


admin.site.register(ContactForm, ContactFormAdmin)


# NewsletterFormAdmin
class NewsletterFormAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_added',
    )

    ordering = ('date_added',)
    search_fields = ('email',)
    list_per_page = 25


admin.site.register(NewsletterForm, NewsletterFormAdmin)
