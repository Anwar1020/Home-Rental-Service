from operator import index
from turtle import home
from django.urls import path
from .views import landing, signup, signin, homepage, logout, createpost, search

urlpatterns  = [
    path('', landing, name ='landingpage'),
    path('signup/', signup, name='signuppage'),
    path('signin/', signin, name='signinpage'),
    path('home/', homepage, name='homepage' ),
    path('logout/', logout, name='logoutpage'),
    path('createpost/', createpost, name='createpost'),
    path('search/', search, name='search'),


]