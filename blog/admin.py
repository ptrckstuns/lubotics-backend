from django.contrib import admin
from .models import Post, Product, OrderProduct, Order, Wishlist

# Register your models here.
# admin.site.register(Post)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Wishlist)
# admin.site.register(Profile) 