from django_filters import FilterSet
from .models import *


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'dateCreations' : ['gt'],
            'postCategory' : ['icontains'],
            'article_title' : ['icontains'],
            'rating' : ['gt'],
        }