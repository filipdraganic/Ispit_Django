from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Korisnik(models.Model):
    ime= models.CharField(max_length=64, default=None, blank=False)
    prezime= models.CharField(max_length=64, default=None, blank=False)
    email= models.EmailField(max_length=64, default=None, blank=False)
    adresa = models.CharField(max_length=64, default=None, blank=False)
    grad = models.CharField(max_length=64, default=None, blank=False)
    username = models.CharField(max_length=64, default=None, blank=False)
    password = models.CharField(max_length=255, default=None, blank=False)
