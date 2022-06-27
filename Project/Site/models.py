from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
	posts_author = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000)
	creation = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title + "\n" + self.description

class Comment(models.Model):
	posts_author = models.ForeignKey(User,on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)
	creation = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.description

class Feedback(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	integer = models.IntegerField()
	def __str__(self):
		return self.integer

class Image(models.Model):
	image_author = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='imgs/',blank=True)

	def __str__(self):
		return self.title + "\n"

class Note(models.Model):
	user_notes = models.ForeignKey(User,on_delete=models.CASCADE)
	describ = models.CharField(max_length=10000)

	def __str__(self):
		return self.describ + "\n"