"""
Planning:
 - Add budget.
 - Add bills.
 - Add frequency to budget and bills.
 - Design API to allow interaction with budget and bills:
     - (can I afford x at this time? how much money will I need on y date to afford my bills before I get paid? etc.).
 - Design visual layout.
"""
import datetime

class Balance:
    def __init__(self, amount=0):
        self.amount: float = amount
        self.date = datetime.date.today()

    def add(self, amount):
        self.amount += amount

    def subtract(self, amount):
        self.amount -= amount

    def view(self):
        print("Current balance is:", self.amount)


class Bill:
    def __init__(self, name, amount, due_date, is_paid=False):
        self.name: str = name
        self.amount: float = amount
        self.due_date:datetime.date = due_date
        self.is_paid: bool = is_paid
        self.is_late: bool = False

    def check_due_date(self):
        print(f"'{self.name}' is due on {self.due_date}")
        if self.due_date < datetime.date.today():
            self.is_late = True
            print(f"'{self.name}' is late!")

    def check_is_paid(self):
        if self.is_paid:
            print(f"Bill of {self.amount} has been paid")
        else:
            print(f"Bill of {self.amount} has not been paid")

    def check_is_late(self):
        if self.is_late:
            days_past_due = datetime.date.today() - self.due_date  
            print(f"'{self.name}' is {days_past_due.days} days past due!")
        else:
            days_until_due = self.due_date - datetime.date.today() 
            print(f"You still have {days_until_due.days} days until '{self.name}' is due.")


account = Balance(1000)
bill = Bill("Example", 250, datetime.date(2024, 7, 30))
bill.check_due_date()
bill.check_is_paid()
bill.check_is_late()

