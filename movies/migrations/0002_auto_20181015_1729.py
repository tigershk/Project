# Generated by Django 2.0.9 on 2018-10-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movieid',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='overview',
            field=models.TextField(default=''),
        ),
    ]