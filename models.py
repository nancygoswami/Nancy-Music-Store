from django.db import models

# Create your models here

class Songs(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.track_name == models.CharField(max_length=200)

class User(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.user_name == models.CharField(max_length=200)

    
class Playlist(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.track_name == models.CharField(max_length=200)
