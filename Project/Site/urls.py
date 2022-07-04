from django.urls import path

from . import views as vw

urlpatterns = [

	path('login/',vw.authf,name="authf"),
	path('logout/',vw.Logout,name="Logout"),
	path('settings/',vw.settings,name="settings"),
	#----------------------------------------------------------------------------->
	path('create_lesson/',vw.create_lesson,name="create_lesson"),
	path('displaylessons/',vw.displaylessons,name="displaylessons"),
	path('files',vw.files,name="files"),
	path('create_quiz/',vw.create_quiz,name="create_quiz"),
	path('',vw.home,name='home'),
	#path('questions/',vw.questions,name="questions"),
	#path('mess/',vw.permess,name="permess"),
	path('tutorials/',vw.tutorials,name="tutorials"),
	path('editor/',vw.editor,name="editor"),
]
