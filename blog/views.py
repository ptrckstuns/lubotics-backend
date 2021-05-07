from django.shortcuts import render
# from django.core.exeptions import ObjectDoesNotExist
from .models import Post, Product, OrderProduct, Order
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

class CartDetail(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
		except Exception:
			messages.error(request, "You do not have an order")
			return redirect("/")
		else:
			context = {
				'object': order
			}
			return render(self.request, 'blog/cart.html', context)

class ProductDetailView(DetailView):
	model = Product
	template_name = 'blog/product.html'


@login_required
def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order_product, created = OrderProduct.objects.get_or_create(product=product)
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
	return redirect("lubotics:product", slug=slug)