from django.shortcuts import render
from .models import Crypto
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .services import parse_data_to_db, download_data_from_api, remove_from_favourite, add_to_favourite
from django.contrib.auth.models import User


class CryptoListView(ListView):
    model = Crypto
    template_name = 'crypto_currencies/list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        search_query = self.request.GET.get('search_query')
        sort_param = self.request.GET.get('sort')
        if search_query:
            queryset = Crypto.objects.filter(
                name__istartswith=search_query) | Crypto.objects.filter(
                slug__istartswith=search_query).order_by('name')

        if sort_param:
            queryset = Crypto.objects.all().order_by(
                sort_param if sort_param not in [
                    'price', 'percent_change_24h'] else f'-{sort_param}')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CryptoListView, self).get_context_data()
        context['user'] = self.request.user

        return context


class CryptoDetailView(DetailView):
    model = Crypto
    template_name = 'crypto_currencies/detail_view.html'
    context_object_name = 'crypto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        isAdded = False
        context['user'] = self.request.user
        is_log_user = self.request.user.is_authenticated
        if is_log_user:
            if self.object in self.request.user.favourite.all():
                isAdded = True

            context['isAdded'] = isAdded

        return context


class FavouriteListView(ListView):
    model = User
    template_name = 'crypto_currencies/favourites.html'

    def get_queryset(self):
        user_name = self.request.user
        user_object = User.objects.get(username=user_name)
        queryset = user_object.favourite.all().select_related().order_by('name')
        sort_param = self.request.GET.get('sort')
        if sort_param:
            queryset = user_object.favourite.all().select_related().order_by(
                sort_param if sort_param not in [
                    'price', 'percent_change_24h'] else f'-{sort_param}')
        return queryset


def add_to_favourite_list(request, pk):
    add_to_favourite(request, pk)
    return HttpResponseRedirect(reverse('crypto_currencies:favourites'))


def remove_from_favourite_list(request, pk):
    remove_from_favourite(request,pk)
    return HttpResponseRedirect(reverse('crypto_currencies:favourites'))


def update(request):
    parse_data_to_db(download_data_from_api())
    return HttpResponseRedirect(reverse('crypto_currencies:crypto_list'))
