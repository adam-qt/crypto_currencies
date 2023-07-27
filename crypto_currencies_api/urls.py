from django.urls import path, include
from rest_framework import routers
from .views import CryptoViewSet
from .views import FavouritesViewSet


router = routers.DefaultRouter()
router.register(r'currencies', CryptoViewSet)


urlpatterns = [
    path('blog_api-auth/', include('rest_framework.urls')),
    path('crypto/', include(router.urls), name='api'),
    path('crypto/favourites/', FavouritesViewSet.as_view())
]
