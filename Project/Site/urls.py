from django.urls import path

from . import views as vw

urlpatterns = [
	path('',vw.home,name='home'),

	#path('sign-up',vw.signup,name="signup"),
	path('login/',vw.authf,name="authf"),
	path('logout/',vw.Logout,name="Logout"),
	

	
	path('questions/',vw.questions,name="questions"),
	path('create-post/',vw.create_post,name="create_post"),
	
	path('tutorials/',vw.tutorials,name="tutorials"),
	path('notes/',vw.notes,name="notes"),
	path('editor/',vw.editor,name="editor"),
]
