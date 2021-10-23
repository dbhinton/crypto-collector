from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Crypto
from .models import Marketplace
from .forms import TradeForm

# # Add the following import
# from django.http import HttpResponse

# Define the home view
class CryptoCreate(CreateView):
  model = Crypto
  fields = '__all__'
  success_url = '/index/'


class CryptoUpdate(UpdateView):
  model = Crypto
  fields = ['price']


class CryptoDelete(DeleteView):
  model = Crypto
  success_url = '/index/'  

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def crypto_index(request):
  crypto = Crypto.objects.all()
  return render(request, 'assets/index.html', { 'cryptos': crypto})

def crypto_detail(request, crypto_id):
  crypto = Crypto.objects.get(id = crypto_id)
  marketplaces_asset_is_not_on = Marketplace.objects.exclude(id__in = crypto.marketplace.all().values_list('id'))
  trade_form = TradeForm()

  return render(request, 'assets/detail.html', { 'crypto': crypto, 'trade_form': trade_form, 'marketplace': marketplaces_asset_is_not_on })

def add_trade(request, crypto_id):
  form = TradeForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_trade = form.save(commit=False)
    new_trade.crypto_id = crypto_id
    new_trade.save()
  return redirect('detail', crypto_id=crypto_id)



def assoc_marketplace(request, crypto_id, marketplace_id):
  Crypto.objects.get(id=crypto_id).marketplace.add(marketplace_id)
  return redirect('detail', crypto_id=crypto_id)