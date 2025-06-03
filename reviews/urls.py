from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.create_review, name='add_review'), 
    path('add/<int:menu_item_id>/', views.create_review, name='add_review_for_item'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('like/<int:review_id>/', views.toggle_like, name='toggle_like'),
    path('', views.ReviewListView.as_view(), name='review_list'),
]