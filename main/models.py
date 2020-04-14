from django.db import models

# Create your models here.
class Book(models.Model):
    objects = models.Manager()

    cover = models.ImageField()
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 20)
    publisher = models.CharField(max_length = 20)
    letters = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class EachLetter(models.Model):
    objects = models.Manager()

    whichBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    content = models.TextField()

    def __str__(self):
        return self.title

