from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.



User = get_user_model()


class Post(models.Model):
	user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
	title = models.CharField(max_length=150, default=('New Post'))
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:all')

	class Meta():
		ordering = ['-created_at']
		unique_together = ('user','message')


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    def __str__(self):
        return self.text