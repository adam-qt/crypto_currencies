import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def get_data_for_crypto():
    crypto_data = {
        "name": "Crypto 1",
        "slug": "crypto-1",
        "total_supply": 11,
        "price": 12,
        "market_cap": 2323,
        "volume_change_24h": 11.1,
        "percent_change_24h": 11.1,
        "user_favourite": "",
    }
    return crypto_data


@pytest.mark.django_db
def test_crypto_list():
    client = APIClient()
    response = client.get("/api/crypto/currencies/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crypto_create_method_not_allowed():
    client = APIClient()
    crypto_data = get_data_for_crypto()
    response = client.post("/api/crypto/", data=crypto_data)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED



@pytest.mark.django_db
def test_crypto_detail_not_found():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/api/crypto/", data=crypto_data)
    pk = "145"
    response = client.get(f"/api/crypto/currencies/{pk}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND





