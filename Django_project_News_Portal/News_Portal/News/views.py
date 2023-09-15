from django.shortcuts import render
from .models import New
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *

def index(request):
    news = [New.objects.all(),
        'news_list',
         'Sport',
         'Politic',
         'Education',
         'Market',
         'Economics',
         'Technology'
         ]
    return render(request, 'index.html', context={'name': news})

def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'New':New})

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    queryset1 = Author.objects.all()
    # queryset2 = Author.objects.filter(Author.title_censor())
    template_name = 'Author/author_list.html'

class Post(DetailView):
    model = Post