from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts,Image,Comment,Note,Feedback

class Register(UserCreationForm):
	email = forms.EmailField(label = "email",max_length= 100, required = True)
	first_name = forms.CharField(label = "first_name",max_length=100,required=True)
	last_name = forms.CharField(label="last_name",max_length=100,required=True)
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","password1","password2"]
		

class Post(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ['title','description']

class ImageForm():
	class Meta:
		model = Image
		fields = ['title']

class Comms():
	class Meta:
		model = Comment
		fields = ['description']

class Not():
	class Meta:
		model = Note
		fields = ['describ']				
		
class Feed():
	class Meta:
		model = Feedback
		fields = ['integer']