from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
	description = models.CharField(max_length=255, blank=True)
	files = models.FileField(upload_to='posts')
	date_posted = models.DateTimeField(default=timezone.now)
	usernames = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)
	likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)
	like_count = models.BigIntegerField(default='0')

	def __str__(self):
		return self.description


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
 

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)