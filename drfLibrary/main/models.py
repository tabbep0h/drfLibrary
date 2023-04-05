from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(default=1990)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=255)
    allprice = models.IntegerField()
    Books = models.ForeignKey(Book, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

