from django.db import models
from django.contrib.auth.models import User
from blog.models import Product
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	birth_date =models.DateField(auto_now=False, null=True, blank=True)
	# date_joined = models.DateTimeField(default=timezone.now)
	
	address = models.CharField(max_length=250, blank=True)
	contact_number = PhoneNumberField(blank=True)


	def fullname(self):
		return f'{self.first_name} {self.last_name}'

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)