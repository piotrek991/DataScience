from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE, null=True, blank=False)
    num_pages = models.IntegerField()
    published_date = models.DateField()
    hard_cover = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " " + str(self.published_date)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    authors = models.ManyToManyField('books.Author')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Create your models here.
