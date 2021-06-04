from django.db import models
from django.db.models.fields import CharField

class job(models.Model):
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to = 'images/') #Inside the media folder created, anytime you upload an image it goes to the images folder
    summary = CharField(max_length=200, default='') #To put cap to the summary boxes

    def __str__(self):
        return self.title