from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class TipUtilizator(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email = models.EmailField(max_length=255)
    preference = models.CharField(max_length=255,null=True)
    biograpghy = models.TextField(blank=True,null=True)
    tiputilizator = models.CharField(max_length= 255,null = True)
    def __str__(self):
        return self.user.username



class PostTeacher(models.Model):
    teacher_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    update = models.FileField(upload_to = "files")
    imag = models.ImageField(upload_to = "media")
    date = models.DateTimeField(auto_now_add = True)     