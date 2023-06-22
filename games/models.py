from django.db import models
from django.core.exceptions import ValidationError
import uuid
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
    slug = models.SlugField(blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            self.size = self.file.size / (1000*1000*1000)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Games"
