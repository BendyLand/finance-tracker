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
from balance import Balance
from datetime import date


account = Balance(1000)
bill = Bill("Example", 250, date(2024, 7, 30))
bill2 = Bill("Example2", 300, date(2024, 7, 28))
account.add_bill(bill)
account.add_bill(bill2)
account.view_bills()
account.view_balance()
account.check_past_due_bills()
account.save_bills_to_file()

