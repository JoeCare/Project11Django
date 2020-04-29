from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    value = models.IntegerField()
    image = models.CharField(max_length=1000, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
