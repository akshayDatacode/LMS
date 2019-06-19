from django.urls import path
from .import views
from .import login
urlpatterns=[

path('index',views.index,name='index'),
path('stdlogin',login.stdlogin,name='stdlogin'),
path('article_list',views.article,name='article_list'),
]
