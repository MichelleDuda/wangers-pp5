from django.shortcuts import render, get_object_or_404
from .models import MenuItem
# Create your views here.


def all_menu_items(request):
    ''' A view to return the menu items'''

    from collections import defaultdict

    items_by_type = defaultdict(list)
    all_items = MenuItem.objects.all().order_by('item_type')

    for item in all_items:
        items_by_type[item.item_type].append(item)

    return render(request, 'menu/menu.html', {
        'items_by_type': dict(items_by_type),
    })


def menu_item_detail(request, menu_item_id):
    ''' A view to return an individual menu items details'''

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

    context = {
        'menu_item': menu_item,
    }

    return render(request, 'menu/menu_item_detail.html', context)