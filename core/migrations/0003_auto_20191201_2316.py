# Generated by Django 2.2.7 on 2019-12-02 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191129_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
    ]