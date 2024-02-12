from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
    
]