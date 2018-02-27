from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    word_count = models.PositiveIntegerField()
    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
