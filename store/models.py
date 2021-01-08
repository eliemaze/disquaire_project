  
from django.db import models


class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "artiste"
        verbose_name_plural = "artistes"


class Contact(models.Model):
    email = models.EmailField('e-mail', max_length=100)
    name = models.CharField('Nom', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "contacte"
        verbose_name_plural = "contactes"


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.TextField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albums"

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name
    
    class Meta:
        verbose_name = "réservation"
        verbose_name_plural = "réservations"