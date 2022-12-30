from django.db import models

# Create your models here.
class Mongo(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    app_name = models.CharField(max_length=120)

    def __str__(self):
        return self.title