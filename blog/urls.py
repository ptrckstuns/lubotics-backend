from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "lubotics"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('products/<str:category>', views.ProductCategoryView.as_view(), name='products-category'),
    path('products/search/', views.search_products, name='products-search'),
    path('cart/', views.CartDetail.as_view(), name='cart'),
    path('cart/add/<slug>', views.add_to_cart, name='add-to-cart'),
    path('cart/add/b/<slug>', views.buy_now, name='buy-now'),
    path('cart/remove/<slug>', views.remove_from_cart, name='remove-from-cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('wishlist/add/<slug>', views.add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/remove/<slug>', views.remove_from_wishlist, name='remove-from-wishlist'),
    path('nav/', views.cart, name='nav'),
    path('products/view/<slug>', views.ProductDetailView.as_view(), name='product'),



]

                          
# testproduct/category/1
# URLS 
#  home - ''
#  profile / wishlist
#  

# user
## sign up
# - date joined
# - username
# - password
# - email
## edit 
# - profile-picture
# - birthday 
# - address

# - wishlist [ list of products ]
# - cart [ list of products ] 
# - purchases [ list of products ]

# productsffffff
# - id
# - picture
# - description
# - features
# - price
# - category


# featured products list [ icacall nalang yung ID ]
# best selling  [ icacall nalang yung ID ]

# cart -> checkout button -> # payment form -> mawawala sa cart | order

## dito malilink ng sa HOME and footer
# products/humanoids
# products/education
# products/drones 
# products/etc
