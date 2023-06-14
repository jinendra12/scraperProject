# Generated by Django 4.2.2 on 2023-06-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinMarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('one_h_percent', models.CharField(max_length=255)),
                ('twentyFour_h_percent', models.CharField(max_length=255)),
                ('seven_d_percent', models.CharField(max_length=255)),
                ('market_cap', models.CharField(max_length=255)),
                ('volume_24h', models.CharField(max_length=255)),
                ('circulating_supply', models.CharField(max_length=255)),
            ],
        ),
    ]
