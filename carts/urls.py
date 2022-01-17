from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index,name='index'),
    path('account',Register,name='account'),
    path('blog-archive',blog_archives,name='blog-archive'),
    path('blog-single/<int:id>',blog_single,name='blog-single'),
    path('product',product,name='product'),
    path('mens/<int:category_id>',Men,name='mens'),
    path('womens/<int:category_id>',Women,name='womens'),
    path('sports/<int:category_id>',sports,name='sports'),
    path('electronics/<int:category_id>',electronics,name='electronics'),
    path('furniture/<int:category_id>',Furniture,name='furniture'),
    path('wishlist/<int:product_id>',wishlist,name='wishlist'),   
    path('logout',user_logout,name="logout"),
    path('add_cart/<int:product_id>',add_cart,name="add_cart"),
    path('complete_remove/<int:product_id>',complete_remove,name="complete_remove"),
    path('remove_quantity/<int:product_id>',remove_quantity,name="remove_quantity"),
    path('cart_detail',cart_detail,name="cart_detail"),
    path('checkout/',checkout,name="checkout"),
    path('wishlist_detail',wishlist_detail,name="wishlist_detail"),
    path('complete_remove_wishlist/<int:product_id>',complete_remove_wishlist,name="complete_remove_wishlist"),

    

    # path('Comment',comm,name='Comment'),

]