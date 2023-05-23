# tasks.py

from .models import Trader, TraderData

import random
from datetime import datetime
from django.core.management.base import BaseCommand
from celery import shared_task


@shared_task
def simulate_profit_loss():
    traders = Trader.objects.all()

    for trader in traders:
        # Generate a random profit/loss value for each trader
        profit_loss = random.uniform(-1, 1)  # Example range: -1 to 1

        # Update trader's profit, loss, and total_balance
        trader.profit += profit_loss if profit_loss > 0 else 0
        trader.loss += profit_loss if profit_loss < 0 else 0
        # trader.total_balance += profit_loss
        trader.total_balance = int(trader.total_balance + profit_loss)

        trader.save()

        # Create or update the trader's data for the current minute
        timestamp = datetime.now()
        trader_data, _ = TraderData.objects.get_or_create(
            trader=trader,
            timestamp=timestamp,
            defaults={'profit_loss': profit_loss}
        )
        trader_data.profit_loss = profit_loss
        trader_data.save()

    print('Simulation completed successfully')
