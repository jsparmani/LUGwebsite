from django.db import models

# Create your models here.

class Receiver(models.Model):
	email = models.EmailField(unique = True)

	def __str__(self):
		return self.email