from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import MenuItem, Category
from django.db.models import Q
from collections import defaultdict
from django.utils.safestring import mark_safe

# Create your views here.


def all_menu_items(request):
    query = None
    categories = Category.objects.all()
    items_by_category = []

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))       

    for category in categories:
        menu_items = MenuItem.objects.filter(category=category, is_available=True)

        if query:
            search_filter = Q(name__icontains=query) | Q(description__icontains=query)
            menu_items = menu_items.filter(search_filter)

        if menu_items.exists():
            items_by_category.append((category, menu_items))
    
    if query and not items_by_category:
        messages.info(
            request, 
            mark_safe("Even our wings have limits — for now. Craving something we don’t serve? Hit our <a href='/contact/'>contact form</a> and help us spread our... wings.")
        )
        return redirect(reverse('menu'))

    context = {
        'items_by_category': items_by_category,
        'search_term': query,
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