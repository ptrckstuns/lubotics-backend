from django.contrib import admin
from .models import Post, Product, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Profile)