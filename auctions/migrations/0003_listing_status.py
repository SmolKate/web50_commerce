# Generated by Django 3.2.9 on 2022-02-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_watchlist_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(default='active', max_length=64),
        ),
    ]