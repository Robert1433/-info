from re import T
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import Profile,PostLessonTeacher
from .forms import  Register
from django.contrib.auth.models import User
from itertools import chain
from django.contrib.auth.decorators import login_required
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def home(request):
	posts = Profile.objects.all()
	return render(request,"home.html",{'posts':posts})

def authf(request):

		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password1',None)
		tiputilizator = request.POST.get('tiputilizator',None)
		user = authenticate(request, username = username, password = password, email = email,tiputilizator = tiputilizator)
		if user is not None:
			login(request,user)
			return redirect('settings')	
		else:
				form = Register(request.POST)
				if form.is_valid():
					user = form.save()			
					login(request,user)
					usermodel = User.objects.get(username=username)
					newprofile = Profile.objects.create(user= usermodel,user_id = usermodel.id)
					newprofile.save()
					return redirect('settings')
				else:
					form = Register()
					return render(request,'register/login.html',{"form":form})					
	

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="/login/")
def settings(request):
	UserProfile = Profile.objects.get(user=request.user)
	if request.method == 'POST':	
		email = request.POST['email']
		preferences = request.POST['preferences']
		bio = request.POST['bio']
		tip = request.POST['tip']
		UserProfile.email = email
		UserProfile.preference = preferences
		UserProfile.biograpghy = bio
		UserProfile.tiputilizator = tip
		UserProfile.save()
		return redirect('home')
	return render(request,'register/settings.html',{'user_profile':UserProfile})

#doesn`t work import files

def create_lesson(request):
	UserObject = User.objects.get(username=request.user.username)
	UserProfile = Profile.objects.get(user = UserObject)
	if request.method == 'POST':
		user = request.user.username
		imag = request.FILES.get('imag')
		text = request.POST['text']
		fila = request.FILES.get('fila')
		print(fila)
		newpost = PostLessonTeacher.objects.create(teacher_user=user,imag = imag,text = text,update = fila)
		newpost.save()
		return redirect('home')
	return render(request,'utilites/lessons.html',{'UserProfile':UserProfile})

def files(request):
	return render(request,'media/files/sdac.pdf',{})
def displaylessons(request):
	posts2 = PostLessonTeacher.objects.all()
	return render(request,'utilites/displaylessons.html',{'posts2':posts2})


def create_quiz(request):

	return render(request,'utilites/uploadlesson.html',{})

def displayquiz(request):
	pass



def searchteacher(request):
	user_object = User.objects.get(username=request.user.username)
	user_profile = Profile.objects.get(user=user_object)
	if request.method == 'POST':
		username=request.POST['username'] 
		username_object = User.objects.filter(username__icontains=username)
		usernameprof = [] 
		usernameprofilelist = []
		for users in username_object:
			usernameprof.append(users.id)
		for ide in usernameprof:
			profile_lists = Profile.objects.filter(id_user=ide) 
			usernameprofilelist.append(profile_lists)
		usernameprofilelist = list(chain(*usernameprofilelist))
	return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': usernameprofilelist})






#----------------------------------------------------------------------------->





# editor (html + css + js)
@login_required(login_url="/login/")
def editor(request):
	return render(request,"utilites/compiler.html")

#----------------------------------------------------------------------------->
#Tutorials
@login_required(login_url="/login/")
def tutorials(request):
	return render(request,"utilites/tutorials.html")




