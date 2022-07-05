from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime
User = get_user_model()

class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id_user = models.IntegerField(null=True)
    email = models.EmailField(max_length=255)
    preference = models.CharField(max_length=255,null=True)
    biograpghy = models.TextField(blank=True,null=True)
    tiputilizator = models.CharField(max_length= 255,null = True)
    def __str__(self):
        return self.user.username


class PostLessonTeacher(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    teacher_user = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    update = models.FileField(upload_to = "files")
    imag = models.ImageField(upload_to = "images")     
    creation_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    
class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"
    
class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.quiz)
