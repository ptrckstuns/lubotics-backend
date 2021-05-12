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
	('Military', 'Military & Security'),
)
CATEGORY_SLUGS = {k.lower(): v for k, v in CATEGORY_CHOICES}

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	features = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2) 
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
		# max_length = self._meta.get_field('slug').max_length
		# slug_candidate = slug_original = slugify(self.title)[:max_length]
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
		
class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	products = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

class Wishlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.user.username
# class Profile(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	image = models.ImageField(upload_to=profile_path)

# 	first_name = models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)
	
# 	birth_date = models.DateField()
# 	date_joined = models.DateTimeField(default=timezone.now)
	
# 	address = models.CharField(max_length=250)
# 	contact_number = PhoneNumberField()
# 	# wishlist = models.ManyToManyField(Product, blank = True, related_name='Profile.wishlist')
# 	# cart = models.ManyToManyField(Product, blank = True, related_name='Profile.cart')
# 	# purchases = models.ManyToManyField(Product, blank = True, related_name='Profile.purchases')
	
# 	# AVATAR image
# 	# bday
# 	# date joined (yung kay coreyMS)
# 	# reference user
# 	def fullname(self):
# 		return f'{self.first_name} {self.last_name}'

# 	def __str__(self): 
# 		return self.user.username

# class Cart(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	items = models.ManyToManyField(Product, blank = True, related_name='Cart.items')
# 	quantity = model.Positi­veI­nte­ger­Field(default=0)

# class Orders(model.s.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	items = models.ManyToManyField(Product, blank = True, related_name='Orders.items')
# 	quantity = model.Positi­veI­nte­ger­Field()
	# random_id 
	# eta
