import requests
from .models import Crypto
from django.db import Error
import requests
from django.conf import settings
from django.contrib.auth.models import User


def download_data_from_api():
    url = settings.API
    key = settings.API_TOKEN
    api_header = settings.API_HEADER
    headers = {
        api_header: f'{key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        data = e
    return data


def parse_data_to_db(data):
    for coin in data['data']:
        name = coin['name']
        unit, _ = Crypto.objects.get_or_create(name=name)
        try:
            unit.slug = coin['symbol']
            unit.total_supply = coin['total_supply']
            unit.price = int(coin['quote']['USD']['price'])
            unit.market_cap = int(coin['quote']['USD']['market_cap'])
            unit.volume_change_24h = float("{:.2f}".format(
                coin['quote']['USD']['volume_change_24h']))
            unit.percent_change_24h = float("{:.2f}".format(
                coin['quote']['USD']['percent_change_24h']))
            unit.save()

        except (KeyError, ValueError, TypeError) as e:
            return e


def remove_from_favourite(request, pk):
    crypto_object = Crypto.objects.get(pk=pk)
    user_object = User.objects.get(username=request.user.username)
    user_object.favourite.remove(crypto_object)


def add_to_favourite(request, pk):
    crypto_object = Crypto.objects.get(pk=pk)
    user_object = User.objects.get(username=request.user.username)
    user_object.favourite.add(crypto_object)
