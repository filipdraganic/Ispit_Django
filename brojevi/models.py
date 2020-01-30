from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

# Create your models here.
from django import forms
from django.forms import TextInput, NumberInput

IZBORI = (
    ('cena', 'Cena oglasa'),
    ('brojPregleda', 'Broj pregleda'),
    ('brojLicitacija', 'Broj licitacija po oglasu'),
    ('brojLicitacijaKorisnik', 'Broj licitacija po korisniku'),
    ('brojOglasaKorisnik', 'Broj oglasa po korisniku')

)


class Brojevi(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    prvoPolje = models.CharField(blank=False, null=True, choices=IZBORI, default='brojPregleda', max_length=22)
    drugoPolje = models.CharField(blank=False, null=True, choices=IZBORI, default='cena', max_length=22)
    # id = models.CharField(validators=[numeric])
    # ime = models.CharField(max_length=22)
    # cena = models.CharField(max_length=22)
    # brojPregleda = models.CharField(max_length=22)
    # kategorija = models.CharField(max_length=22)
    # preostaloVreme = models.CharField(max_length=22)
    # prodavac_id = models.CharField(max_length=22)

class BrojeviForma(forms.ModelForm):
    class Meta:
        model = Brojevi
        fields = ['prvoPolje']

    def clean_data(self):
        prvo = self.cleaned_data['prvoPolje']

        return prvo


class FilterForma(forms.Form):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    id = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
    ime = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[a-zA-Z]+', 'title':'Enter text Only '}))
    cena = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
    brojPregleda = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
    kategorija = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[a-zA-Z]+', 'title':'Enter text Only '}))
    preostaloVreme = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
    prodavac_id = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))

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
