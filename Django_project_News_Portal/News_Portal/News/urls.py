from .views import *
from django.contrib import admin
from django.urls import path, include
from .views import IndexView, NewPostView, take_post


urlpatterns = [
    path('author_list', AuthorList.as_view()),
    path('news_list/', index, name='index'),
    path('New/<str:slug>', detail, name='detail'),
    path('search/<str:slug>', detail, name='detail'),
    path('post/', PostChoices.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    #path('admin/', admin.site.urls),
    path('accounts/',
         #include('django.contrib.auth.urls')),
         include('allauth.urls')),
    path('accounts/', include('Accounts.urls')),
    path('subscriptions/', Subscription, name='subscriptions'),
    path('', IndexView.as_view()),
    path('new', NewPostView.as_view(), name = 'take_post'),
    path('take/<int:oid>', take_post, name = 'take_post'),
]