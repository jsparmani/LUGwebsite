from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()

	def __str__(self):
		return self.message

	def get_absolute_url(self):
		return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

	class Meta():
		ordering = ['-created_at']
		unique_together = ('user','message')


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    def __str__(self):
        return self.text