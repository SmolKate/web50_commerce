# Generated by Django 3.2.9 on 2022-02-16 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('listing', 'username')},
        ),
    ]
