from django.db import models
from datetime import date
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(blank=True,null=True, max_length=50)
    last_name = models.CharField( blank=True,null=True,max_length=50)
    email= models.EmailField(blank=True,null=True, max_length=254)
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"Name : {self.first_name} instrument : {self.instrument_type}"
    
class Album(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    album_name = models.CharField( max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(default=date.today)
    rating = models.IntegerField(choices=RATING_CHOICES )
    def __str__(self) -> str:
        return f"Album name : {self.album_name}"
    
