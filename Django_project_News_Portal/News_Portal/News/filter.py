from django_filters import FilterSet
from .models import *


class PostFilter(FilterSet):
    class Meta:
        model = Post
        filter = {
            'name' : ['icontains'],
            'author' : ['contains'],
            'News' : ['contains'],
            'Article' : ['contains'],
            'Category_Choices' : ['contains'],
            'dateCreations' : ['gt'],
            'postCategory' : ['contains'],
            'article_title' : ['contains'],
            'rating' : ['gt'],
        }