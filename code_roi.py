## Friday EOD: started with OOP -- it would not work.
## Saturday: scratched what I had, and converted into LinkedList
## That also would not work. By EOD, scratched that as well
## Saturday EOD: came up with this non-OOP, which ran successfully
## >>>included basic operations only: TOTAL income, TOTAL expenses, etc<<<

# income = int(input("* Enter monthly expected TOTAL income for this property: \n"))
# expenses = int(input("* Enter monthly expected TOTAL expenses for this property: \n"))
# investment = int(input("* How much will you invest in TOTAL to buy this property? \n"))
# annual_cashflow = (income * 12) - (expenses * 12)
# tell_cashflow = print(f"* Expected annual cashflow for this property: {annual_cashflow}\n")
# roi = round((annual_cashflow / investment) * 100, 2)
# tell_roi = print(f"* Expected Return on Investment: {roi}%\n")

## Sunday: found tutorial to make OOP calculator and decided to 
## use what I had, and transform it into a class
## That ^ wouldn't work either, so I came up with an even simpler version
## that still had a class, and two methods, but needed to be instantiated

# class ROI():

#     def cashflow(income, expenses):
#         print((income * 12) - (expenses * 12))

#     def roi(cashflow, investment):
#         print(f"{(cashflow / investment) * 100}%")

# cashflow = ROI.cashflow(1000, 300)
# ROI.roi(8400, 200000)

## Finally...

class ROIcalculator():
    def __init_(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def cashflow(self):
        self.cashflow = (self.income * 12) - (self.expenses * 12)
        print(round(self.cashflow, 2))
    
    def roi(self):
        self.roi = self.cashflow / self.investment * 100
        print(round(self.roi, 2))

income = int(input("Enter property's TOTAL monthly income as a number: \n"))
expenses = int(input("Enter property's monthly expenses as a number: \n"))
investment = int(input("Enter TOTAL investment required for you to acquire this property: \n"))

a_property = ROIcalculator()

while True:
    if income <= 0:
        print("Obsiouly a bad investment! Let's try another one.\n")
    elif income > 0 and expenses > income:
        print("Obsiouly a bad investment! Let's try another one.\n")
    else:
        print(a_property.cashflow())
        print(a_property.roi())