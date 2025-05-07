from django.contrib import admin
from .models import MenuItem, Category, Sauce, DietaryRestriction, AddOn


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Sauce)
admin.site.register(DietaryRestriction)
admin.site.register(AddOn)