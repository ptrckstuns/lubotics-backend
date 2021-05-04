from django.shortcuts import render
from .models import Post, Product
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
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
	return render(request, 'blog/products.html', {'title': 'Products', 'products': Product.objects.all()})

def contact(request):
	return render(request, 'blog/about.html', {'title': 'Contact'})

def chlog(request):
	return render(request, 'blog/chlog.html', {'title': 'Changelog'})

def cart(request):
	return render(request, 'blog/cart.html', {'title': 'My Cart'})	

# def profile(request):
# 	return render(request, 'blog/profile.html', {'title': 'Profile'})	

def wishlist(request):
	return render(request, 'blog/wishlist.html', {'title': 'My Wishlist'})	

def signup(request):
	return render(request, 'blog/signup.html', {'title': 'Sign Up'})	

def nav(request):
	return render(request, 'blog/nav.html', {'title': 'Nav template'})

def testproduct(request):
	return render(request, 'blog/testproduct.html', {'products': Product.objects.all()})

def testproduct1(request):
	return render(request, 'blog/testproduct1.html', {'products': Product.objects.all()})

# try
class TestProductView(generic.ListView):
    template_name = 'blog/testproduct2.jinja'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()
		# """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]