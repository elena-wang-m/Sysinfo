from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('disk/', views.disk,  name='disk'),
    path('users/', views.users, name = 'users'),
]
