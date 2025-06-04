from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Category, DietaryRestriction
from django.db.models import Q
from collections import defaultdict
from django.utils.safestring import mark_safe
from .forms import MenuItemForm

# Create your views here.


def all_menu_items(request):
    query = None
    categories = Category.objects.all()
    items_by_category = []
    dietary_restrictions = None

    if request.GET:
        if 'dietary_restriction' in request.GET:
            restriction_names = request.GET['dietary_restriction'].split(',')
            dietary_restrictions = DietaryRestriction.objects.filter(name__in=restriction_names)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))       

    for category in categories:
        menu_items = MenuItem.objects.filter(category=category, is_available=True)

        if dietary_restrictions:
            restriction_ids = dietary_restrictions.values_list('id', flat=True)
            menu_items = menu_items.filter(dietary_restriction__in=restriction_ids)

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
        'current_restrictions': dietary_restrictions,
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


@login_required
def add_menu_item(request):
    """ Add a menu item to the menu """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Menu Item!')
            return redirect(reverse('add_menu_item'))
        else:
            messages.error(request, 'Failed to add menu item. Please ensure the form is valid.')
    else:
        form = MenuItemForm()
    
    template = 'menu/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_menu_item(request, menuitem_id):
    """ Edit a menu item """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse('home'))

    menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menuitem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('menu_item_detail', args=[menuitem.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = MenuItemForm(instance=menuitem)
        messages.info(request, f'You are editing {menuitem.name}')

    template = 'menu/edit_menu_item.html'
    context = {
        'form': form,
        'menuitem': menuitem,
    }

    return render(request, template, context)

@login_required
def delete_menu_item(request, menuitem_id):
    """ Delete a menu item """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse('home'))

    menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
    menuitem.delete()
    messages.success(request, 'Menu Item deleted!')
    return redirect(reverse('menu'))