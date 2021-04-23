from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('product/', views.product, name='blog-product'),
    path('products/', views.products, name='blog-products'),
]