from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category
from collections import defaultdict
# Create your views here.


def all_menu_items(request):
    categories = Category.objects.all()
    items_by_category = []

    for category in categories:
        menu_items = MenuItem.objects.filter(category=category, is_available=True)
        if menu_items.exists():
            items_by_category.append((category, menu_items))

    context = {
        'items_by_category': items_by_category,
    }
    return render(request, 'menu/menu.html', context)


def menu_item_detail(request, menu_item_id):
    ''' A view to return an individual menu items details'''

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    sauces = menu_item.sauces.all()
    addons = menu_item.add_ons.all()

    context = {
        'menu_item': menu_item,
        'sauces': sauces,
        'addons': addons,
    }

    return render(request, 'menu/menu_item_detail.html', context)