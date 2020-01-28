from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Oglas(models.Model):
    cena = models.IntegerField(default=1, blank=False)
    ime = models.CharField(max_length=64, default=None, blank=False)
    brojPregleda = models.IntegerField(default=0, blank=False)
    prodavac = models.ForeignKey(User, on_delete=models.CASCADE, null=True,default=None, blank=False)
    kategorija = models.CharField(max_length=64,default="opste", null=True, blank=False)
    datumPostavljanja = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    preostaloVreme = models.IntegerField(null=True, blank=False, default=60000)
    opis = models.CharField(null=True, blank=False, default="Klasican opis", max_length=254)


    def getCena(self):
        return self.cena

    def getBrojPregleda(self):
        return self.brojPregleda

    def getDatumPostavljanja(self):
        return self.datumPostavljanja

    def getSveLicitacije(self):
        return self.licitacija_set.all()

    def getZeljenoPolje(self, string):
        if string == "cena":
            return self.cena
        if string == "brojPregleda":
            return self.brojPregleda
        if string == "datumPostavljanja":
            return self.datumPostavljanja
        if string == "brojLicitacija":
            return len(self.licitacija_set.all())


class Licitacija(models.Model):
    vremeLicitacije = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    cena = models.IntegerField(default=None, blank=False)
    licitacionar = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=True)
    oglas = models.ForeignKey(Oglas, on_delete=models.CASCADE, null=True, default=None, blank=False)

