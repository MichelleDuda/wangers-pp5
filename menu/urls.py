from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_menu_items, name='menu'),
    path(
        '<int:menu_item_id>/',
        views.menu_item_detail,
        name='menu_item_detail'
    ),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path(
        'edit/<int:menuitem_id>',
        views.edit_menu_item,
        name='edit_menu_item'
    ),
    path(
        'delete/<int:menuitem_id>',
        views.delete_menu_item,
        name='delete_menu_item',
    ),
]
