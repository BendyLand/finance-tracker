"""
Planning:
 - Add budget.
 - Add bills.
 - Add frequency to budget and bills.
 - Design API to allow interaction with budget and bills:
     - (can I afford x at this time? how much money will I need on y date to afford my bills before I get paid? etc.).
 - Design visual layout.
"""


class Balance:
    def __init__(self, amount=0):
        self.amount: float = amount

    def add(self, amount):
        self.amount += amount

    def subtract(self, amount):
        self.amount -= amount

    def view(self):
        print("Current balance is:", self.amount)


class Bill:
    def __init__(self, amount, is_paid=False):
        self.amount: float = amount
        self.is_paid = is_paid

    def check_is_paid(self):
        if self.is_paid:
            print(f"Bill of {self.amount} has been paid")
        else:
            print(f"Bill of {self.amount} has not been paid")


balance = Balance(1000)
bill = Bill(200)
balance.view()
bill.check_is_paid()
balance.subtract(bill.amount)
bill.is_paid = True
bill.check_is_paid()
balance.view()

