# Generated by Django 4.2.2 on 2023-06-14 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coinmarketdata',
            old_name='one_h_percent',
            new_name='percent_1h',
        ),
        migrations.RenameField(
            model_name='coinmarketdata',
            old_name='seven_d_percent',
            new_name='percent_24h',
        ),
        migrations.RenameField(
            model_name='coinmarketdata',
            old_name='twentyFour_h_percent',
            new_name='percent_7d',
        ),
    ]