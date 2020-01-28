from django.db import models

# Create your models here.
from django import forms

IZBORI = (
    ('datumPostavljanja', 'Datum postavljanja'),
    ('cena', 'cena'),
    ('brojPregleda', 'Broj pregleda'),
    ('brojLicitacija', 'Broj licitacija')
)


class Brojevi(models.Model):
    prvoPolje = models.CharField(blank=False, null=True, choices=IZBORI, default='brojPregleda', max_length=20)
    drugoPolje = models.CharField(blank=False, null=True, choices=IZBORI, default='cena', max_length=20)


class BrojeviForma(forms.ModelForm):
    class Meta:
        model = Brojevi
        fields = ['prvoPolje']

    def clean_data(self):
        prvo = self.cleaned_data['prvoPolje']

        return prvo

class GrafForma(forms.ModelForm):
    class Meta:
        model = Brojevi
        fields = ['prvoPolje', 'drugoPolje']

    def clean_data(self):
        prvo = self.cleaned_data['prvoPolje']
        drugo = self.cleaned_data['drugoPolje']

        return prvo, drugo
