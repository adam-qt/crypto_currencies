from django.urls import path
from .views import  CryptoListView, update, CryptoDetailView, FavouriteListView, add_to_favourite_list, remove_from_favourite_list
app_name = 'crypto_currencies'
urlpatterns = [
    path('', CryptoListView.as_view(), name = 'crypto_list' ),
    path('update/', update, name='update'),
    path('page/<int:page>/', CryptoListView.as_view(), name='paginator'),
    path('detail/<int:pk>', CryptoDetailView.as_view(), name = 'detail_view' ),
    path('detail/<int:pk>/add',add_to_favourite_list, name = 'add_to_favourites'),
    path('detail/<int:pk>/remove',remove_from_favourite_list, name = 'remove_from_favourites'),
    path('favourites/', FavouriteListView.as_view(), name = 'favourites'),
]