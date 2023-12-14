from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="dashboard" ),
    path('customur/', customur_list, name="customur_list" ),
    path('block/customur/', block_customur_list, name="block_customur_list" ),
    path('deleted/customur/',deleted_customur_list, name="deleted_customur_list" ),
    path('customur/profile/',profile, name="customur_profile" ),
    path('customur/profile/<int:id>/',customur_profile, name="customur_profile" ),
    path('search/customur/',search_customur, name="search_customur" ),
    path('email/marketing',email_marketing, name="email_marketing" ),
    path('product/pricing/',ProductAndPricing, name="product_pricing" ),
    path('subscribe/plan/',subscribe_plan, name="subscribe_plan" ),
    path('signin/',signin, name="signin" ),
    path('logout/',logout, name="logout" ),
    path('checkout/buy/<int:id>',checkout_buy,name="checkout_buy"),
    path('checkout/subscribe/<int:id>',checkout_subscribe,name="checkout_sub"),
    
    
]