from django.db import models
from django.db.models.fields import CharField

class job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = CharField(max_length=200)
