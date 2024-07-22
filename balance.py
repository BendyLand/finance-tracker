from datetime import date
import numpy as np
import json


class Balance:
    def __init__(self, amount=0, bills=np.array([])):
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
        self.bills = np.append(self.bills, bill)

    def view_bills(self):
        print("Current Bills:")
        for bill in self.bills:
            print(f"'{bill.name}' is ${bill.amount} due {bill.due_date}.")

    def check_past_due_bills(self):
        print("Checking bill due dates...")
        for bill in self.bills:
            bill.check_is_late()

    def save_bills_to_file(self):
        with open("bills.json", "w") as file:
            temp = {}
            for bill in self.bills:
                temp[bill.name] = {
                    "Amount": bill.amount,
                    "Due_Date": str(bill.due_date),
                    "Is Paid?": bill.is_paid,
                    "Is Late?": bill.is_late,
                }
            line = json.dumps(temp)
            file.write(line)

def new_date(string):
    month, day, year = string.split("/")
    return date(int(year), int(month), int(day))
