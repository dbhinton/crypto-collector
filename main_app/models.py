from django.db import models
from django.urls import reverse
from datetime import date

class Marketplace(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('marketplace_detail', kwargs={'pk': self.id})


# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length = 25)
    acronym = models.CharField(max_length = 6)
    network = models.CharField(max_length = 25)
    description = models.TextField(max_length = 500)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)

    marketplace = models.ManyToManyField(Marketplace)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"crypto_id": self.id})


class Trade(models.Model):
    date = models.DateField()
    trade_amount = models.DecimalField(max_digits = 20, decimal_places = 2)
    quantity = models.DecimalField(max_digits = 20, decimal_places = 2)

    crypto = models.ForeignKey(Crypto, on_delete = models.CASCADE)
    
    def __str__(self):
        if self.quantity < 1:
            return f"{self.quantity} of a {self.crypto.name} coins/tokens was traded at a price of ${self.trade_amount} on {self.date}"
        elif self.quantity == 1:
            return f"{self.quantity} {self.crypto.name} coins/tokens was traded at a price of ${self.trade_amount} on {self.date}"
        else:
            return f"{self.quantity} {self.crypto.name} coins/tokens were traded at a price of ${self.trade_amount} on {self.date}"

    class Meta:
        ordering = ['-date']
