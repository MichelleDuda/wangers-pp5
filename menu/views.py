from django.shortcuts import render
from .models import MenuItem
# Create your views here.


def all_menu_items(request):
    ''' A view to retrun the menu items'''

    menu_items = MenuItem.objects.all()

    context = {
        'menu_items': menu_items,
    }
    
    return render(request, 'menu/menu.html', context)