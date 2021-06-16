from django.db import models
from django.db.models.fields import CharField

class blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/') #Inside the media folder created, anytime you upload an image it goes to the images folder
    link = models.URLField(max_length=1500, blank=True, null="True", default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y, %I:%M %p')
        
    