from re import T
from django.forms import inlineformset_factory
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import *
from .forms import  Register,QuestionsQuiz
from django.contrib.auth.models import User
from itertools import chain
from django.contrib.auth.decorators import login_required
import io
from django.http import FileResponse, JsonResponse
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


def displaylessons(request):
	posts2 = PostLessonTeacher.objects.all()
	return render(request,'utilites/displaylessons.html',{'posts2':posts2})


def quiz(request):
    quiz = Quiz.objects.all()
    para = {'quiz' : quiz}
    return render(request, "quizez/quiz.html", para)

def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "quizez/quiz.html", {'quiz':quiz})

def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, myid):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(content=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.correct:
                            score += 1
                            correct_answer = a.content
                    else:
                        if a.correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})
     
        Marks_Of_User.objects.create(quiz=quiz, user=user, score=score)
        
        return JsonResponse({'passed': True, 'score': score, 'marks': marks})
    




def add_quiz(request):
    if request.method=="POST":
        form = QuestionsQuiz(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            obj = form.instance
            return render(request, "quizez/add_quiz.html", {'obj':obj})
    else:
        form=QuestionsQuiz
    return render(request, "quizez/add_quiz.html", {'form':form})

def add_question(request):
    questions = Question.objects.all()
    questions = Question.objects.filter().order_by('-id')
    if request.method=="POST":
        form = QuestionsQuiz(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "quizez/add_question.html")
    else:
        form=QuestionsQuiz
    return render(request, "quizez/add_question.html", {'form':form, 'questions':questions})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "quizez/delete_question.html", {'question':question})


def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "add_options.html", {'alert':alert})
    else:
        formset=QuestionFormSet(instance=question)
    return render(request, "quizez/add_options.html", {'formset':formset, 'question':question})

def results(request):
    marks = Marks_Of_User.objects.all()
    return render(request, "quizez/results.html", {'marks':marks})

def delete_result(request, myid):
    marks = Marks_Of_User.objects.get(id=myid)
    if request.method == "POST":
        marks.delete()
        return redirect('/results')
    return render(request, "quizez/delete_result.html", {'marks':marks})


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


def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = PostLessonTeacher.objects.filter(user=pk)
    user_post_length = len(user_posts)
    user = pk
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
    }
    return render(request, 'profile.html', context)




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




