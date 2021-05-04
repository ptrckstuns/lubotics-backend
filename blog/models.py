from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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


class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	features = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2) 
	category = models.CharField(max_length=100)

	# image = models.ImageField(upload_to='images')
	image = models.ImageField(upload_to=product_path)

	def __str__(self): 
		return self.name


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
