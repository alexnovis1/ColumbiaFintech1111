##Week One: Project One##
#loan_analyzer 

import csv
from pathlib import Path

## Part 1: Automate the calculations 

loan_costs = [500, 600, 200, 1000, 450]

#1. Use the 'len' function to calculate the total number of loans of prices for 5 loans. 
num_of_loans = len(loan_costs)


#2. Use the `sum` function to calculate the total of all loans in the list.
sum_of_loans = sum(loan_costs)


#3. Using the sum of all loans and the total number of loans, calculate the average loan price.
avg_loan_price = int(sum_of_loans / number_of_loans)

#4. Print all calculations with a descriptive message 
print("Part 1 Answers:")
print("The total number of loans is:", num_of_loans) #Return is 5
print("The sum of the total loans is: $", format(sum_of_loans, ',.2f')) 
print("The average loan price is: $", format(avg_loan_price, ',.2f'))

print()

## Part 2: Analyze Loan Data 

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

print("Part2 Answers:")
#1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
future_value = loan.get("future_value")
print("The future value is:", future_value)
remaining_months = loan.get("remaining_months")
print("The remaining months is:", remaining_months)

#2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.

# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
fair_value = future_value / ((1 + (.2/12))**remaining_months)
print("The fair value is: $", format(fair_value, ',.2f'))

#3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
loan_price = loan.get("loan_price")

if fair_value >= loan_price:
    print("The loan is worth at least the cost to buy it.")
#b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.    
else:
    print("The loan is too expensive and not worth the price.")
                                    
print()

## Part 3: Perform Financial Conditions

print("Part 3 Answers:")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# 1. Define a new function that will be used to calculate present value.
    # a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    # b. The function should return the `present_value` for the loan.
  

def present_value(new_future_value, new_remaining_months, annual_discount_rate):
    new_fair_value = new_future_value / ((1 + (annual_discount_rate/12))**new_remaining_months)
    return new_fair_value

    

new_future_value = new_loan.get("future_value")
new_remaining_months = new_loan.get("remaining_months")
annual_discount_rate = .2

new_present_val = present_value(new_future_value, new_remaining_months, annual_discount_rate)
print(f"The present value is: ${new_present_val: ,.2f}")

print()

## Part 4: Conditionally filter lists of loans
print("Part 4 Answers") 

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# 1. Create a new, empty list called `inexpensive_loans`.
inexpensive_loans = []

# 2. Use a for loop to select each loan from a list of loans.
    # a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    # b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
    