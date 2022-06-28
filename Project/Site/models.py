from django.db import models
from django.contrib.auth.models import User
 
'''class Chat(models.ModelForm):
	user_author = models.ForeignKey(User,on_delete=models.CASCADE)
	description = models.CharField(max_length=100)
	time = models.DateTimeField()
	def __str__(self):
		return self.user_author + '\n' + self.description
'''