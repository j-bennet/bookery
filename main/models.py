from django.db import models

CATEGORIES = [
    ("Fiction", "Fiction"),
    ("Non-Fiction", "Non-Fiction"),
    ("Fantasy", "Fantasy"),
    ("Romance", "Romance"),
    ("Thriller", "Thriller"),
    ("Cookbook", "Cookbook"),
    ("Science", "Science"),
    ("Children", "Children"),
    ("Other", "Other"),
]

LANGUAGES = [
    ("en", "English"),
    ("fr", "French"),
    ("ru", "Russian"),
]


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    language = models.CharField(max_length=100, choices=LANGUAGES)
