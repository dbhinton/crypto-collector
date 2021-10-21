from django.shortcuts import render
from .models import Crypto

# Add the following import
from django.http import HttpResponse

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
  return render(request, 'assets/details.html', { 'crypto': crypto })
