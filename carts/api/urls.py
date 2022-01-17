from .views import *
from django.urls import path,include
from rest_framework import routers

#API router config
router = routers.DefaultRouter()
router.register('Product',Product_add_update_delete)
router.register('Category',Category_add_update_delete)
router.register('Poster',Poster_add_update_delete)
router.register('cart_items',Cart_view)
#API urls
urlpatterns = [
    path('',include(router.urls)),
    path('product_list',product_list.as_view()),
    path('category_list',Category_list.as_view()),
    path('comment',Comment_list.as_view()),
    path('comment/<int:pk>',Comment_delete.as_view()),
    path('poster',Poster_list.as_view()),
   
]