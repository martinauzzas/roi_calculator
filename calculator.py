class Calculator():
    def __init__(self):
        self.income = int(input("What's the monthly income for this property? "))
        self.expenses = int(input("What's the total of the monthly expenses? "))
        self.investment = int(input("What's the total of the investment you made? "))

    def getProfit(self):
        global profit
        profit = self.income - self.expenses 
        print(f"The monthly profit for this property is: {profit}")

    def getRoi(self):
        cash_flow = profit * 12
        calculate_roi = cash_flow/self.investment * 100
        print(f"Your Return on Investment is {calculate_roi}%")

test1 = Calculator()
test1.getProfit()
test1.getRoi()
        