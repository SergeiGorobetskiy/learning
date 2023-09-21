from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('author_list', AuthorList.as_view()),
    path('news_list/', index, name='index'),
    path('New/<str:slug>', detail, name='detail'),
    path('search/<str:slug>', detail, name='detail'),
    path('post/', PostChoices.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]