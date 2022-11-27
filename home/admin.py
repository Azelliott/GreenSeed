from django.contrib import admin
from .models import ContactForm

# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_added',
        'message',
    )

    ordering = ('date_added',)

admin.site.register(ContactForm, ContactFormAdmin)


