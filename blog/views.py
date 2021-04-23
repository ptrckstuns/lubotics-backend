from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def product(request):
	return render(request, 'blog/product.html', {'title': 'Product'})

def products(request):
	return render(request, 'blog/products.html', {'title': 'Products'})