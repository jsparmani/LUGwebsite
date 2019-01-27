from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Maker(models.Model):
	user = models.ForeignKey(User,related_name='makers',on_delete=models.CASCADE)
	role_in_website = models.CharField(max_length = 100)
	present_designation = models.CharField(max_length = 100)
	resume_link = models.URLField()

	def __str__(self):
		return (self.user.first_name + " " + self.user.last_name)



