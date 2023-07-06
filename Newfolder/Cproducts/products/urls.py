from django.urls import include, path
from rest_framework import routers
from products.views import CustomerViewSet, ProductViewSet,set_product_inactive


urlpatterns = [
    path('users/<int:pk>',ProductViewSet.as_view(),name="product_details"),
    path('users',CustomerViewSet.as_view(),name="customer_details"),
    path('',set_product_inactive,name="counter")
]