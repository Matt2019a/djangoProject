from django.db import models


class Activity(models.Model):
    id = models.CharField(max_length=264, primary_key= True)
    title = models.CharField(max_length= 127)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Create your models here.
