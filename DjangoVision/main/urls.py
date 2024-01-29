from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signIn/', views.signIn, name='signIn'),
    path('test/', views.test, name='test'),
    path('upload/', views.upload, name='upload'),
    path('postsign/', views.postsign, name='postsign')
]

