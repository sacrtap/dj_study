from django.db import models

# Create your models here.
class DBINFO(models.Model):
    albumName = models.CharField(max_length=45)
    credits = models.CharField(max_length=45)
    source = models.CharField(max_length=45)
    posterPicUrl = models.CharField(max_length=255)
    html5PlayUrl = models.CharField(max_length=255)
    votenum = models.IntegerField(default=0)
    sharenum = models.IntegerField(default=0)
    videonum = models.IntegerField(default=0)
    videonumold = models.IntegerField(default=0)
    videodate = models.DateTimeField()