from pd_ds.celery import app
from django.utils import timezone
from books.models import Book, Author, Event
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def calculation():
    Event.objects.all().update(active=False)
    #Event.objects.exclude(start_date__lte=timezone.now(), end_date__gte=timezone.now()).update(active=False)
    Event.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now()).update(active=True)
    logger.info('jestem')
    # for e in Event.objects.all():
    #     # if e.start_date <= timezone.now() <= e.end_date:
    #     #     e.active = True
    #     # else:
    #     #     e.active = False
    #     e.active = e.start_date <= timezone.now() <= e.end_date
    #     e.save()
    #     print("equations finished")