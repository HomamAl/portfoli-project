from django.db import models
from django.db.models.fields import CharField

class job(models.Model):
    header = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to = 'images/') #Inside the media folder created, anytime you upload an image it goes to the images folder
    summary = CharField(max_length=1500, default='') #To put cap to the summary boxes
    link = models.URLField(max_length=1500, default='')

    def __str__(self):
        return self.header