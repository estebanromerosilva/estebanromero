# Generated by Django 2.2.7 on 2019-11-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]