# Lines 2-6 is about what im making. Lines 8-16 is some info bout my personality im going to try to incorporate. Lines 24-43 are the info i need to create the function. 
#  Calculate rental property ROI.
#  Looking to create a program that calculates the return on investment for a rental property. 
#  Will need user inputs.
#  Will require OOP (Object Oriented Programming, AKA OOP OOP OOP), lots of .self everywhere (lucky you Robin, literally the thing i feel most confident doing so far.)
#   I'mma be trying to make this mostly user inputted. It would be the cherry on top here. 
#
#                                              Use the values from below to check it out. 
#                                                 INFO ON THE HOUSE FROM VIDEO BELOW
#  $200,000 property
#  Income: Rental income is "what"? Laundry, storage, misc. How much income they have incoming and available 
#  Rental income: $2,000 per month; $0 for laundry, 0$ for storage, $0 for misc costs 
#  Total monthly income = $2,000
#  
#  Expenses: Tax- $150/mo, Insurance- $100/mo, Utilities- $0 (electric, water, sewer, garbage, gas), HOA fees- $0, Lawn care (grass or snow)- $0, Vacancy- $100, Repairs- $100/mo, 
#   capital expenditures (CapEx)- $100/mo, Property management (using property manager in this case)- $200/mo, Mortgage- $860/mo.
#  TOTAL MONTHLY EXPENSES- $1,610
#  
#  Cash Flow: Income($2,000) - expenses ($1,610) == $390 TOTAL MONTHLY CASH FLOW 
#
#  Cash on Cash Return on Investment (CoCROI): 
#  Down Payment- $40,000, Closing Costs- $3,000 (for this case), Rehab (repair) budget- $7,000 (we painting the house boyo!!), 
#  MISC OTHERS AKA AREAS YOU MIGHT SPEND MONEY before purchasing or during purchasing
#  Total investment: $50,000 added from the lines above, 
#  Annual cash flow == $4,680 // total investment = 0.0936 but converted to percentages by moving decimal 2 places to the right is: 9.36%
#  CoCROI == 9.36%  
#  Sorry about the 42 lines of random bs. But this was fun. 


# total cost; = expenses; = Down payment, Repair budget, Property manager, capital expidentures, Vacancy, 




class RentalProp:
    def __init__(self):
        self.rental_income = {}
        self.expenses = {}
        self.total_investment = 0

    def user_input(self):                                            
        print("Enter rental income")                                          
        self.rental_income['rent'] = float(input("Rental income: "))                           #user inputting rent payment
        self.rental_income['laundry'] = float(input("Laundry: "))                               # user inputting laundry costs per month
        self.rental_income['storage'] = float(input("Storage costs:"))                            #user inputting cost of storage each month
        self.rental_income['miscellaneous'] = float(input("Miscellaneous costs"))                #just random costs, could be alcohol, could be games, could be car parts, could be random trips out of town

        print("\nEnter Monthly expenses: ")
        self.expenses['tax'] = float(input("Taxes: "))                                                             #How much do you pay in taxes for the property per month
        self.expenses['insurance'] = float(input("Insurance costs: "))                                           #how much is the total cost for insurance on the property and your vehicles
        self.expenses['utilities'] = float(input("Utilities cost: "))                                         #Electric, gas, water, internet, cable, car payment etc..
        self.expenses['hoa_fees'] = float(input("HOA Fees: "))                                               #Do you have any weird ass HOA fees you gotta pay? Those people are just weird
        self.expenses['lawn_care'] = float(input("Lawn Care: "))                                              #How much do you spend per month to maintain basic lawn care year round.
        self.expenses['vacancy'] = float(input("Vacancy costs : "))                                         # Vacancy as a whole is weird to me. But i included it. 
        self.expenses['repairs'] = float(input("Estimated Repairs: "))                                     #how much do you think youll repair on average each month? (set the money aside if no repairs are needed)
        self.expenses['capex'] = float(input("Capital Expenditures (CapEx): "))                            #Cash on Cash Return on Investment? This is a mouthful and hurts my brain trying to understand
        self.expenses['property_management'] = float(input("Property Management: "))                    #This is the cost of whether or not youre paying someone else to manage the property for you AKA a manager
        self.expenses['mortgage'] = float(input(" Mortgage: "))                                          #This is your monthly mortgage cost

        self.total_investment = float(input("\nEnter total investment: i.e (Down payment + Closing Costs, + early repairs, etc..)"))     #Total investment, Literally all the money you put up front total cost of it               

    def calc_cash_flow(self):                
        total_income = sum(self.rental_income.values())
        total_expenses = sum(self.expenses.values())
        cash_flow = total_income - total_expenses
        return cash_flow
    
    def calc_cocroi(self):
        cash_flow = self.calc_cash_flow()
        ann_cash_flow = cash_flow * 12
        cocroi = (ann_cash_flow / self.total_investment) * 100
        return cocroi
    
    def display_results(self):
        cash_flow = self.calc_cash_flow()
        cocroi = self.calc_cocroi()
        print("\nTotal Monthly Cash Flow: ${:.2f}".format(cash_flow))
        print("Cash on Cash Return on Investment (CoCROI): {:.2f}%".format(cocroi))

    def main():                                                     # this func is where the math will happen to calculate the ROI for the property using information given above.
        calculator = RentalProp()
        calculator.user_input()
        calculator.display_results()

if __name__ == "__main__":
    RentalProp.main()                                               # note: if you input the values as $5,000 itll error out due to the comma and the $ somehow im not sure how to fix that. 
                                                                    # Just use; example: 5000 or 500 or 50000 no commas, no periods, or dollar signs please!
                                                                    # Maybe ill fix monday before class. I found an answer but it gave me errors elsewhere, and i didnt wanna continue messing with it
                                                                    # The thing i struggle the most with: is coming up with what to name things. I hope that gets easier! 
                                                                    # Oop so far seems to be the easiest thing for me to pick up. The more i mess with this all the easier itll get im sure! 