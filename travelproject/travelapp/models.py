from django.db import models

# Create your models here.

class Place(models.Model):
    tit = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.tit

class Members(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='images2')
    address = models.TextField()

    def __str__(self):
        return self.name
