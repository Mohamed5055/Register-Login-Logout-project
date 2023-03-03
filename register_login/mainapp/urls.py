from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # the main url
    path('register', views.register, name='register'), # register url
    path('login', views.login, name='login'), # login url
    path('logout', views.logout, name='logout') # logout url
]