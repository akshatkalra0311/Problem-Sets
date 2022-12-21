#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

import math

annsal = float(input("Enter annual salary: "))
# portion_saved = float(input("What is the portion of your Salary saved: "))
# total_cost = float(input("What's the cost of your dream home: "))
total_cost = 1000000
# semi_annual_raise = float(input('Enter the bi-annual raise scale: '))
semi_annual_raise = 0.07
target_months = int(input('Enter the number of months you wish to save for: '))

portion_down_payment = 0.25 * total_cost
current_savings = 0
# monthly_salary = annual_salary/12
# Just added another comment to make an arbitrary update.
r = 0.04

portion_saved = 0
upper = 1
lower = 0.00
i = 1

while abs(portion_down_payment - current_savings) > 100:
    annual_salary = annsal
    if portion_saved >= 0.9800:
        print("It's not possible to pay the downpayment in 3 years.")
        break
    portion_saved = (upper + lower) / 2
    portion_saved = round(portion_saved, 4)
    # print(portion_saved)
    months = 0
    current_savings = 0
    while months < target_months + 1:
        # print(current_savings)
        if months > 0:
            current_savings += (r / 12) * current_savings
            # print(current_savings)
        if months % 6 == 0 and months != 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise

        current_savings += portion_saved * (annual_salary / 12)
        # print(current_savings)
        months += 1

    if current_savings < portion_down_payment:
        lower = portion_saved
    else:
        upper = portion_saved
    # print(current_savings)
    # print('Bisection #', i)
    i += 1

print('Best Saving Rate:', portion_saved)
print('Steps in Bisection Search:', i - 1)