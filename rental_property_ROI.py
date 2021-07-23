import os
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

class ROI:
    def __init__(self, income = 0, expenses = 0, investment = 0, cash_flow = 0):
        self.income = income
        self.expenses = expenses
        self.investment = investment
        self.cash_flow = cash_flow

    def make_int(self, num):
        num = num.strip('$ ').replace(',', '')
        while not num.isnumeric():
            num = input("Invalid entry. Please enter an integer: ")
            num = num.strip('$ ').replace(',', '')
        return int(num)
        
    def calc_income(self):
        print("INCOME" + "\n" + "-"*80)
        rental_income = self.make_int(input("What is your total monthly rental income? "))
        print("Enter the total monthly amount of any additional income (laundry, storage, etc.). ")
        extra_income = self.make_int(input("Enter 0 if there is no additional income. "))
        self.income = rental_income + extra_income
        return self.income

    def calc_expenses(self):
        print("EXPENSES" + "\n" + "-"*80)
        mortgage = self.make_int(input("What is the monthly mortgage payment? "))
        tax = self.make_int(input("What is the monthly tax payment? "))
        insurance = self.make_int(input("What is the monthly insurance payment? "))
        print("Enter the total monthly amount of any additional expenses (utilities, repairs, etc.). ")
        extra_income = self.make_int(input("Enter 0 if there are no additional expenses. "))
        self.expenses = mortgage + tax + insurance + extra_income
        return self.expenses

    def calc_cash_flow(self):
        self.cash_flow = self.income - self.expenses

    def calc_investment(self):
        down_pmt = self.make_int(input("What is the down payment? "))
        closing_costs = self.make_int(input("What are the closing costs? "))
        rehab_budget = self.make_int(input("What is the rehab budget? "))
        self.investment = down_pmt + closing_costs + rehab_budget
        return self.investment

    def calc_ROI(self):
        cash_flow = (self.income - self.expenses) * 12
        return f"{round((cash_flow / self.investment) * 100, 2)} %"

def run():
    clear()
    new_roi = ROI()
    print("="*80 + "\n" + "RENTAL PROPERTY ROI CALCULATOR" + "\n" + "="*80 + "\n")
    new_roi.calc_income()
    clear()

    print("="*80 + "\n" + "RENTAL PROPERTY ROI CALCULATOR" + "\n" + "="*80 + "\n")
    print("MONTHLY INCOME -- $" + str(new_roi.income) + "\n" + "-"*80)
    new_roi.calc_expenses()
    new_roi.calc_cash_flow()
    annual_cash = new_roi.cash_flow * 12
    clear()

    print("="*80 + "\n" + "RENTAL PROPERTY ROI CALCULATOR" + "\n" + "="*80 + "\n")
    print("MONTHLY INCOME -- $" + str(new_roi.income) + "\n" + "-"*80)
    print("MONTHLY EXPENSES -- $" + str(new_roi.expenses) + "\n" + "-"*80)
    print("MONTHLY CASH FLOW -- $" + str(new_roi.cash_flow) + "\n" + "-"*80)
    print("ANNUAL CASH FLOW -- $" + str(annual_cash) + "\n" + "-"*80)
    print("INVESTMENT" + "\n" + "-"*80)
    new_roi.calc_investment()
    clear()

    print("="*80 + "\n" + "RENTAL PROPERTY ROI CALCULATOR" + "\n" + "="*80 + "\n")
    print("MONTHLY INCOME -- $" + str(new_roi.income) + "\n" + "-"*80)
    print("MONTHLY EXPENSES -- $" + str(new_roi.expenses) + "\n" + "-"*80)
    print("MONTHLY CASH FLOW -- $" + str(new_roi.cash_flow) + "\n" + "-"*80)
    print("ANNUAL CASH FLOW -- $" + str(annual_cash) + "\n" + "-"*80)
    print("TOTAL INVESTMENT -- $" + str(new_roi.investment))

    print("="*80)
    print(f"** Your ROI is {new_roi.calc_ROI()} **")
    print("="*80 + "\n")
run()