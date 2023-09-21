from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.core.paginator import Paginator
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import *

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

class AuthorList(generic.ListView):
    model = Author
    context_object_name = 'Authors'
    queryset1 = Author.objects.all()
    # queryset2 = Author.objects.filter(Author.title_censor())
    template_name = 'Author/author_list.html'

class PostDetail(generic.DetailView):
    model = Post

class PostChoices(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'search.html'
    ordering = ['-dateCreations']
    paginate_by = 10

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

# class AutorCreate(LoginRequiredMixin, generic.CreateView):
#     raise_exception = True
#     form_class = AuthorForm
#     model = Author
#     template_name = 'author_edit.html'