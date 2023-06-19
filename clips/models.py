from django.db import models
from accounts.models import Accounts
# Create your models here.


class Clips (models.Model):
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to="clips/videos")
    date_uploaded = models.DateField(auto_now_add=True)
    User = models.ForeignKey(Accounts, models.CASCADE)
    thumbnial = models.ImageField(upload_to="clips/images")

    def __str__(self):
        return self.name
