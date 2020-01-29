from django.contrib.auth.models import User
from django.db import models

from oglas.models import Licitacija
from oglas.models import Oglas
# Create your models here.

class Korisnik(models.Model):
    ime = models.CharField(max_length=64, default=None, blank=False)
    prezime = models.CharField(max_length=64, default=None, blank=False)
    email = models.EmailField(max_length=64, default=None, blank=False)
    adresa = models.CharField(max_length=64, default=None, blank=False)
    grad = models.CharField(max_length=64, default=None, blank=False)
    username = models.CharField(max_length=64, default=None, blank=False)
    password = models.CharField(max_length=255, default=None, blank=False)


    def getBrojOglasa(self):
        return len(self.oglas_set.all())

    def getBrojLicitacija(self):
        return len(self.licitacija_set.all())

    def getZeljenoPolje(self, string):
        if string == "brojLicitacijaKorisnik":
            return self.getBrojLicitacija()
        if string == "brojOglasaKorisnik":
            return self.getBrojOglasa()