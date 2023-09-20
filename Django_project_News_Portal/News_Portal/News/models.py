from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import reverse
from django_filters import FilterSet, DateFilter, widgets
from django.core.validators import MinValueValidator


class Author(models.Model):
    objects = ()
    author_name = models.CharField(max_length=255)
    author_surname = models.CharField(max_length=255)
    article_topic = models.CharField(max_length=255)
    article_title = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    autor_rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post.set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.user.comment_set.aggregste(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get1('commentRating')

        self.author_rating = pRat *3 + cRat
        self.save()

    def title_censor(self):
        censor = '*'


    # photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)


sport = 'sprt'
politic ='pltc'
education = 'educ'
market = 'mrkt'
economics = 'ecms'
technology = 'tech'
wealth = 'wlth'
news = 'news'

CATEGORIES = [
    (sport, 'Sports'),
    (politic, 'Politics'),
    (education, 'Education'),
    (market, 'Markets'),
    (economics, 'Economics'),
    (technology, 'Technology'),
    (wealth, 'Wealth'),
    (news, 'Breaking news')
]
class Category(models.Model):
# the topics that they reflect(sports, politics, education, etc.).
    categories_of_articles = models.CharField(max_length=4, choices=CATEGORIES, default=news)
    unique = True
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    News = 'NW'
    Article = 'AR'
    Category_Choices = (
    (News, 'News post'),
    (Article, 'Article post')
    )
    dateCreations = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    article_title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating +=1
        self.save()

    def preview(self):
        return '{} ... {}' .format(self.title, str(self.text[0:255] + '...'))


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrougt = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating += 1
        self.save()


    comment_text = models.CharField(max_length=100)
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField()

class New(models.Model):
    objects = ()
    article_title = models.CharField(max_length=255)
    text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.article_title)

class PostCategoryChoicesFilter(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category_Choices', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class PostArticleTitleFilter(models.Model):
    name = models.CharField(max_length=255)
    title = models.ForeignKey('article_title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class PostDateCreationsFilter(models.Model):
    dateCreations = models.ForeignKey('dateCreations', on_delete=models.CASCADE)
    added_after = models.DateTimeField(
        field_name='added_at',
        lookup_expr='gt',
        widget=models.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        ),
    )
