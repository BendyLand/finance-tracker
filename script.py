"""
Planning:
 - Add budget.
 - Add bills.
 - Add frequency to budget and bills.
 - Design API to allow interaction with budget and bills:
     - (can I afford x at this time? how much money will I need on y date to afford my bills before I get paid? etc.).
 - Design visual layout.
"""

from bill import Bill
from balance import Balance, new_date
from datetime import date


def init_account(amount=0):
    account = Balance(amount)
    return account


account = init_account()
