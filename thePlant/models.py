from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Profit(models.Model):
    cost = models.FloatField()
    category = models.CharField(max_length=20)
    date = models.DateField(default='2023-09-20')


class Order(models.Model):
    date = models.DateField()
    income = models.FloatField()
    customer = models.CharField(max_length=20)
    invoice = models.BooleanField(default=False)






