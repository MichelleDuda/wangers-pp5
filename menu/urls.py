from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_menu_items, name='menu'),
    path('<menu_item_id>', views.menu_item_detail, name='menu_item_detail'),
]
