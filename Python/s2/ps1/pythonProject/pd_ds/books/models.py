from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    publish_data = models.DateTimeField()
    pages = models.IntegerField()
    hard_cover = models.BooleanField(default=True)
    author_id = models.ForeignKey('books.Author', null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# Create your models here.
