from django.db import models

# Create your models here.
class RecordList(models.Model) :

    todo = models.CharField(max_length=200)