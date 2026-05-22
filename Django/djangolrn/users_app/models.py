from os import name

from django.db import models

# Create your models here.

# the model data: each tpe of dta will have a tabkl ein DB
# tye clasases/model we create iinpython here then get migrated and move to DB -> models becomes ttables

class Users(models.Model):          # django docs +> model field refrence
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    email = models.EmailField(max_length=75)     # serach: django filed model refrence for email
