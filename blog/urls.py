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
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('nav/', views.cart, name='nav'),
    # path('changelog/', views.chlog, name='chlog'),
    path('testproduct/', views.testproduct, name='testproduct'),
    path('testproduct1/', views.testproduct1, name='testproduct1'),
    path('testproduct2/', views.TestProductView.as_view(), name='testproduct2'),

    # path('wishlist/', views.wishlist, name='blog-wishlist'),
    path('signup/', views.signup, name='blog-signup'),
    # path('testmedia/', views.media, name='media'),
    # path('login/', views.login, name='blog-login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
                          
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
