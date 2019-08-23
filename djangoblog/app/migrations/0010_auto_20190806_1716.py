# Generated by Django 2.2.3 on 2019-08-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190806_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_to', through='app.Follow', to='app.Profile'),
        ),
    ]
