# Generated by Django 3.0.2 on 2020-01-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brojevi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prvoPolje', models.CharField(choices=[('datumPostavljanja', 'Datum postavljanja'), ('cena', 'cena'), ('brojPregleda', 'Broj pregleda'), ('brojLicitacija', 'Broj licitacija')], default='brojPregleda', max_length=20, null=True)),
                ('drugoPolje', models.CharField(choices=[('datumPostavljanja', 'Datum postavljanja'), ('cena', 'cena'), ('brojPregleda', 'Broj pregleda'), ('brojLicitacija', 'Broj licitacija')], default='cena', max_length=20, null=True)),
            ],
        ),
    ]
