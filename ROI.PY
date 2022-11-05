import time 
from time import sleep 
import math

class ROI():

    def __init__(self):
        self.mortgage = []
        self.fees = {
            "taxes": 150,
            "insurance": 100,
            "water": 30,
            "garbage": 30,
            "sewer": 30,
            "lawn care": 500,
            "property management": 200,
        }
        self.income = {}
        self.units = []
        self.cash_flow = []

    def cost(self):
        home_cost = int(input("What is the cost of the home you are interested in purchasing ? "))
        down_payment = int(input("What percentage can you put down? "))
        result = (down_payment)/100
        result2 = (result)*(home_cost)
        self.mortgage.append(result2)
        loan = (home_cost) - (result2)
        m = 12 # months in a year
        l = 30 # length of loan 
        r = 0.05 # interest rate
        mortgage = (loan)                 
        mortgage_calc = (1-(1+r/m)**(-m*l))/(r/m)
        monthly_payment = float(mortgage/mortgage_calc)
        self.fees["mortgage"] = monthly_payment
        
        unit = int(input("How many units would you be able to rent out? "))
        self.units.append(unit)
        extra_cost = unit*100
        self.fees["capital expenditures"] = extra_cost
        self.fees["repairs"] = extra_cost
        rent = int(input("If you choose to rent out the space, how much would you charge a month in total? "))
        self.income["monthly rent for all units combines"] = rent
        result3 = float(rent)*0.05
        self.fees["vacancy"] = result3
        self.Income()

    def Income(self):
        sleep(1)
        print("\n")
        print("Great, now that you have an idea of how much you can charge for rent let's see some other ways you can make additional income.")

        alternative_income = input("What sources of alternative income will you have? Charge for laundry, offer storage unit, a parking space, all of the above, or nothing else? ")
        
        if alternative_income.lower() == "charge for laundry":
            print("This is a great way to add some extra income.")
            laundry = int(input("The average person does about 6 loads of laundry a month. How much would you like to charge for using a washer AND dryer? "))
            if alternative_income not in self.income.keys():
                self.income[alternative_income] = (laundry*6)* [self.units] # error calculating this. it prints the self.units 12 times from the laundry*6
                print(self.income)
                #self.expenses()
                
        if alternative_income.lower() == "offer storage unit":
            storage = int(input("A storage unit conveniently located in the building can go for about $50-$100/month. How much would you like to charge for storage? "))
            if alternative_income not in self.income.keys():
                self.income[alternative_income] = storage
                #self.expenses()
        
                
        if alternative_income.lower() == "a parking space":
            parking = int(input("How much would you like to charge for parking? If it is a covered spot you can charge a bit more. "))
            if alternative_income not in self.income.keys():
                self.income[alternative_income] = parking
                #self.expenses()
                
        if alternative_income.lower() == "all of the above":
            laundry = int(input("The average person does about 6 loads of laundry a month. How much would you like to charge for using a washer AND dryer? "))
            self.income["laundry"] = (laundry*6)* [self.units] # error calculating this. it prints the self.units 12 times from the laundry*6
            storage = int(input("A storage unit conveniently located in the building can go for about $50-$100/month. How much would you like to charge for storage? "))
            self.income["storage"] = storage                
            parking = int(input("How much would you like to charge for parking? If it is a covered spot you can charge a bit more. "))
            self.income["parking"] = parking
            print(self.fees)
            print(self.income)
            self.expenses()
            
        if alternative_income.lower() == "none":
            print("Looks like you are not a greedy landlord. Let's move on. ")
        self.expenses()

    def expenses(self):
        print("\n")
        sleep(1)
        print("Another thing you have to think about is all the additional expenses when purchasing property.")
        print("\n")
        sleep(1)
        print("The tenent should be responsible for gas, electric, and internet but the rest are generally covered by the owner. For now I will add the rest to your total cost based on the average for the area. Taxes: $150, insurance: $100, water: $30, garbage: $30, sewer: $30, lawn care: $500.")
        print("\n")
        sleep(1)
        print("Now some additional expenses that you should keep in mind that are more like emergency funds. You should account for saving some of your income in case there is a vacancy, for any repairs that are needed, and also capital expenditures.")
        print("\n")
        sleep(1)
        print("For vacancy it is recommeded that you save 5 percent of your rental income. I can go ahead and automatically calculate that for you.")
        print("\n")
        sleep(1)
        print("For repairs and capital expenditures you should save about $100 per month per unit. I can also calculate this for you and add it to your total costs.")
        print("\n")
        sleep(1)
        print("The last two things you should think about are your mortgage cost and property management fees. Property management can vary but I would recommend saving $200 a month. Your mortgage is going to depend on how much money you put down.")
        self.cashflow()


    def cashflow(self):
        print("\n")
        sleep(1)
        print("Now that we have figured out your monthly income as well as monthly expenses we can see how much money you will earn each month. To figure that out we can subtract the total expenses from the total income.")
        total_expenses = sum(int(self.fees.values()))
        total_income = sum(int(self.income.values()))
        cash_flow = total_income - total_expenses
        cash_flow2 = float(cash_flow)
        self.cash_flow.append(cash_flow2)
        print(f"The total cash flow you will have each month based on all the expenses and the income you can earn is {cash_flow} a month.")
        self.cash_on_cash()

    def cash_on_cash(self):
        print("\n")
        sleep(1)
        print("The last factor we need to calculate is called cash on cash return on investment. To do this you can multiply your monthly cash flow by 12 to see how much is made anually. Then divide that by your total investment. Your total investment will include your down payment and closing costs. That will give you a percentage for your cash on cash ROI.")
        return_investment = (self.cash_flow * 12) / int((self.mortgage + 3000))
        flt_invest = float(return_investment)
        sleep(1)
        print("\n")
        print(f"Your cash on cash return on investment is {flt_invest} percent")

class Calc:

    def run():
        my_calc = ROI()
        while True: 
            intro = input("Welcome to Bigger Pockets. Our goal is to help you calculate your ROI to see if this investment is something that would be worth it to you. To get started you can enter 'S' to start the process from the beginning or 'Q' to quit. ")
            if intro.lower() == 's':
                my_calc.cost()
            elif intro.lower() == "q":
                print("Guess you will never know... Bye")
                break 
            else:
                print("Invalid input, please try again.")


Calc.run()

