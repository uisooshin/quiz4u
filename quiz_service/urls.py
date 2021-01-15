from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                    #root page -> index page
    #path('index.html', views.index, name='index'),          #index page
    path(r'index/', views.index, name='index'),          #index page
    path(r'solv_quiz/', views.solv_quiz, name='solv_quiz'), #quiz page
    path(r'signup/', views.signup, name='signup'),    #signup page
    path(r'signin/', views.signin, name='signin'),    #signup page

]
