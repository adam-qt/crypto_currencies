from django.shortcuts import render
from crypto_currencies.models import Crypto
from .permissions import IsAccountAdminOrReadOnly
from rest_framework import generics, viewsets
from .serializers import UserSerializer, CryptoSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from crypto_currencies.models import Crypto
from .permissions import IsAccountAdminOrReadOnly


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CryptoViewSet(viewsets.ModelViewSet):
    serializer_class = CryptoSerializer
    queryset = Crypto.objects.all()

    def get_permissions(self):
        permission_classes = [IsAccountAdminOrReadOnly]
        return [permission() for permission in permission_classes]


class FavouritesViewSet(generics.ListAPIView):

    serializer_class = CryptoSerializer
    def get_queryset(self):
        user_name = self.request.user
        queryset = User.objects.get(username=user_name).favourite.all()
        return queryset

