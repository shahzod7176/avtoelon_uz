from django.urls import path
from apps.views import ProductListView, ProductDetailView, home_view, redirect_to_products

urlpatterns = [
    path('', home_view, name='home'),
    path('', redirect_to_products, name='product'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
