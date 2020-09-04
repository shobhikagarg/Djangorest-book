# noinspection PyUnresolvedReferences
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now=False)
    published_by=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    author = models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book=models.ForeignKey(Book,related_name='boks',on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)
    up_votes=models.PositiveIntegerField()

    
    
