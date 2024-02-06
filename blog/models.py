from django.db import models
import datetime
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=40)
    dt = datetime.datetime.now()  # Assume dt is 2023-11-24 15:30:00
    date = dt.date()  # date_only is now 2023-11-24
    description = models.TextField()

    def __str__(self):
        return self.title
