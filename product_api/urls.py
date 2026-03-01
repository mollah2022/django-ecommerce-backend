from rest_framework import routers
from .views import *
from django.urls import re_path,include



router = routers.DefaultRouter()
router.register('product',ProductViewSet,basename='product')
router.register('cart_items',CartItemViewSet,basename='cart_item')
router.register('order',OrderViewSet,basename='order')


urlpatterns = [
    re_path(r'^',include(router.urls)),
]
