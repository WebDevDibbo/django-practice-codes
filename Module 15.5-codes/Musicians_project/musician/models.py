from django.db import models
MUSIC_INSTRUMENTS = [
    ('piano','Piano'),
    ('guitar','Guitar'),
    ('drum set','Drum set'),
    ('wind','Wind'),
]
# Create your models here.
class Musician(models.Model):
    First_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=11)
    Instrument_type = models.CharField(max_length=100,choices=MUSIC_INSTRUMENTS)

    def __str__(self) -> str:
        return self.First_name
