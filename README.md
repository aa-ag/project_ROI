#ROI Calculator

* Friday EOD: started with OOP -- it would not work.
* Saturday: scratched what I had, and converted into LinkedList. That also would not work. By EOD, scratched that as well
* Saturday EOD: came up with this non-OOP, which ran successfully
_included basic operations only: TOTAL income, TOTAL expenses, etc_

```
income = int(input("* Enter monthly expected TOTAL income for this property: \n"))
expenses = int(input("* Enter monthly expected TOTAL expenses for this property: \n"))
investment = int(input("* How much will you invest in TOTAL to buy this property? \n"))
annual_cashflow = (income * 12) - (expenses * 12)
tell_cashflow = print(f"* Expected annual cashflow for this property: {annual_cashflow}\n")
roi = round((annual_cashflow / investment) * 100, 2)
tell_roi = print(f"* Expected Return on Investment: {roi}%\n")
```

* Sunday: found tutorial to make OOP calculator and decided to 
use what I had, and transform it into a class. That ^ wouldn't work either, so I came up with an even simpler version that still had a class, and two methods, but needed to be instantiated

```
class ROI():

    def cashflow(income, expenses):
        print((income * 12) - (expenses * 12))

    def roi(cashflow, investment):
        print(f"{(cashflow / investment) * 100}%")

cashflow = ROI.cashflow(1000, 300)
ROI.roi(8400, 200000)
```

* Sunday by noon: was able to create current version.
* Monday: while meeting with Jack and Jackie, we discussed potential bugs, I had not been able to fix user input different from int/float, fixed with try-except. 