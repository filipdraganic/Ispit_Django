# Generated by Django 3.0.2 on 2020-01-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oglas', '0002_oglas_preostalovreme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='preostaloVreme',
            field=models.IntegerField(default=60000, null=True),
        ),
    ]
