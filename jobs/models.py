from django.db import models
from django.db.models.fields import CharField

class job(models.Model):
    image = models.ImageField(upload_to = 'images/') #Inside the media folder created, anytime you upload an image it goes to the images folder
    summary = CharField(max_length=200, default='SOME STRING') #To put cap to the summary boxes

