from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('index/', views.crypto_index, name='index'),
    path('assets/<int:crypto_id>/', views.crypto_detail, name = 'detail'),
    path('assets/create/', views.CryptoCreate.as_view(), name = 'crypto_create'),
    path('crypto/<int:pk>/update', views.CryptoUpdate.as_view(), name = 'crypto_update'),
    path('crypto/<int:pk>/delete', views.CryptoDelete.as_view(), name = 'crypto_delete'),
    path('crypto/<int:crypto_id>/add_trade/', views.add_trade, name='add_trade'),
     path('crypto/<int:crypto_id>/assoc_marketplace/<int:marketplace_id>/', views.assoc_marketplace, name='assoc_marketplace'),
]