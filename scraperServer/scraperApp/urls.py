from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('update_coin_market_data/', views.UpdateCoinMarketData.as_view(), name='update_data'),
    path('get_coin_market_data/', views.GetCoinMarketData.as_view(), name='get_latest_data'),
]
