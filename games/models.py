from django.db import models

# Create your models here.


class Games (models.Model):
    name = models.CharField(max_length=200, blank=False)
    describtions = models.TextField()
    type = models.CharField(max_length=200, blank=False)
    file = models.FileField(upload_to="gamesFile/games")
    thumbnails = models.ImageField(upload_to="gamesFile/images")
    sample_video = models.FileField(upload_to="gamesFile/sample_video")
    size = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
