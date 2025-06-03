from django.contrib import admin
from .models import Review, Like


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'user', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating', 'created_at')
    search_fields = ('user__username', 'menu_item__name', 'title', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Mark selected reviews as approved"

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'created_at') 
    search_fields = ('user__username', 'review__title')
    list_filter = ('created_at',)

admin.site.register(Like, LikeAdmin)
admin.site.register(Review, ReviewAdmin)