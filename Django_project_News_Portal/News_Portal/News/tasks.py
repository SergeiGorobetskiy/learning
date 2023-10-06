from celery import shared_task
import time
from News_Portal.News.models import news


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i + 1)

@shared_task
def complete_news(oid):
    new = news.objects.get(pk = oid)
    new.complete = True
    new.save()