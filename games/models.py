from django.db import models
from django.core.exceptions import ValidationError
import uuid
from accounts.models import Accounts
from django.urls import reverse
# Create your models here.


choices = (
    ('FPS', 'First-Person Shooters (FPS)'),
    ('TPS', 'Third-Person Shooters'),
    ('Action-Adventure', 'Action-Adventure'),
    ('Hack-Slash', 'Hack and Slash'),
    ('Platformers', 'Platformers'),
    ('Beat-em-up', 'Beat em Up'),
    ('Open-World', 'Open-World Action'),
    ('Battle-Royale', 'Battle Royale'),
    ('RPG', 'Role-Playing Games (RPG)'),
    ('Racing', 'Racing Games'),
    ('Sports', 'Sports Games'),
    ('Strategy', 'Strategy Games'),
    ('Puzzle', 'Puzzle Games'),
    ('Simulation', 'Simulation Games'),
    ('Stealth', 'Stealth Games'),
    ('Fighting', 'Fighting Games'),
)


video_formats = [
    "MP4",
    "AVI",
    "MKV",
    "MOV",
    "WMV",
    "FLV",
    "WebM",
    "MPEG",
    "3GP",
    "VOB",
    "MPG",
    "ASF",
    "M4V",
    "OGV",
    "TS"
]


def validate_sample_video(value):
    ext = value.name.split('.')[-1].upper()
    if not ext.upper() in video_formats:
        raise ValidationError(' Only support Video Files')
    


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Games (models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200, blank=False)
    describtions = models.TextField()
    type = models.CharField(choices=choices, max_length=100)
    file = models.FileField(upload_to="gamesFile/games", blank=False)
    thumbnails = models.ImageField(upload_to="gamesFile/images", blank=False)
    sample_video = models.FileField(
        upload_to="gamesFile/sample_video", validators=[validate_sample_video], blank=False)
    size = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    version = models.IntegerField(blank= False)
    slug = models.SlugField(blank=False)
    genre = models.ForeignKey(Genre, models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            self.size = self.file.size / (1000*1000*1000)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("game_details", kwargs={"pk": self.uuid})
    

    class Meta:
        verbose_name_plural = "Games"




class Downloaded (models.Model):
    user = models.ForeignKey(Accounts, models.CASCADE)
    game = models.ForeignKey(Games, models.CASCADE)
    Download_date = models.DateTimeField(auto_created=True)



    def downloadCount ():
        return self.game.count()


    def __str__ (self):
        return f"{self.game.name} - {self.user.first_name}"
    

