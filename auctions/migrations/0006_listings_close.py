# Generated by Django 4.1 on 2022-10-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]
