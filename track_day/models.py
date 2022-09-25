from django.db import models

# Create your models here.

class TaskDay(models.Model):

    name = models.CharField(max_length=15)
    opis = models.TextField(blank = True)

    def __str__(self) -> str:
        return self.name
