from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
]
