from django.db import models
from django.db.models.fields import CharField

class blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/') #Inside the media folder created, anytime you upload an image it goes to the images folder
