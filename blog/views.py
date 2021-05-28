# from django.shortcuts import render
# from django.core.exeptions import ObjectDoesNotExist
from .models import Post, Product, OrderProduct, Order, Wishlist
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, View
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ProductCategoryView(generic.ListView):
	template_name = 'blog/products.html'
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.filter(category_slug=self.kwargs['category'])

def search_products(request):
	if request.method == "POST":
		searched = request.POST['searched']
		products = Product.objects.filter(name__contains=searched)

		if not products.exists():
			products = []

		return render(request, 'blog/products.html', {'products': products, 'searched': searched})
	else:
		return redirect("lubotics:products")

class CartDetail(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
		except Exception:
			order = []
			# return redirect("/")
		finally:
			context = {
				'title': 'My Cart',
				'object': order
			}
			return render(self.request, 'blog/cart.html', context)

class ProductDetailView(DetailView):
	model = Product
	template_name = 'blog/product.html'


@login_required
def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug=product.slug).exists():
			order_product.quantity += 1
			order_product.save()
		else:
			order.products.add(order_product)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user = request.user, ordered_date=ordered_date)
		order.products.add(order_product)
	messages.success(request, f'Added item to cart')
	# return redirect("lubotics:product", slug=slug)
	return redirect("lubotics:products")

@login_required
def buy_now(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug=product.slug).exists():
			order_product.quantity += 1
			order_product.save()
		else:
			order.products.add(order_product)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user = request.user, ordered_date=ordered_date)
		order.products.add(order_product)
	messages.success(request, f'Added item to cart')
	# return redirect("lubotics:product", slug=slug)
	return redirect("lubotics:cart")

@login_required
def add_to_wishlist(request, slug):
	product = get_object_or_404(Product, slug=slug)
	wishlist_qs = Wishlist.objects.filter(user=request.user)

	if wishlist_qs.exists(): # wishlist for user exist in the db
		wishlist = wishlist_qs[0] 
		if wishlist.products.filter(slug=product.slug).exists(): # product exists already
			messages.warning(request, f'Product already in wishlist')
		else: # product is not in wishlist
			wishlist.products.add(product)
			messages.success(request, f'Added product to wishlist')

	else: # user does not have a wishlist in the db
		wishlist = Wishlist.objects.create(user = request.user)
		wishlist.products.add(product)
		messages.success(request, f'Added product to wishlist')

	# return redirect("lubotics:product", slug=slug)
	return redirect("lubotics:products")
	
@login_required
def remove_from_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order_qs = Order.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug=product.slug).exists():
			order_product = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)[0]
			order_product.delete() # remove the order_product instance in the array
			order.products.remove(order_product)
		else:
			messages.warning(request, f'Order does not contain this item')
			return redirect("lubotics:product", slug=slug)

	else:
		messages.warning(request, f'User does not have an order')
		return redirect("lubotics:product", slug=slug)

	messages.warning(request, f'Removed item from cart')
	return redirect("lubotics:cart")

@login_required
def checkout(request):
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]

		order_products = order.products.all()
		order_products.update(ordered=True)
		for order_product in order_products:
			order_product.save()
		order.ordered = True
		order.save()
		
		messages.success(request, f'Your order was successful!!')
		return redirect("lubotics:cart")
	else:
		messages.warning(request, f'User does not have an order')
		return redirect("lubotics:cart")

@login_required
def remove_from_wishlist(request, slug):
	product = get_object_or_404(Product, slug=slug)
	wishlist_qs = Wishlist.objects.filter(user=request.user)

	if wishlist_qs.exists():
		wishlist = wishlist_qs[0]
		if wishlist.products.filter(slug=product.slug).exists():
			wishlist.products.remove(product)
			messages.warning(request, f'Removed item from wishlist')
		else:
			messages.warning(request, f'Wishlist does not contain this item')
			return redirect("profile")
	else:
		messages.warning(request, f'User does not have a wishlist')
		return redirect("profile")

	return redirect("profile")


# @login_required
# def add_to_wishlist(request, slug):
# 	product = get_object_or_404(Product, slug=slug)
# 	# order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
# 	wishlist_qs = Wishlist.objects.filter(user=request.user)

# 	if order_qs.exists():
# 		order = order_qs[0]
# 		if order.products.filter(product__slug=product.slug).exists():
# 			order_product.quantity += 1
# 			order_product.save()
# 		else:
# 			order.products.add(order_product)
# 	else:
# 		ordered_date = timezone.now()
# 		order = Order.objects.create(user = request.user, ordered_date=ordered_date)
# 		order.products.add(order_product)
# 	messages.success(request, f'Added item to cart')
# 	return redirect("lubotics:product", slug=slug)