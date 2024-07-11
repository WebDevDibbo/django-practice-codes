from django.db import models
from musician.models import Musician
rating = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]
# Create your models here.
class Album(models.Model):
    Album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    Release_date = models.DateField(auto_now_add=True)
    Ratings = models.CharField(max_length=50,choices=rating)

    def __str__(self):
        return self.Album_name