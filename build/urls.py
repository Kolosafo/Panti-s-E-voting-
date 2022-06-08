from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name ='index'),
	path('register/', views.register, name ='register'),
	path('about/', views.about, name ='about'),
	path('<int:question_id>/confirmation/', views.confirmation, name ='confirmation'),
    path('logout/', views.logout_user, name='logout'),
	path('login/', views.login_page, name ='login'),
	path('<int:question_id>/', views.detail, name ='detail'),
	path('<int:question_id>/results/', views.results, name ='results'),
	path('<int:question_id>/vote/', views.vote, name ='vote'),
]
