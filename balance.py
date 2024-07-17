from datetime import date


class Balance:
    def __init__(self, amount=0, bills=[]):
        self.amount: float = amount
        self.date = date.today()
        self.bills = bills

    def add(self, amount):
        self.amount += amount

    def subtract(self, amount):
        self.amount -= amount

    def view_balance(self):
        print(f"Current balance is: ${self.amount}.")

    def add_bill(self, bill):
        self.bills.append(bill)

    def view_bills(self):
        print("Current Bills:")
        for bill in self.bills:
            print(f"'{bill.name}' is ${bill.amount} due {bill.due_date}.")

    def check_past_due_bills(self):
        print("Checking bill due dates...")
        for bill in self.bills:
            bill.check_is_late()
