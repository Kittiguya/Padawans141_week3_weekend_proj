# Lines 2-6 is about what im making. Lines 8-16 is some info bout my personality im going to try to incorporate. Lines 24-43 are the info i need to create the function. 
#  Calculate rental property ROI.
#  Looking to create a program that calculates the return on investment for a rental property. 
#  Will need user inputs.
#  Will require OOP (Object Oriented Programming, AKA OOP OOP OOP), lots of .self everywhere (lucky you Robin, literally the thing i feel most confident doing so far.)
#   I'mma be trying to make this mostly user inputted. It would be the cherry on top here. 
#
#                                              Use the values from below to check it out. Or make up your own! :)
#                                                 INFO ON THE HOUSE FROM VIDEO BELOW
#  $200,000 property
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
#  Down Payment- $40,000, Closing Costs- $3,000 (for this case), Rehab (repair) budget- $7,000 (we painting the house boyo!!), -- i didnt include this in user inputs. Rip
#  MISC OTHERS AKA AREAS YOU MIGHT SPEND MONEY before purchasing or during purchasing
#  Total investment: $50,000 added from the lines above, 
#  Annual cash flow == $4,680 // total investment = 0.0936 but converted to percentages by moving decimal 2 places to the right is: 9.36%
#  CoCROI == 9.36%

class RentalProp:
    def __init__(self):
        self.rental_income = {}
        self.expenses = {}
        self.initial_investment = {}
        self.total_investment = 0

    def user_input(self):
        print("\nEnter your initial investment costs")
        self.initial_investment['down_payment'] = float(input("What is your down payment?: $").replace(',', '').replace('$', ''))
        self.initial_investment['closing_costs'] = float(input("What were the closing costs?: $").replace(',', '').replace('$', ''))
        self.initial_investment['repair_budget'] = float(input("What is your Rehab/Repair budget?: $").replace(',', '').replace('$', ''))

        self.total_investment = sum(self.initial_investment.values())      

        print("Enter rental income")                                       
        self.rental_income['rent'] = float(input("Whats is your rental income?: $").replace(',', '').replace('$', ''))                           #user inputting rent payment
        self.rental_income['laundry'] = float(input("What are your laundry costs?: $").replace(',', '').replace('$', ''))                               # user inputting laundry costs per month
        self.rental_income['storage'] = float(input("What is the cost of your Storage?: $").replace(',', '').replace('$', ''))                           #user inputting cost of storage each month
        self.rental_income['miscellaneous'] = float(input("Do you have any miscellaneous costs? If so please add the total.: $").replace(',', '').replace('$', ''))     #just random costs, could be alcohol, could be games, could be car parts, could be random trips out of town
        

        print("\nEnter Monthly expenses: ")
        self.expenses['tax'] = float(input("What is your monthly tax payment?: $").replace(',', '').replace('$', ''))                                                             #How much do you pay in taxes for the property per month
        self.expenses['insurance'] = float(input("How much does your insurance cost?: $").replace(',', '').replace('$', ''))                                           #how much is the total cost for insurance on the property and your vehicles
        self.expenses['utilities'] = float(input("What is the total cost of your Utilities?: $").replace(',', '').replace('$', ''))                                         #Electric, gas, water, internet, cable, car payment etc..
        self.expenses['hoa_fees'] = float(input("Do you have any HOA fees?: $").replace(',', '').replace('$', ''))                                               #Do you have any weird ass HOA fees you gotta pay? Those people are just weird
        self.expenses['lawn_care'] = float(input("What is your monthly Lawn maintence cost?: $").replace(',', '').replace('$', ''))                                             #How much do you spend per month to maintain basic lawn care year round.
        self.expenses['vacancy'] = float(input("What is your expected vacancy cost?: $").replace(',', '').replace('$', ''))                                         # Vacancy as a whole is weird to me. But i included it. 
        self.expenses['repairs'] = float(input("How much do you have for repairs each month?: $").replace(',', '').replace('$', ''))                                     #how much do you think youll repair on average each month? (set the money aside if no repairs are needed)
        self.expenses['capex'] = float(input("What is the Capital Expenditures (CapEx) cost?: $").replace(',', '').replace('$', ''))                            #Cash on Cash Return on Investment? This is a mouthful and hurts my brain trying to understand
        self.expenses['property_management'] = float(input("Do you have a property manager? If so, how much do they cost?: $").replace(',', '').replace('$', ''))                    #This is the cost of whether or not youre paying someone else to manage the property for you AKA a manager
        self.expenses['mortgage'] = float(input("What is your monthly Mortgage payment?: $").replace(',', '').replace('$', ''))                                      #This is your monthly mortgage cost
                                                
          

    def calc_cash_flow(self):                
        total_income = sum(self.rental_income.values())                    # sum() is adding up the values of the given dic/list from user input for self.rental_income
        total_expenses = sum(self.expenses.values())                       # same thing as line above. just adds the values from user inputted self.expenses
        cash_flow = total_income - total_expenses                          #this line literally deducts total expenses from total income to give you cash flow value.
        return cash_flow
    
    def calc_cocroi(self):                                                  # this func, uses the cash_flow acquired from above to perform math to get the CoCROI
        cash_flow = self.calc_cash_flow()
        ann_cash_flow = cash_flow * 12                                      
        cocroi = (ann_cash_flow / self.total_investment) * 100
        return cocroi
    
    def display_results(self):                                                    #this function is showing you the monthly cash flow and your COCROI :) 
        cash_flow = self.calc_cash_flow()
        cocroi = self.calc_cocroi()
        print("\nTotal Monthly Cash Flow: ${:.2f}".format(cash_flow))
        print("Cash on Cash Return on Investment (CoCROI): {:.2f}%".format(cocroi))

    def main():                                                    
        calculator = RentalProp()
        calculator.user_input()
        calculator.display_results()

if __name__ == "__main__":
    RentalProp.main()                                               # note: if you input the values as $5,000 itll error out due to the comma and the $ somehow im not sure how to fix that. 
                                                                    # Just use; example: 5000 or 500 or 50000 no commas, no periods, or dollar signs please!
                                                                    # Maybe ill fix monday before class. I found an answer but it gave me errors elsewhere, and i didnt wanna continue messing with it
                                                                    # The thing i struggle the most with: is coming up with what to name things. I hope that gets easier! 
                                                                    # Oop so far seems to be the easiest thing for me to pick up. The more i mess with this all the easier itll get im sure! 