from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from requests import request
from .forms import  Register,Post
from .models import Posts
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(reqeust):
	return render(reqeust,"home.html")

#django authentication

def authf(request):

		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password1',None)
		password1 = request.POST.get('password2',None)
		user = authenticate(request, username = username, password = password, email = email)
		if user is not None:
			login(request,user)
			messages.add_message(request,messages.SUCCESS, "Your account was logged in with succses. Good luck and have fun!")
			return redirect('home')	
		else:
				form = Register(request.POST)
				if form.is_valid():
					user = form.save()
					login(request,user)
					messages.success(request, "Your account was created with succses. Good luck and have fun!")
					return redirect('home')
				else:
					form = Register()
					return render(request,'register/login.html',{"form":form})					

def Logout(request):
    logout(request)
    return redirect('home')



#Questions and answers
@login_required(login_url="/login/")
def questions(request):
	posts = Posts.objects.all()
	if request.method == 'POST':
		postid = request.POST.get('postid')

		post = Posts.objects.filter(id=postid).first()
		if post and post.author == request.user:
			post.delete()

	return render(request,"utilites/questions.html",{"posts":posts})

def create_post(request):
	if request.method == "POST":
		form = Post(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect("questions")
	else:
		form = Post()
	return render(request, "utilites/create_post.html",{"form":form})


#Notes
@login_required(login_url="/login/")
def notes(request):
	return render(request,"utilites/notes.html")
#Tutorials
@login_required(login_url="/login/")
def tutorials(request):
	return render(request,"utilites/tutorials.html")
#Editor
@login_required(login_url="/login/")
def editor(request):
	return render(request,"utilites/compiler.html")


