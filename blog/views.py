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

def contact(request):
	return render(request, 'blog/about.html', {'title': 'Contact'})

def chlog(request):
	return render(request, 'blog/chlog.html', {'title': 'Changelog'})

def cart(request):
	return render(request, 'blog/cart.html', {'title': 'My Cart'})	

def profile(request):
	return render(request, 'blog/profile.html', {'title': 'Profile'})	

def wishlist(request):
	return render(request, 'blog/wishlist.html', {'title': 'My Wishlist'})	

def signup(request):
	return render(request, 'blog/signup.html', {'title': 'Sign Up'})	