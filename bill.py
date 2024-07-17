from datetime import date


class Bill:
    def __init__(self, name, amount, due_date, is_paid=False):
        self.name: str = name
        self.amount: float = amount
        self.due_date: date = due_date
        self.is_paid: bool = is_paid
        self.is_late: bool = False

    def check_due_date(self):
        print(f"Today is {date.today()} and '{self.name}' is due on {self.due_date}.")
        if self.due_date < date.today():
            self.is_late = True

    def check_is_paid(self):
        if self.is_paid:
            print(f"Bill of {self.amount} has been paid")
        else:
            print(f"Bill of {self.amount} has not been paid")

    def check_is_late(self):
        if self.is_late:
            days_past_due = date.today() - self.due_date
            print(f"'{self.name}' is {days_past_due.days} days past due!")
        else:
            days_until_due = self.due_date - date.today()
            print(
                f"You still have {days_until_due.days} days until '{self.name}' is due."
            )
