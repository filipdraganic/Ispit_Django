# Generated by Django 3.0.2 on 2020-01-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oglas', '0004_oglas_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='prodavac',
            field=models.IntegerField(default=0),
        ),
    ]
