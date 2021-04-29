from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('product/', views.product, name='blog-product'),
    path('products/', views.products, name='blog-products'),
    path('contact/', views.about, name='blog-about'),
    path('changelog/', views.chlog, name='blog-chlog'),
    path('cart/', views.cart, name='blog-cart'),
    path('profile/', views.profile, name='blog-profile'),
    path('wishlist/', views.wishlist, name='blog-wishlist'),
    path('signup/', views.signup, name='blog-signup'),
    # path('login/', views.login, name='blog-login'),
]