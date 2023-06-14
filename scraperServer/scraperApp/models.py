from django.db import models


class CoinMarketData(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    percent_1h = models.CharField(max_length=255)
    percent_24h = models.CharField(max_length=255)
    percent_7d = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    volume_24h = models.CharField(max_length=255)
    circulating_supply = models.CharField(max_length=255)