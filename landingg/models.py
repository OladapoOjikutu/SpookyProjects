from django.db import models
from embed_video.fields import EmbedVideoField
from colorfield.fields import ColorField

# Create your models here.
class site_visitor (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30, default= 'this is it')

    def __str__(self):
        return self.name


class Videos(models.Model):
    video=  EmbedVideoField()

class NameField(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    thisresult = models.CharField(blank=True,null=True,max_length=2000)
    thisresult1 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult2 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult3 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult4 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult5 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult6 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult7 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult8 = models.CharField(blank=True,null=True,max_length=2000)
    thisresult9 = models.CharField(blank=True,null=True,max_length=2000)


    def __str__(self):
        return self.name

class AlphaGuide(models.Model):
    letter_Position = models.CharField(max_length=30)
    attribute = models.TextField(max_length=1500)    

    def _str_(self):
        return self.letter_Position
        

class Alphatables(AlphaGuide):
    pass