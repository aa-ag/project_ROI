class ROIcalculator():
    def __init_(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def income(self):
        try:
            self.income = float(input("\n* Enter property's TOTAL monthly income as a number: \n"))
            return self.income
        except Exception:
            print("*** Uh-oh! Dunno what that means... please enter a number.")

    def expenses(self):
        try:
            self.expenses = float(input("\n* Enter property's monthly expenses as a number: \n"))
            return self.expenses
        except Exception:
            print("*** Uh-oh! Dunno what that means... please enter a number.")

    def investment(self):
        try:
            self.investment = float(input("\n* Enter TOTAL investment required for you to acquire this property: \n"))
            return self.investment
        except Exception:
            print("\n*** Uh-oh! Dunno what that means... please enter a number.")

    def cashflow(self):
        self.cashflow = (self.income * 12) - (self.expenses * 12)
        if self.cashflow <= 0:
            print("\n* STEER CLEAR: Seems like expected expenses are higher than or equal to the expected income.\n")
        else:
            print(f"* This property's expected annual cashflow: ${round(self.cashflow, 2)}.\n")
    
    def roi(self):
        self.roi = self.cashflow / self.investment * 100
        print(f"* This property's expected Return on Investment: {round(self.roi, 2)}%.\n")

def calculate():
    a_property = ROIcalculator()

    while True:
        start = input("\n* Enter 'start' to get started or 'quit' to leave: \n")
        if start.lower() == 'start':
            a_property.income()
            a_property.expenses()
            a_property.investment()
            a_property.cashflow()
            a_property.roi() 
            break
        elif start.lower() == 'quit':
            print("\n * Thanks for stopping by!\n")
            break

calculate()
