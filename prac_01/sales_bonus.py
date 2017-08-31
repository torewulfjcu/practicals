"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1000, the user gets a 10% bonus.
If sales are $1000 or over, the bonus is 15%
"""

bonus = 0
sales = float(input("Enter sales: $"))

# a negative sales number quits the program (breaks the while loop)
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print("Bonus based on sales: ${:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))

print("Thank you.")
