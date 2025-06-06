from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_full_name',
        'default_phone_number',
        'default_town_or_city',
        'default_postcode',
    )
    search_fields = (
        'user__username',
        'default_full_name',
        'default_phone_number',
        'default_town_or_city',
        'default_postcode',
    )
    list_filter = ('default_town_or_city', 'default_state')


admin.site.register(UserProfile, UserProfileAdmin)