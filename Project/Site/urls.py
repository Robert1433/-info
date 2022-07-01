from django.urls import path

from . import views as vw

urlpatterns = [

	path('login/',vw.authf,name="authf"),
	path('logout/',vw.Logout,name="Logout"),
	path('settings/',vw.settings,name="settings"),
	#----------------------------------------------------------------------------->

	path('',vw.home,name='home'),
	#path('questions/',vw.questions,name="questions"),
	#path('mess/',vw.permess,name="permess"),
	path('tutorials/',vw.tutorials,name="tutorials"),
	path('notes/',vw.notes,name="notes"),
	path('editor/',vw.editor,name="editor"),
]
