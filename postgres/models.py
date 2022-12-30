from django.db import models
from mongo.models import *

# Create your models here.


class Postgres(models.Model):
    name = models.CharField(max_length=120)
    numbers = models.IntegerField()


