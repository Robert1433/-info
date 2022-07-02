from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import TipUtilizator
from .forms import  Register
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
	posts = TipUtilizator.objects.all()
	return render(request,"home.html",{'posts':posts})

#----------------------------------------------------------------------------->

#django authentication
def authf(request):

		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password1',None)
		password1 = request.POST.get('password2',None)
		tiputilizator = request.POST.get('tiputilizator',None)
		user = authenticate(request, username = username, password = password, email = email)
		if user is not None:
			login(request,user)
			messages.add_message(request,messages.SUCCESS, "Your account was logged in with succses. Good luck and have fun!")
			return redirect('home')	
		else:
				form = Register(request.POST)
				if form.is_valid():
					user = form.save(commit= False)
					tip = user
					tip.user = request.user
					tip.save()					
					login(request,tip)
					messages.success(request, "Your account was created with succses. Good luck and have fun!")

					return redirect('home')
				else:
					form = Register()
					return render(request,'register/login.html',{"form":form})					
	

def Logout(request):
    logout(request)
    return redirect('home')

#----------------------------------------------------------------------------->

# editor (html + css + js)
@login_required(login_url="/login/")
def editor(request):
	return render(request,"utilites/compiler.html")

#----------------------------------------------------------------------------->
'''
#django chat room 
@login_required(login_url="/login/")
def questions(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'utilites/questions.html', {"posts": posts})


def permess(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			com = form.save(commit = False)
			com.author = request.user
			com.save()
			return redirect("questions")
	else:
		form = PostForm()
	return render(request, "utilites/create_post.html",{"form":form})	 

'''


@login_required(login_url="/login/")
def notes(request):
	return render(request,"utilites/notes.html")
#Tutorials
@login_required(login_url="/login/")
def tutorials(request):
	return render(request,"utilites/tutorials.html")




