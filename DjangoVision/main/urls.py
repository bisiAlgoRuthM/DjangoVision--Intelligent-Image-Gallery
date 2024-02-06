from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('category/', views.category, name='category'),
    path('postsign/', views.postsign, name='postsign'),
    path('welcome/', views.welcome, name='welcome')
]

