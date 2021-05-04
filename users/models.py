from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	# image = models.ImageField(upload_to=profile_path)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	# birth_date = models.DateField()
	date_joined = models.DateTimeField(default=timezone.now)
	
	address = models.CharField(max_length=250)
	# contact_number = PhoneNumberField()
	
	# wishlist = models.ManyToManyField(Product, blank = True, related_name='Profile.wishlist')
	# cart = models.ManyToManyField(Product, blank = True, related_name='Profile.cart')
	# purchases = models.ManyToManyField(Product, blank = True, related_name='Profile.purchases')
	
	# AVATAR image
	# bday
	# date joined (yung kay coreyMS)
	# reference user

	def fullname(self):
		return f'{self.first_name} {self.last_name}'

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)