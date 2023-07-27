from rest_framework import serializers
from django.contrib.auth.models import User
from crypto_currencies.models import Crypto


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "total_supply",
            "market_cap",
            "volume_change_24h",
            "percent_change_24h",
            "user_favourite",
        ]


class UserSerializer(serializers.ModelSerializer):
    favourite = CryptoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "favourite"]
