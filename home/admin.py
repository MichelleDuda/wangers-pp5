from django.contrib import admin
from .models import ContactMessage, NewsletterSignup


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-submitted_at',)

@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined')
    search_fields = ('email',)
    readonly_fields = ('date_joined',)
    ordering = ('-date_joined',)
