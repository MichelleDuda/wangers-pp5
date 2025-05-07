from django.contrib import admin
from .models import MenuItem, Category, Sauce, DietaryRestriction, AddOn


class MenuItemAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'item_type',
        'price',
    )

    ordering = ('name',)

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category)
admin.site.register(Sauce)
admin.site.register(DietaryRestriction)
admin.site.register(AddOn)