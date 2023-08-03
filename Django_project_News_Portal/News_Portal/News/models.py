from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_surname = models.CharField(max_length=255)
    article_topic = models.CharField(max_length=255)
    article_title = models.CharField(max_length=255)


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
    author_name = models.CharField(max_length=255)
    author_surname = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    article_topic = models.CharField(max_length=255)
    article_title = models.CharField(max_length=255)
    text_of_articles = models.CharField(max_length=255)
    categories_of_articles = models.CharField(max_length=4, choices=CATEGORIES)
    rating = models.IntegerField()
class PostCategory(models.Model):
    pass


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField()


