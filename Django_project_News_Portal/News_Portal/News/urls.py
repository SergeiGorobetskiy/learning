from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist', AuthorList.as_view()),
    path('news_list/', index, name='index'),
    path('New/<str:slug>', detail, name='detail'),
    path('post/<int:pk>/', Post.as_view())
]