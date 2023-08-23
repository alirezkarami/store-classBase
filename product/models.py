from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CharField)
    price = models.IntegerField()
    description = models.TextField()
