from django.db import models

# Create your models here.
class Leaveapp(models.Model):
    date        = models.CharField(max_length=100)
