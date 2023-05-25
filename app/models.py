from os import name
from django.db import models
from django.contrib.auth.models import User


class Trader(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    total_profit = models.FloatField()
    total_loss = models.FloatField()
    total_balance = models.FloatField(default=100)

    def __str__(self):
        return f"{self.name}"


class TraderData(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.FloatField()

    def __str__(self):
        return f"Trader: {self.trader.name},  Profit/Loss: {self.profit_loss}"
