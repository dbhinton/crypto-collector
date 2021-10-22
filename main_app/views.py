from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Crypto

# # Add the following import
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def crypto_index(request):
  crypto = Crypto.objects.all()
  return render(request, 'assets/index.html', { 'cryptos': crypto})

def crypto_detail(request, crypto_id):
  crypto = Crypto.objects.get(id = crypto_id)
  return render(request, 'assets/detail.html', { 'crypto': crypto })

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
