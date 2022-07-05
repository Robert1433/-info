from django.urls import path

from . import views as vw

urlpatterns = [

	path('login/',vw.authf,name="authf"),
	path('logout/',vw.Logout,name="Logout"),
	path('settings/',vw.settings,name="settings"),
	#----------------------------------------------------------------------------->
	path('create_lesson/',vw.create_lesson,name="create_lesson"),
	path('displaylessons/',vw.displaylessons,name="displaylessons"),
	 path("quiz/", vw.quiz, name="quiz"), 
    path('quiz/data/', vw.quiz_data_view, name='quiz-data'),
    path('quiz/save/', vw.save_quiz_view, name='quiz-save'),
	path('add_quiz/', vw.add_quiz, name='add_quiz'),    
    path('add_question/', vw.add_question, name='add_question'),  
    path('add_options/', vw.add_options, name='add_options'), 
    path('results/', vw.results, name='results'),    
    path('delete_question/', vw.delete_question, name='delete_question'),  
    path('delete_result/', vw.delete_result, name='delete_result'),    

	path('',vw.home,name='home'),
	#path('questions/',vw.questions,name="questions"),
	#path('mess/',vw.permess,name="permess"),
	path('tutorials/',vw.tutorials,name="tutorials"),
	path('editor/',vw.editor,name="editor"),
]
