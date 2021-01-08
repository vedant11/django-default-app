from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
	photo = models.ImageField(null =True, blank = True , upload_to="myimage")
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=300 , null =True, blank = True )
	body = models.CharField(max_length=1000 , null=True , blank=True)
	likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
	unlikes = models.ManyToManyField(User, blank=True, related_name='post_unlikes')
def get_like_url(self):
	return reverse("instagram:like")

def get_unlike_url(self):
	return reverse("instagram:unlike")

class editprofile(models.Model):
	name = models.CharField(max_length=300 , null =True, blank = True )