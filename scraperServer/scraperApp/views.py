import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core import serializers

from .coinMarketDataScrapper import get_coinmarketcap_data
from .models import CoinMarketData


class UpdateCoinMarketData(View):
    @staticmethod
    def post(request):
        data_list = json.loads(request.body) if request.body else None

        # Added a fallback just in case if data is not coming it will call the scrapper itself to get the latest data
        if not data_list:
            data_list = get_coinmarketcap_data()

        # For each row updating the db
        for row in data_list:
            CoinMarketData.objects.update_or_create(name=row["name"],
                                                    defaults={"price": row["price"],
                                                              "percent_1h": row["percent_1h"],
                                                              "percent_24h": row[
                                                                  "percent_24h"],
                                                              "percent_7d": row["percent_7d"],
                                                              "market_cap": row["market_cap"],
                                                              "volume_24h": row[
                                                                  "volume_24h"],
                                                              "circulating_supply": row[
                                                                  "circulating_supply"],
                                                              })

        return HttpResponse("Data updated successfully.")


class GetCoinMarketData(View):
    @staticmethod
    def get(request):
        data = CoinMarketData.objects.all()
        res = serializers.serialize('json', data)
        return JsonResponse(res, safe=False)
