from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Event(models.Model):
	user = models.ForeignKey(User,related_name='events',on_delete=models.CASCADE)

	organization_name = models.CharField(max_length = 150, blank=False)
	organization_logo = models.ImageField(upload_to='logo',blank=False)

	title = models.CharField(max_length = 150, default='New Event', blank=False)
	description = models.TextField(blank=False)

	start_date = models.DateField(blank=False)
	end_date = models.DateField(blank=True)
	start_time = models.TimeField(blank=False)
	end_time = models.TimeField(blank=True)

	venue = models.TextField(blank=False)

	link = models.URLField(blank=False)
	price = models.PositiveIntegerField(blank=True, default=0)

	event_image_1 = models.ImageField(upload_to='event_images',blank=False)
	event_image_2 = models.ImageField(upload_to='event_images',blank=True)
	event_image_3 = models.ImageField(upload_to='event_images',blank=True)
	event_image_4 = models.ImageField(upload_to='event_images',blank=True)

	contact_no = models.BigIntegerField(blank=False)
	contact_email = models.EmailField(blank=False)
	
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home')

	class Meta():
		ordering = ['start_date']
