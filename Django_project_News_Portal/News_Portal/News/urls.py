from django.urls import path
from .views import *

urlpatterns = [
    path('author_list', AuthorList.as_view()),
    path('news_list/', index, name='index'),
    path('New/<str:slug>', detail, name='detail'),
    path('search/<str:slug>', detail, name='detail'),
    path('post/<int:pk>/', PostChoices.as_view()),
    path('post/<int:pk>/', PostDetail.as_view())
]