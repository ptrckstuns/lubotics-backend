from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse
from django.utils.text import slugify

import itertools

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) #date registered
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# isFeatured = models.BooleanField(default=False)
	def __str__(self): 
		return self.title


def product_path(instance, filename):
    return f'products/{instance.category}/{instance.name}/{filename}'

def profile_path(instance, filename):
    return f'profile/{instance.user.username}/{filename}'


CATEGORY_CHOICES = (
	('Humanoids', 'Humanoids'),
	('Consumer', 'Consumer'),
	('Drones', 'Drones'),
	('Education', 'Education'),
	('Military', 'Military'),
)
CATEGORY_SLUGS = {k.lower(): v for k, v in CATEGORY_CHOICES}

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	features = models.TextField()
	price = models.DecimalField(max_digits=12, decimal_places=2) 
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=25)
	category_slug = models.CharField(default='', editable= False, max_length=25)
	image = models.ImageField(upload_to=product_path)
	slug = models.SlugField(
		default='',
		editable=False,
		# max_length=settings.BLOG_TITLE_MAX_LENGTH,
	)
	# image = models.ImageField(upload_to='images')

	def __str__(self): 
		return self.name

	def _get_category_slug(self):
		slugs = CATEGORY_SLUGS
		for slug in slugs:
			if slugs[slug] == self.category:
				return slug

	def _generate_slug(self):
		slug_candidate = slug_original = slugify(self.name)
		for i in itertools.count(1):
			if not Product.objects.filter(slug=slug_candidate).exists():
				break
			slug_candidate = '{}-{}'.format(slug_original, i)
		return slug_candidate

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = self._generate_slug()
			self.category_slug = self._get_category_slug()
		super(Product, self).save(*args, **kwargs)


	
	def get_category_url(self):
		return reverse("lubotics:products-category", kwargs={
			'category': self.category
		})

	def get_absolute_url(self):
		return reverse("lubotics:product", kwargs={
			'slug': self.slug
		})

	def get_add_to_cart_url(self):
		return reverse("lubotics:add-to-cart", kwargs={
			'slug': self.slug
		})

	def get_buy_now_url(self):
		return reverse("lubotics:buy-now", kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse("lubotics:remove-from-cart", kwargs={
			'slug': self.slug
		})
	def get_add_to_wishlist_url(self):
		return reverse("lubotics:add-to-wishlist", kwargs={
			'slug': self.slug
		})
	def get_remove_from_wishlist_url(self):
		return reverse("lubotics:remove-from-wishlist", kwargs={
			'slug': self.slug
		})


class OrderProduct(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default = 1)

	def __str__(self):
		return f"({self.product.pk}) - {self.product.name} {self.quantity}x"
	def get_order_price(self): 
		return self.quantity * self.product.price
		
class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	products = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
	#total ng mga selected / checked 
	def get_subtotal_price(self):
		total = 0
		for product in self.products.all():
			total += product.get_order_price()
		return total

	def get_total_quantity(self):
		n = 0
		for product in self.products.all():
			n += product.quantity
		return n

	def get_shipping_fee(self):
		# unique = len(self.products.all()) # no. of unique items
		totaln = self.get_total_quantity() # unique * quantity #decimal
		base = 10000
		
		if totaln == 0:
			return 0
		else:
			return base + (base / totaln)
		# 10000 + (10000 / 2) # 15000
		# 10000 + (10000 / 1) = 1000 # 20k

	def get_total_price(self):
		return float(self.get_subtotal_price()) + float(self.get_shipping_fee())


class Wishlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.user.username
